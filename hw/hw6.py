"""
Библиотека Faker используется для создания фейковых данных.
адрес, имя, профессия, др. итд
"""

from faker import Faker  # Импортируем библиотеку Faker

fake = Faker()  # Создаём объект генератора данных

# Создаем случайное имя
name = fake.name()
print(f"Случайное имя: {name}")

# Создаем случайный адрес
address = fake.address()
print(f"Случайный адрес: {address}")

# Создаем случайный email
email = fake.email()
print(f"Случайный email: {email}")

# Создаем случайную дату рождения
dob = fake.date_of_birth()
print(f"Дата рождения: {dob}")

# Создаем случайную профессию
job = fake.job()
print(f"Профессия: {job}")