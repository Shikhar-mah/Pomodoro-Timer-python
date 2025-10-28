import datetime as dt

class Session:
    def __init__(self):
        self.start_time = None 
        self.end_time = None 
        self.duration = None

    def calculateDuration(self):
        self.duration = self.end_time - self.start_time
        return self.duration