import sqlite3

class Storage:
    def __init__(self):
        self.conn = sqlite3.connect('data.db')
        self.create_table()

    def create_table(self):
        try:
            cursor = self.conn.cursor()
            cursor.execute('''CREATE TABLE IF NOT EXISTS results (id INTEGER PRIMARY KEY, data TEXT)''')
            self.conn.commit()
        except sqlite3.Error as e:
            raise Exception(f"Failed to create table: {str(e)}")

    def save_to_db(self, data):
        try:
            cursor = self.conn.cursor()
            cursor.execute("INSERT INTO results (data) VALUES (?)", (str(data),))
            self.conn.commit()
        except sqlite3.Error as e:
            raise Exception(f"Failed to save to database: {str(e)}")

    def retrieve_data(self):
        try:
            cursor = self.conn.cursor()
            cursor.execute("SELECT * FROM results")
            rows = cursor.fetchall()
            return rows
        except sqlite3.Error as e:
            raise Exception(f"Failed to retrieve data: {str(e)}")

    def get_status(self):
        try:
            cursor = self.conn.cursor()
            cursor.execute("SELECT COUNT(*) FROM results")
            count = cursor.fetchone()[0]
            return f"{count} records found"
        except sqlite3.Error as e:
            raise Exception(f"Failed to get status: {str(e)}")
