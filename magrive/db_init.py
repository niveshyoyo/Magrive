import sqlite3
# conn = sqlite3.connect('my_database.sqlite')
# cursor = conn.cursor()
# print("Opened database successfully")

# cursor.execute('''CREATE TABLE magrive_1
#          (TORRENT_LINK TEXT PRIMARY KEY     NOT NULL,
#          FILE_NAME           TEXT    NOT NULL,
#          DRIVE_LINK         TEXT    NOT NULL);''')

# conn.commit()
# cursor.close()

# ######insert
# conn = sqlite3.connect('my_database.sqlite')
# cursor = conn.cursor()
# cursor.execute("INSERT INTO magrive_1 (TORRENT_LINK, FILE_NAME, DRIVE_LINK) VALUES ('vsvs','caca', 'acca')");
# cursor.execute("INSERT INTO magrive_1 (TORRENT_LINK, FILE_NAME, DRIVE_LINK) \
#       VALUES ('csca','acssc', 'acas')");
# conn.commit()
# conn.close()

#####checking
conn = sqlite3.connect('my_database.sqlite')
cursor = conn.cursor()
for row in cursor.execute("SELECT TORRENT_LINK, FILE_NAME, DRIVE_LINK from magrive_1"):
	print("torrent_link = ", row[0])
	print("FILE_NAME = ", row[1])
	print("DRIVE_LINK = ", row[2], "\n")
conn.commit()
conn.close()

########finding
conn = sqlite3.connect('my_database.sqlite')
cursor = conn.cursor()
cursor.execute("SELECT FILE_NAME, DRIVE_LINK FROM magrive_1 WHERE TORRENT_LINK LIKE 'csca';");
a = cursor.fetchall()
print(a)
conn.commit()
conn.close()