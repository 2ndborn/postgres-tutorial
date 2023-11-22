import psycopg2


# connect to the "chinook" data# base
connection = psycopg2.connect(database="chinook")

# Build a cursor object of the database
cursor = connection.cursor()

# Query 1 - select all records from the "Artist" table
# cursor.execute('SELECT * FROM "Artist"')

# Query 2 - select only the "Name" column from the "Artist" table
# cursor.execute('SELECT "Name" FROM "Artist"')

# Query 3 - select only "Queen" from the "Artist" table
# cursor.execute('SELECT * FROM "Artist" WHERE "Name" = %s', ["Queen"])

# Query 4 - select only "ArtistId" from the "Artist" table
# cursor.execute('SELECT * FROM "Artist" WHERE "ArtistId" = %s', [51])

# Query 4 - select only "ArtistId" from the "Artist" table
# cursor.execute('SELECT * FROM "Album" WHERE "ArtistId" = %s', [51])

# Query 4 - select only "ArtistId" from the "Artist" table
cursor.execute('SELECT * FROM "Track" WHERE "Composer" = %s', ["Queen"])

# fetch the results (multiple)
results = cursor.fetchall()

# fetch the results (single)
# results = cursor.fetchone()

# close the connection
connection.close()

# print result
for result in results:
    print(result)
