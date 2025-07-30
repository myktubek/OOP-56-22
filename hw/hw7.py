import sqlite3

conn = sqlite3.connect('users.db')
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    author TEXT NOT NULL,
    user_id INTEGER,
    FOREIGN KEY (user_id) REFERENCES users(id)
)
""")

def add_book(title, author, user_id):
    cursor.execute("INSERT INTO books (title, author, user_id) VALUES (?, ?, ?)", (title, author, user_id))
    conn.commit()

def get_all_books():
    cursor.execute("""
    SELECT books.title, books.author, users.name
    FROM books
    JOIN users ON books.user_id = users.id
    """)
    results = cursor.fetchall()
    for title, author, user in results:
        print(f"Книга: {title}, Автор: {author}, Читатель: {user}")

def update_book_title(book_id, new_title):
    cursor.execute("UPDATE books SET title = ? WHERE id = ?", (new_title, book_id))
    conn.commit()

def delete_book(book_id):
    cursor.execute("DELETE FROM books WHERE id = ?", (book_id,))
    conn.commit()

def update_book_title(book_id, new_title):
    cursor.execute("UPDATE books SET title = ? WHERE id = ?", (new_title, book_id))
    conn.commit()

cursor.execute("INSERT OR IGNORE INTO users (id, name) VALUES (1, 'naruto')")
cursor.execute("INSERT OR IGNORE INTO users (id, name) VALUES (2, 'sasuke')")
cursor.execute("INSERT OR IGNORE INTO users (id, name) VALUES (3, 'Мыктыбек')")
conn.commit()

add_book("Гарри Поттер", "Дж. Роулинг", 1)
add_book("Преступление и наказание", "Ф.М. Достоевский", 2)
add_book("1984", "Джордж Оруэлл", 3)

print("\n📚 Список книг:")
get_all_books()

conn.close()


