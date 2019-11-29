import sqlite3
conn = sqlite3.connect('my_database.sqlite')
cursor = conn.cursor()
print("Opened database successfully")

cursor.execute('''CREATE TABLE magrive_1
         (TORRENT_LINK TEXT PRIMARY KEY     NOT NULL,
         FILE_NAME           TEXT    NOT NULL,
         DRIVE_LINK         TEXT    NOT NULL);''')

conn.commit()
cursor.close()
