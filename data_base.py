import sqlite3

conn = sqlite3.connect('season_info.sqlite3')
cursor = conn.cursor()

cursor.execute('DROP TABLE IF EXISTS seasons')
cursor.execute('DROP TABLE IF EXISTS directors')

cursor.execute('''
CREATE TABLE directors (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    UNIQUE(name)
)
''')

cursor.execute('''
CREATE TABLE seasons (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    numbering TEXT NOT NULL UNIQUE,
    years TEXT NOT NULL,
    description TEXT,
    how_much_likes REAL NOT NULL
)
''')

directors_data = [
    ("Russell T. Davies",),
    ("Steven Moffat",),
    ("Chris Chibnall",),
    ("Jodie Whittaker",),
    ("David Tennant",)
]

season_data = [
    ("Season 1", "2005-2006", "Russell T. Davies", 9.5),
    ("Season 2", "2006-2007", "Steven Moffat", 9.8),
    ("Season 3", "2007-2008", "Steven Moffat", 9.7),
    ("Season 4", "2008-2010", "Steven Moffat", 9.6),
    ("Season 5", "2010", "Chris Chibnall", 9.4),
]

for director in directors_data:
    cursor.execute("INSERT OR IGNORE INTO directors (name) VALUES (?)", director)

for season in season_data:
    cursor.execute("INSERT OR IGNORE INTO seasons (numbering, years, description, how_much_likes) VALUES (?, ?, ?, ?)", season)

conn.commit()

query = "SELECT * FROM seasons;"
cursor.execute(query)
all_seasons = cursor.fetchall()
print("Сезони:")
for season in all_seasons:
    print(season)

query = "SELECT * FROM directors;"
cursor.execute(query)
all_directors = cursor.fetchall()
print("Режисери:")
for director in all_directors:
    print(director)

conn.close()
