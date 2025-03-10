import random
from models.building import Building

class Simulation:
    def __init__(self):
        self.building = Building()
        self.turn = 0

    def configure(self, floors_count, rooms_per_floor):
        self.building = Building(floors_count, rooms_per_floor)
        self.turn = 0

    def add_initial_zombies(self, count=1):
        """Añade zombis aleatorios al inicio de la simulación"""
        floors_count = len(self.building.floors)
        if floors_count == 0:
            return

        for _ in range(count):
            floor_num = random.randint(1, floors_count)
            floor = self.building.get_floor(floor_num)
            if floor and floor.rooms:
                room_num = random.randint(1, len(floor.rooms))
                room = floor.get_room(room_num)
                room.add_zombies()

    def advance_turn(self):
        """Avanza un turno en la simulación, moviendo zombis"""
        self.turn += 1

        # Recolectar todas las habitaciones con zombis
        zombie_rooms = []
        for floor in self.building.floors:
            for room in floor.rooms:
                if room.has_zombies and not room.is_locked:
                    zombie_rooms.append(room)

        # Propagar zombis a habitaciones adyacentes
        new_infections = []
        for room in zombie_rooms:
            adjacent_rooms = self.building.get_adjacent_rooms(room.floor_number, room.room_number)
            for adj_room in adjacent_rooms:
                if not adj_room.has_zombies and not adj_room.is_locked:
                    # Expansión de la infección
                    if random.random() < 0.50:
                        new_infections.append(adj_room)
                    # Traslado de zombis
                    else:
                        new_infections.append(adj_room)
                        room.remove_zombies()

        # Aplicar nuevas infecciones
        for room in new_infections:
            room.add_zombies()

        return len(new_infections)  # Retorna número de nuevas infecciones