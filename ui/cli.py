from simulation.simulator import Simulation
import os

class ZombieCrisisUI:
    def __init__(self):
        self.simulation = Simulation()

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def print_building_state(self):
        """Muestra el estado actual del edificio"""
        self.clear_screen()
        print(f"=== ZOMBIE CRISIS SIMULATOR - TURN {self.simulation.turn} ===\n")

        for floor_idx, floor in enumerate(reversed(self.simulation.building.floors)):
            actual_floor = len(self.simulation.building.floors) - floor_idx - 1
            print(f"Floor {actual_floor}:")
            for room in floor.rooms:
                print(room)

    def configure_building(self):
        """Configura el edificio inicial"""
        self.clear_screen()
        print("=== BUILDING CONFIGURATION ===\n")

        try:
            floors = int(input("Number of floors: "))
            rooms = int(input("Number of rooms per floor: "))
            zombies = int(input("Initial number of zombies: "))

            self.simulation.configure(floors, rooms)
            self.simulation.add_initial_zombies(zombies)
            print("\nBuilding configured successfully!")
            input("Press Enter to continue...")
        except ValueError:
            print("\nInvalid input. Please enter numbers only.")
            input("Press Enter to try again...")
            self.configure_building()

    def advance_simulation(self):
        """Avanza un turno en la simulación"""
        new_infections = self.simulation.advance_turn()
        print(f"\nTurn {self.simulation.turn} completed. {new_infections} new rooms infected.")
        input("Press Enter to continue...")

    def clean_room(self):
        """Limpia zombis de una habitación específica"""
        try:
            floor_num = int(input("Floor number: "))
            room_num = int(input("Room number: "))

            room = self.simulation.building.get_room(floor_num, room_num)
            if room:
                room.remove_zombies()
                print(f"Room {room_num} on Floor {floor_num} has been cleaned.")
            else:
                print("Invalid room or floor number.")
        except ValueError:
            print("Invalid input. Please enter numbers only.")

        input("Press Enter to continue...")

    def reset_sensor(self):
        """Resetea el sensor de una habitación específica"""
        try:
            floor_num = int(input("Floor number: "))
            room_num = int(input("Room number: "))

            room = self.simulation.building.get_room(floor_num, room_num)
            if room:
                room.reset_sensor()
                print(f"Sensor in Room {room_num} on Floor {floor_num} has been reset.")
            else:
                print("Invalid room or floor number.")
        except ValueError:
            print("Invalid input. Please enter numbers only.")

        input("Press Enter to continue...")

    def run(self):
        """Ejecuta el menú principal"""
        self.configure_building()

        while True:
            self.print_building_state()
            print("\nMENU:")
            print("1. Advance simulation (1 turn)")
            print("2. Clean room (remove zombies)")
            print("3. Reset sensor")
            print("4. Reconfigure building")
            print("5. Exit")

            choice = input("\nEnter your choice (1-5): ")

            if choice == '1':
                self.advance_simulation()
            elif choice == '2':
                self.clean_room()
            elif choice == '3':
                self.reset_sensor()
            elif choice == '4':
                self.configure_building()
            elif choice == '5':
                print("Thank you for using Zombie Crisis Simulator!")
                break
            else:
                print("Invalid choice. Please try again.")
                input("Press Enter to continue...")