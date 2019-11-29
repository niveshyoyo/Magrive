import sqlite3


conn = sqlite3.connect('my_database.sqlite')
cursor = conn.cursor()
for row in cursor.execute("SELECT TORRENT_LINK, FILE_NAME, DRIVE_LINK from magrive_1"):
	print("torrent_link = ", row[0])
	print("FILE_NAME = ", row[1])
	print("DRIVE_LINK = ", row[2], "\n")
conn.commit()
conn.close()
