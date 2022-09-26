import csv

f = open('result.txt', 'w')
with open('books.csv', 'r') as csvfile:
    books = csv.reader(csvfile, delimiter=';')

    zadanie1 = -1
    zadanie2 = 0  # переменная для 2 задания
    avtor = input('Введите автора')  # 7 вариант
    poisk = input(
        'Введите 1, если хотите ввести 20 ID книг для библиографической ссылки, иначе введите 0 для случайного набора ')
    massiv4 = []
    tags_array = []
    flag4 = 0
    zadanie4 = 20

    massiveDop2 = []


    # Задание 1
    for row in books:
        zadanie1 += 1

with open('books.csv', 'r') as csvfile:
    books = csv.reader(csvfile, delimiter=';')
    # Задание 2
    massiv4 = []
    tags_array = []
    massiveDop2 = []
    for row in books:

        if len(row[1]) > 30:
            zadanie2 += 1

    # Задание 3 вариант 7
with open('books.csv', 'r') as csvfile:
    books = csv.reader(csvfile, delimiter=';')
    massiv4 = []
    tags_array = []
    massiveDop2 = []
    for row in books:
        year = row[6].split()
        year = year[0].split('.')
        year = year[-1]

        surname = row[3].split()
        surname = surname[-1:]
        if len(surname) > 0:
            if (avtor == str(surname[0])) and 2016 < int(year) < 2018:
                print(row[1])

    # Задание 4
with open('books.csv', 'r') as csvfile:
    books = csv.reader(csvfile, delimiter=';')
    massiv4 = []
    tags_array = []
    massiveDop2 = []
    zadanie1 = 0
    if poisk == '1':
        for i in range(zadanie4):
            massiv4.append(input('Введите ID искомой книги '))
    else:
        flag4 = 1
    for row in books:
        zadanie1+=1
        if flag4 == 0:
            if row[0] in massiv4:
                f.write('<' + str(surname[0]) + '>. <' + str(row[1]) + '> - <' + str(year) + '>' + '\n')
        elif (flag4 == 1) and (zadanie1 < 22) and (zadanie1 > 1):
            f.write('<' + str(surname[0]) + '>. <' + str(row[1]) + '> - <' + str(year) + '>' + '\n')

        # Дополнительное задание 1
with open('books.csv', 'r') as csvfile:
    books = csv.reader(csvfile, delimiter=';')
    tags_array = []
    for row in books:
        tags = row[12].split('#')
        for tag in tags:
            if not (tag in tags_array):
                tags_array.append(tag)

    print('Всего записей = ', zadanie1)
    print('Количество зназваний длиннее длиной 30 = ', zadanie2)
    tags_array.pop(0)
    tags_array.pop(0)
    print('Перечень всех тегов: ', tags_array)
f.close()
