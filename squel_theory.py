import sqlite3

conn = sqlite3.connect('book_store.sqlite3')
cursor = conn.cursor()

cursor.execute('DROP TABLE IF EXISTS books')
cursor.execute('DROP TABLE IF EXISTS authors')

cursor.execute('''
CREATE TABLE authors (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    birth_year INTEGER NOT NULL
)
''')

cursor.execute('''
CREATE TABLE books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    author_id INTEGER NOT NULL,
    price REAL NOT NULL,
    description TEXT,
    FOREIGN KEY (author_id) REFERENCES authors(id),
    UNIQUE(title, author_id)
)
''')

authors_data = [
    ("Stephen King", 1947),
    ("Lewis Carroll", 1832),
    ("Taras Shevchenko", 1814),
    ("Lila Walter", 1990),
    ("Agatha Christie", 1890),
]

for author in authors_data:
    cursor.execute("INSERT OR IGNORE INTO authors (name, birth_year) VALUES (?, ?)", author)

authors_dict = {}
cursor.execute("SELECT id, name FROM authors")
authors = cursor.fetchall()
for author_id, name in authors:
    authors_dict[name] = author_id

def get_author_id(author_name):
    return authors_dict.get(author_name)

books_data = [
    ("The Shining", get_author_id("Stephen King"), 120.0, "A horror novel by Stephen King."),
    ("Alice's Adventures in Wonderland", get_author_id("Lewis Carroll"), 300.0, "An 1865 novel by Lewis Carroll."),
    ("Kobzar", get_author_id("Taras Shevchenko"), 100.0, "A collection of poems by Taras Shevchenko."),
    ("The Recipe of Marriage", get_author_id("Lila Walter"), 160.0, "A brand-new novel by Lila Walter."),
    ("Murder on the Orient Express", get_author_id("Agatha Christie"), 160.0, "A mysterious novel by Agatha Christie."),
    ("Carrie", get_author_id("Stephen King"), 95.0, "First novel of Stephen King."),
    ("Caterina", get_author_id("Taras Shevchenko"), 70.0, "A novel about life by Lewis Carroll."),
    ("In the glass House", get_author_id("Lila Walter"), 100.0, "A very moving novel by Lila Walter."),
    ("Life`s recipe", get_author_id("Lila Walter"), 200.0, "One of the best novels in Europe by Lila Walter."),
    ("Death on the Nile", get_author_id("Agatha Christie"), 110.0, "A bestseller by Agatha Christie.")
]

for book in books_data:
    cursor.execute("INSERT OR IGNORE INTO books (title, author_id, price, description) VALUES (?, ?, ?, ?)", book)

conn.commit()

query = "SELECT * FROM books LIMIT 2 OFFSET 1;"
cursor.execute(query)
second_and_third_books = cursor.fetchall()
print("Books:")
for book in second_and_third_books:
    print(book)



conn.close()
