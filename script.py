import json
from csv import DictReader

# Читаем csv (выбираем только Title, Author, Pages)
with open('books.csv') as f:
    books = DictReader(f)
    # Получаем нужные параметры Title, Author, Pages, Genre у книг
    book_data = ['Title', 'Author', 'Pages', 'Genre']
    cut_books = []
    for dataset in books:
        temp = {j: dataset[j] for j in book_data}
        cut_books.append(temp)
    # Получаем готовый итератор с отобранными кгигами
    book_data_iterator = iter(cut_books)

# Читаем json и получаем список (cut_users) читателей (выбираем тольо Name, Gender, Address)
with open('users.json', "r") as f:
    users = json.loads(f.read())
    # Получаем нужные параметры Name, Gender, Address, Age у читателей
    user_data = ['name', 'gender', 'address', 'age']
    cut_users = []
    for dataset in users:
        temp = {j: dataset[j] for j in user_data}
        cut_users.append(temp)

# Получаем среднее количество книг, которое будет выдано каждому читателю
average_amount = (len(cut_books)//len(cut_users))

""" Разбиваем список книг на "равные" части - результирующий список (separated_books) должен содержать в себе
28 списков книг (28 = количетство читателей) 27 из которых содержат по 7 (average_amount) книг, а последний -
22 книги (average_amount + остаток) """
separated_books = []
for i in range(len(cut_users)):
    temp_list = []
    for j in range(average_amount):
        temp_list.append(next(book_data_iterator))
    separated_books.append(temp_list)

# Добавляем "хвостик" из оставшихся книг в список для последнего читателя
for i in book_data_iterator:
    separated_books[-1].append(i)

# Добавляем каждому юзеру из списка cut_users ключ "books" - пустой список книг
book_key = {"books": []}
for user in cut_users:
    user.update(book_key)

# Пополняем пустые списки книг пользователей книгами из списка "separated_books"
counter = 0
for user in cut_users:
    user.update(books=separated_books[counter])
    counter += 1

# Создаем JSON из питоновского словаря
with open("result.json", "w") as f:
    s = json.dumps(cut_users, indent=4)
    # s = json.dumps(cut_users, indent=4)
    f.write(s)















