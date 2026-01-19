from datetime import datetime
from persistence.database import Database

class Logger:
    def __init__(self):
        self.db = Database()

    def log(self, action, feu, scenario):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.db.log(timestamp, action, feu, scenario)
