import heapq
import datetime

# Se problemformuleringen inde på README.md filen i projektmappen

class Patient:
    def __init__(self, name, age, urgency, reason, læge=None):
        self.name = name
        self.age = age
        self.urgency = urgency
        self.reason = reason
        self.læge = læge
        self.added_time = datetime.datetime.now()
        self.id = id(self)

    def __lt__(self, other):
        return (self.urgency, self.added_time) < (other.urgency, other.added_time)

    def __str__(self):
        return (
            f"ID: {self.id} | Navn: {self.name} | Alder: {self.age} | "
            f"Prioritet: {self.urgency} | Årsag: {self.reason} | "
            f"Læge: {self.læge.name if self.læge else 'Ingen'} | "
            f"Tilføjet: {self.added_time.strftime('%Y-%m-%d %H:%M')}"
        )

class Læge:
    def __init__(self, name, age, speciale):
        self.name = name
        self.age = age
        self.speciale = speciale
        self.added_time = datetime.datetime.now()
        self.id = id(self)

    def __str__(self):
        return f"Læge ID: {self.id} | Navn: {self.name} | Alder: {self.age} | Speciale: {self.speciale}"

        

class Venteliste:
    def __init__(self):
        self.queue = []  # Priority queue for patienter
        self.læger = []  # Liste for læger

    def add_patient(self, patient):
        heapq.heappush(self.queue, patient)
        print(f"✅ Patient tilføjet: {patient}")

    def add_læge(self, læge):
        self.læger.append(læge)
        print(f"✅ Læge tilføjet: {læge}")

    def remove_next_patient(self):
        if not self.queue:
            print("Ventelisten er tom.")
            return None
        patient = heapq.heappop(self.queue)
        print(f"🩺 Patient fjernet: {patient}")
        return patient

    def show_list(self):
        if not self.queue:
            print("Ventelisten er tom.")
            return
        print("📋 Aktuel venteliste (sorteret efter prioritet og tid):")
        for patient in sorted(self.queue):
            print(patient)

    def show_læger(self):
        if not self.læger:
            print("Ingen læger tilføjet endnu.")
            return
        print("👨‍⚕️ Aktuelle læger:")
        for i in self.læger:
            print(i)

    def find_læge(self, name):
        for i in self.læger:
            if i.name.lower() == name.lower():
                return i
        return None

    def search_patient(self, name):
        for patient in self.queue:
            if patient.name.lower() == name.lower():
                print(f"🔍 Fundet: {patient}")
                return patient
        print("Patient ikke fundet.")
        return None

# ---- Hovedprogram ----
if __name__ == "__main__":
    vl = Venteliste()

    def menu():
        print("\n--- VENTELISTE SYSTEM ---")
        print("1. Tilføj patient")
        print("2. Vis venteliste")
        print("3. Søg patient")
        print("4. Fjern næste patient (højeste prioritet)")
        print("5. Tilføj læge")
        print("6. Vis læger")
        print("7. Afslut")
        return input("Vælg en mulighed (1-7): ")

    while True:
        valg = menu()

        if valg == "1":
            print("\n--- Tilføj patient ---")
            name = input("Navn: ")
            age = input("Alder: ")
            urgency = input("Prioritet (1=høj, 3=lav): ")
            reason = input("Årsag: ")
            læge_navn = input("Læge (indtast navn eller lad stå tomt): ")
            læge = vl.find_læge(læge_navn) if læge_navn else None
            try:
                patient = Patient(name, int(age), int(urgency), reason, læge)
                vl.add_patient(patient)
            except ValueError:
                print("Fejl: Alder og prioritet skal være tal.")

        elif valg == "2":
            vl.show_list()

        elif valg == "3":
            name = input("Indtast patientnavn: ")
            vl.search_patient(name)

        elif valg == "4":
            vl.remove_next_patient()
        elif valg == "5":
            print("\n--- Tilføj læge ---")
            name = input("Navn: ")
            age = input("Alder: ")
            speciale = input("Speciale: ")
            try:
                læge = Læge(name, int(age), speciale)
                vl.add_læge(læge)
            except ValueError:
                print("Fejl: Alder skal være et tal.")

        elif valg == "6":
            vl.show_læger()

        elif valg == "7":
            print("Afslutter programmet...")
            break

        else:
            print("Ugyldigt valg, prøv igen.")

