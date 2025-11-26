from typing import List, Optional

USERNAME = "secretary"
PASSWORD = "12345"


def login() -> bool:
    """Displays login menu and handles login."""
    
    while True:
        print("1. Login")
        print("2. Exit System")

        choice = input("Enter choice (1-2): ").strip()

        if choice == "1":
            username = input("Username: ").strip()
            password = input("Password: ").strip()

            if username == USERNAME and password == PASSWORD:
                return True
            else:
                print(" Incorrect username or password.\n")

        elif choice == "2":
            print("\nExiting system... Goodbye!")
            exit()

        else:
            print("Invalid choice. Enter 1 or 2.")


# PATIENT CLASS
class Patient:
    """Represents a patient in the queue."""
    def __init__(self, name: str, concern: str, queue_number: int):
        self.name = name
        self.concern = concern
        self.queue_number = queue_number

    def __str__(self) -> str:
        return f"Q:{self.queue_number:03d} | Name: {self.name.ljust(15)} | Concern: {self.concern}"


# CLINIC SYSTEM
class ClinicSystem:
    """Manages patient registration and queue."""
    def __init__(self):
        self.patient_queue: List[Patient] = []
        self._next_queue_number = 1

    def register_patient(self, name: str, concern: str) -> None:
        queue_num = self._next_queue_number
        new_patient = Patient(name, concern, queue_num)
        self.patient_queue.append(new_patient)
        self._next_queue_number += 1

        print(f"Patient Registered: {new_patient.name}")
        print(f"   Assigned Queue Number: Q-{queue_num:03d}")
    
    def view_queue(self) -> None:
        print("\nCURRENT QUEUE")
        if not self.patient_queue:
            print("The queue is currently empty.")
            return

        for patient in self.patient_queue:
            print(patient)

        print(f"Total Patients Waiting: {len(self.patient_queue)}")

    def call_next_patient(self) -> Optional[Patient]:
        if not self.patient_queue:
            print("\nCannot call patient: The queue is empty.")
            return None

        next_patient = self.patient_queue.pop(0)

        print("\nCALLING NEXT PATIENT ")
        print(f"Calling Patient Q-{next_patient.queue_number:03d}...")
        print(f"Name: {next_patient.name}")
        print(f"Concern: {next_patient.concern}")
        return next_patient


# SECRETARY MENU
def secretary_menu(system: ClinicSystem):
    while True:
        print("\nSECRETARY MENU")
        print("1. Register Patient")
        print("2. View Current Queue")
        print("3. Call Next Patient")
        print("4. Logout")

        choice = input("Enter your choice (1-4): ").strip()

        if choice == '1':
            name = input("Enter patient name: ").strip().title()
            concern = input("Enter primary concern: ").strip()

            if name and concern:
                system.register_patient(name, concern)
            else:
                print("Both name and concern are required.")

        elif choice == '2':
            system.view_queue()

        elif choice == '3':
            system.call_next_patient()

        elif choice == '4':
            print("Logging out...\n")
            break

        else:
            print("Invalid choice. Please enter 1-4.")


# MAIN APPLICATION
def main():
    system = ClinicSystem()

    print("PATIENT CHECK-IN SYSTEM")
    

    while True:
        # Login screen with Exit System
        login()

        # Secretary menu
        secretary_menu(system)

        print("Returning to login screen...\n")


if __name__ == "__main__":
    main()