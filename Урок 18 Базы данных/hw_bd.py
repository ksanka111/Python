# Создайте новую Базу данных.
# Поля: id, 2 целочисленных поля
# Целочисленные поля заполняются рандомно от 0 до 9.
# Посчитайте среднее арифметическое всех элементов без учёта id.
# Если среднее арифметическое больше количества записей в БД, то удалите четвёртую запись БД.

import sqlite3
import random

conn = sqlite3.connect('alfa.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS my_tab(id INTEGER PRIMARY KEY AUTOINCREMENT, col_1 INT, col_2 INT)''')
cursor.execute('''INSERT INTO my_tab(col_1, col_2) VALUES (?,?)''', (random.randint(0, 9), random.randint(0, 9)))
conn.commit()

cursor.execute('''SELECT col_1, col_2 FROM my_tab''')
k = cursor.fetchall()
print(k)
sr_ar = []
sr_ar_n = 0
for i in k:
    s = ','.join([str(s) for s in i])   # делаем все строками
    c = sum(i)/len(i)   # находим ср.арифм. каждой строки
    sr_ar.append(c)     # добавляем значения ср.арифм. в список sr_ar
    sr_ar_n = sum(sr_ar)/len(sr_ar)     # ср.арифм. от средних арифметических
if sr_ar_n > len(k):
    cursor.execute('''DELETE FROM my_tab  WHERE id=4''')     # удаляем четвертую запись по условию выше
    cursor.execute('''SELECT*FROM my_tab''')    # запрашиваем таблицу и получаем ее атрибуты
    k = cursor.fetchall()
print(k)
print('\nСреднее арифметическое: ', float(sr_ar_n))
print('Количество записей в БД: ', len(k))


