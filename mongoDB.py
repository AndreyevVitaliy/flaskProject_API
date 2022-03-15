import pymongo
import pprint

myclient = pymongo.MongoClient("mongodb://localhost:27017/")  # подключаемся к серверу
mydb = myclient["NewBD"]  # получаем доступ к базе данных

dblist = myclient.list_database_names()  # список баз данных
print(dblist)

mycol = mydb['newTab']  # создаем новую коллекцию или таблицу в БД

#добавляем один элемент
mydict = {"name": "Andrey", 'alt': 16}
result = mycol.insert_one(mydict)
print(result)
print(result.inserted_id)
print()

#добавляем несколько элементов
mydict = [{"name": "Arina", 'alt': 3},{"name": "Alyona", 'alt': 13}]
result = mycol.insert_many(mydict)
print(type(result))
print(result.inserted_ids)

#надо понять как перебрать результаты добавления


# nameCol = str(input('Введите название таблицы'))
#
# collist = mydb.list_collection_names()
# if nameCol in collist:
#     print('ich finde')
#
# print(mydb.list_collection_names())
# print(mycol.list_collection_names())
