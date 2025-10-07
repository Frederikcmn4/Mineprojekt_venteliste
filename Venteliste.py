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
    vl.add_patient(Patient("Carl Knudsen", 22, 1, "Akut Testikelcancer"))
    vl.add_patient(Patient("Julie Dufresne", 18, 3, "Mentalvurdering"))

    # Vis listen
    vl.show_list()

    # Søg efter en patient
    vl.search_patient("Frederik Nielsen")

    # Fjern næste patient (højeste prioritet først)
    vl.remove_next_patient()

    # Vis opdateret liste

    vl.show_list()

# Kode til kørsel af script i terminal

    def menu():
        print("\n--- VENTELISTE SYSTEM ---")
        print("1. Tilføj patient")
        print("2. Vis venteliste")
        print("3. Søg patient")
        print("4. Fjern næste patient (højeste prioritet)")
        print("5. Afslut")
        return input("Vælg en mulighed (1-5): ")

    while True:
        valg = menu()

        if valg == "1":
            print("\n--- Tilføj patient ---")
            name = input("Navn: ")
            age = input("Alder: ")
            urgency = input("Prioritet (1=høj, 3=lav): ")
            reason = input("Årsag: ")

            try:
                patient = Patient(name, int(age), int(urgency), reason)
                vl.add_patient(patient)
            except ValueError:
                print("Fejl: Alder og prioritet skal være tal.")

        elif valg == "2":
            print("\n--- Aktuel venteliste ---")
            vl.show_list()

        elif valg == "3":
            print("\n--- Søg patient ---")
            name = input("Indtast patientnavn: ")
            vl.search_patient(name)

        elif valg == "4":
            print("\n--- Fjern næste patient ---")
            vl.remove_next_patient()

        elif valg == "5":
            print("Afslutter programmet...")
            break

        else:
            print("Ugyldigt valg, prøv igen.")
