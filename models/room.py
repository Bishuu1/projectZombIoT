import random
from models.sensor import Sensor

class Room:
    def __init__(self, floor_number, room_number):
        self.floor_number = floor_number
        self.room_number = room_number
        self.sensor = Sensor()
        self.has_zombies = False
        self.is_locked = True if random.random() < 0.50 else False

    def add_zombies(self):
        self.has_zombies = True
        self.sensor.set_alert()

    def remove_zombies(self):
        self.has_zombies = False
        # No se reseta el sensor al limpiar la habitación

    def reset_sensor(self):
        self.sensor.reset()

    def lock(self):
        self.is_locked = True
    
    def unlock(self):
        self.is_locked = False

    def __str__(self):
        status = "🧟" if self.has_zombies else "👌"
        sensor = "🔴" if self.sensor.is_alert() else "🟢"
        lock = "🔒" if self.is_locked else "🔓"
        return f"Room {self.room_number} - Status: {status} - Sensor: {sensor} - Lock: {lock}"