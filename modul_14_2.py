import sqlite3

connection = sqlite3.connect("not_telegram.db")
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
''')

# cursor.execute('CREATE INDEX IF NOT EXISTS idx_email ON Users (email)')
# for i in range(1, 11):
#   cursor.execute('INSERT INTO Users (username, email, age, balance) VALUES ( ?, ?, ?, ?)', (f'User{i}', f'example{i}@gmail.com', f'{i * 10}', '1000'))

# cursor.execute('UPDATE Users SET balance = ? WHERE id % 2 = 1', (500,))
# cursor.execute('DELETE FROM Users WHERE id % 3 = 1')

# cursor.execute('SELECT * FROM Users WHERE age != ?', (60,))
# users = cursor.fetchall()
# for user in users:
#    username, email, age, balance = user[1], user[2], user[3], user[4]
#    print(f'Имя: {username} | Почта: {email} | Возраст: {age} | Баланс: {balance}')
cursor.execute('DELETE FROM Users WHERE id = ?', (6,))
cursor.execute('SELECT COUNT(*) FROM Users')
total = cursor.fetchone()[0]
print(total)
cursor.execute('SELECT SUM(balance) FROM Users')
total1 = cursor.fetchone()[0]
print(total1)
print(total1 / total)
cursor.execute("SELECT AVG(balance) FROM Users")
total2 = cursor.fetchone()[0]
print(total2)
connection.commit()
connection.close()
