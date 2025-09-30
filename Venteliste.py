import heapq  # Til priority queue
import datetime  # Til tidsstempler

class Patient:
    def __init__(self, name, age, urgency, reason):
        self.name = name
        self.age = age
        self.urgency = urgency  # Lavere tal = højere prioritet (f.eks. 1 = kritisk, 3 = rutine)
        self.reason = reason
        self.added_time = datetime.datetime.now()
        self.id = id(self)  # Simpel unik ID

    def __lt__(self, other):  # Til heapq-sortering: Først urgency, derefter tid
        return (self.urgency, self.added_time) < (other.urgency, other.added_time)

    def __str__(self):
        return f"ID: {self.id} | Navn: {self.name} | Alder: {self.age} | Urgency: {self.urgency} | Årsag: {self.reason} | Tilføjet: {self.added_time.strftime('%Y-%m-%d %H:%M')}"

class Venteliste:
    def __init__(self):
        self.queue = []  # Priority queue (heap)

    def add_patient(self, patient):
        heapq.heappush(self.queue, patient)
        print(f"Patient tilføjet: {patient}")

    def remove_next_patient(self):
        if not self.queue:
            print("Ventelisten er tom.")
            return None
        patient = heapq.heappop(self.queue)
        print(f"Patient fjernet: {patient}")
        return patient

    def show_list(self):
        if not self.queue:
            print("Ventelisten er tom.")
            return
        print("Aktuel venteliste (sorteret efter prioritet og tid):")
        for patient in sorted(self.queue):  # Sorteret visning
            print(patient)

    def search_patient(self, name):
        for patient in self.queue:
            if patient.name.lower() == name.lower():
                print(f"Fundet: {patient}")
                return patient
        print("Patient ikke fundet.")
        return None

# Eksempel på brug
if __name__ == "__main__":
    vl = Venteliste()

    # Tilføj nogle patienter
    vl.add_patient(Patient("Anne Jensen", 45, 2, "Rutinekontrol"))
    vl.add_patient(Patient("Frederik Nielsen", 22, 1, "Akut lungecancer"))
    vl.add_patient(Patient("Clara Olsen", 30, 3, "Forebyggende undersøgelse"))

    # Vis listen
    vl.show_list()

    # Søg efter en patient
    vl.search_patient("Bob Hansen")

    # Fjern næste patient (højeste prioritet først)
    vl.remove_next_patient()

    # Vis opdateret liste

    vl.show_list()
