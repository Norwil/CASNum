import sqlite3
from prettytable import PrettyTable
from chemical import Chemical

class Database:
    def __init__(self):
        self.conn = sqlite3.connect("chemicals.db")
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS chemicals (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            cas_number TEXT UNIQUE,
            name TEXT,
            banned INTEGER,
            classification TEXT,
            melting_point REAL,
            boiling_point REAL,
            flashpoint REAL,
            storage_temp REAL
        );
        """
        self.cursor.execute(query)
        self.conn.commit()

    def insert(self, chemical: Chemical):
        try:
            query = f"INSERT INTO chemicals (cas_number, name, banned, classification, melting_point, boiling_point, flashpoint, storage_temp) VALUES ('{chemical.name}', '{chemical.cas_number}', {chemical.banned}, '{chemical.classification}', {chemical.melting_point}, {chemical.boiling_point}, {chemical.flashpoint}, {chemical.storage_temp});"
            self.cursor.execute(query)
            self.conn.commit()
        except sqlite3.IntegrityError as e:
            print(f"Error: {e}")
            print(f"Chemical with CAS number '{chemical.cas_number}' already exists in the database.")

    def add_data(self, data):
        conn = sqlite3.connect("chemicals.db")
        c = conn.cursor()

        for chemical in data:
            cas_number, name, banned, classification, melting_point, boiling_point, flashpoint, storage_temp = chemical
            try:
                c.execute("INSERT INTO chemicals (cas_number, name, banned, classification, melting_point, boiling_point, flashpoint, storage_temp) VALUES (?,?,?,?,?,?,?,?)",
                          (cas_number, name, banned, classification, melting_point, boiling_point, flashpoint, storage_temp))
            except sqlite3.IntegrityError:
                print(f"Duplicate CAS number: {cas_number}")

        conn.commit()
        conn.close()

    def fetch(self, id: int):
        query = f"SELECT * FROM chemicals WHERE id={id};"
        self.cursor.execute(query)
        return self.cursor.fetchone()

    def remove(self, id: int):
        query = f"DELETE FROM chemicals WHERE id={id};"
        self.cursor.execute(query)
        self.conn.commit()

    def update(self, id: int, chemical: Chemical):
        query = f"UPDATE chemicals SET cas_number='{chemical.cas_number}', name='{chemical.name}', banned={chemical.banned}, classification='{chemical.classification}', melting_point={chemical.melting_point}, boiling_point={chemical.boiling_point}, flashpoint={chemical.flashpoint}, storage_temp={chemical.storage_temp} WHERE id={id};"
        self.cursor.execute(query)
        self.conn.commit()

    def select(self):
        query = "SELECT * FROM chemicals;"
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def close(self):
        self.conn.close()

    def show(self):
        chemicals = self.select()

        table = PrettyTable()
        table.field_names = ["id", "Name", "CAS Number", "Banned", "Classification", "Melting Point", "Boiling Point", "Flash Point", "Storage Temperature"]
        for chemical in chemicals:
            table.add_row(chemical)
        print(table)
