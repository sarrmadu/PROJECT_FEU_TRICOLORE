import sqlite3
import os

class Database:
    def __init__(self, db_path="logs/simulation.db"):
        # Crée le dossier logs si inexistant
        os.makedirs(os.path.dirname(db_path), exist_ok=True)
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            action TEXT,
            feu TEXT,
            scenario TEXT
        )
        """)
        self.conn.commit()

    def log(self, timestamp, action, feu, scenario):
        self.cursor.execute(
            "INSERT INTO logs VALUES (NULL, ?, ?, ?, ?)",
            (timestamp, action, feu, scenario)
        )
        self.conn.commit()
