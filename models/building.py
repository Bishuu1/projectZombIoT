from models.floor import Floor

class Building:
    def __init__(self, floors_count=1, rooms_per_floor=1):
        self.floors = []
        self.configure(floors_count, rooms_per_floor)

    def configure(self, floors_count, rooms_per_floor):
        self.floors = [Floor(i, rooms_per_floor) for i in range(1,floors_count+1)]

    def get_floor(self, floor_number):
        index = floor_number - 1
        if 0 <= index < len(self.floors):
            return self.floors[index]
        return None

    def get_room(self, floor_number, room_number):
        floor = self.get_floor(floor_number)
        if floor:
            return floor.get_room(room_number)
        return None

    def get_adjacent_rooms(self, floor_number, room_number):
        """Retorna habitaciones adyacentes (mismo piso y pisos adyacentes)"""
        adjacent = []

        # Habitaciones adyacentes en el mismo piso
        floor = self.get_floor(floor_number)
        if floor:
            adjacent.extend(floor.get_adjacent_rooms(room_number))

        # Habitaciones en pisos adyacentes (solo habitaciones al lado de escaleras, es decir, habitación 1)
        # Piso superior
        if floor_number < len(self.floors) and room_number == 1:
                upper_room = self.get_room(floor_number + 1, room_number)
                if upper_room:
                    adjacent.append(upper_room)

        # Piso inferior
        if floor_number > 0 and room_number == 1:
            lower_room = self.get_room(floor_number - 1, room_number)
            if lower_room:
                adjacent.append(lower_room)

        return adjacent