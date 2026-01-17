from datetime import datetime

class Logger:
    def __init__(self, database):
        self.db = database

    def log(self, action, feu, scenario):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.db.log(timestamp, action, feu, scenario)
