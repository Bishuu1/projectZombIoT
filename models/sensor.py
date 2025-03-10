class Sensor:
    NORMAL = "normal"
    ALERT = "alert"

    def __init__(self):
        self.state = self.NORMAL

    def set_alert(self):
        self.state = self.ALERT

    def reset(self):
        self.state = self.NORMAL

    def is_alert(self):
        return self.state == self.ALERT