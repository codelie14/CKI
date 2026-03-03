import MySQLdb

def create_database():
    try:
        db = MySQLdb.connect(host="localhost", user="root", password="")
        cursor = db.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS cki_db")
        print("Database 'cki_db' created or already exists.")
        db.close()
    except Exception as e:
        print(f"Error creating database: {e}")

if __name__ == "__main__":
    create_database()
