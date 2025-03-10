from models.room import Room

class Floor:
    def __init__(self, floor_number, rooms_count):
        self.floor_number = floor_number
        self.rooms = [Room(floor_number, i) for i in range(1,rooms_count+1)]

    def get_room(self, room_number):
        index = room_number - 1
        if 0 <= index <= len(self.rooms):
            return self.rooms[room_number]
        return None

    def get_adjacent_rooms(self, room_number):
        """Retorna las habitaciones adyacentes en el mismo piso"""
        adjacent = []
        if room_number > 1:
            adjacent.append(self.rooms[room_number - 1])
        if room_number < len(self.rooms):
            adjacent.append(self.rooms[room_number + 1])
        return adjacent