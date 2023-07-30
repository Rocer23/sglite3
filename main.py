import sqlite3

connection = sqlite3.connect("data.db")
cursor = connection.cursor()

sgl_insert = '''
INSERT INTO pupils (name, avg_score, class, parents)
VALUES ("Микола Прокопенко", 10, "12Г", "Оксана Прокопенко")'''

cursor.execute(sgl_insert)

sgl_insert = '''
INSERT INTO pupils (name, avg_score, class, parents)
VALUES ("Степан Гіга", 9, "7В", "Володимир Гіга")'''

cursor.execute(sgl_insert)

sgl_select = '''SELECT * FROM pupils WHERE id < (?)'''

pupils = cursor.execute(sgl_select, [5]).fetchall()

for pupil in pupils:
    print(pupil)

connection.commit()

cursor.close()
connection.close()