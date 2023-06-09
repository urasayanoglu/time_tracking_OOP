"""User database class"""

import sqlite3


class UserDatabase:
    """Class UserDatabase to store the user name and day information"""

    def __init__(self):
        pass

    def create_database(self):
        """Create the database"""
        with sqlite3.connect('userdata.db') as connection:
            cursor = connection.cursor()
            cursor.execute('''CREATE TABLE IF NOT EXISTS users
                (name TEXT, day DATE, work_time DATE, break_time DATE)''')
            connection.commit()

    # If user appears in the database, continue without adding the user again.
    def add_user(self, name, day, work_time, break_time):
        """Add a new user to the database"""
        with sqlite3.connect('userdata.db') as connection:
            cursor = connection.cursor()
            try:
                cursor.execute('''INSERT INTO users (name, day, work_time, break_time) values(?,?,?,?)''',
                               (name, day, work_time, break_time))
                connection.commit()

            except:
                print("User already exists in database")

    def find_user(self, name):
        """Check if a specific user is in the database"""

        with sqlite3.connect('userdata.db') as connection:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM users WHERE name=?", (name,))
            # fetch the results and print them
            result = cursor.fetchone()

        if result:
            return result

    def find_date(self, day):
        """Check if a specific date is in the database"""

        with sqlite3.connect('userdata.db') as connection:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM users WHERE day=?", (day,))
            # fetch the results and print them
            result = cursor.fetchone()

        if result:
            return result

    def find_user_work_time(self, name, day):
        """Return the work time for a specific user and day"""
        with sqlite3.connect('userdata.db') as connection:
            cursor = connection.cursor()
            cursor.execute("SELECT work_time FROM users WHERE name=? AND day=?", (name, day))
            result = cursor.fetchone()

        if result:
            return result[0]

    def find_user_break_time(self, name, day):
        """Return the break time for a specific user and day"""
        with sqlite3.connect('userdata.db') as connection:
            cursor = connection.cursor()
            cursor.execute("SELECT break_time FROM users WHERE name=? AND day=?", (name, day))
            result = cursor.fetchone()

        if result:
            return result[0]

    def clean_database(self):
        '''Keeps the database but empties the tables'''

        with sqlite3.connect('userdata.db') as connection:
            cursor = connection.cursor()
            cursor.execute('''DROP TABLE IF EXISTS users''')
            connection.commit()

    def see_database(self):
        '''function to print out entire database'''

        with sqlite3.connect('userdata.db') as connection:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM users")
            # fetch the results and print them
            result = cursor.fetchall()
            print(result)

    def update_user(self, name, day, work_time, break_time):
        """Update a user's information in the database"""
        with sqlite3.connect('userdata.db') as connection:
            cursor = connection.cursor()
            cursor.execute('''UPDATE users SET work_time=?, break_time=? WHERE name=? AND day=?''', (work_time, break_time, name, day))
            connection.commit()
