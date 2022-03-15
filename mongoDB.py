import pymongo
import pprint

myclient = pymongo.MongoClient("mongodb://localhost:27017/")  # подключаемся к серверу
mydb = myclient["NewBD"]  # получаем доступ к базе данных

dblist = myclient.list_database_names()  # список баз данных
print(dblist)

mycol = mydb['newTab']  # создаем новую коллекцию или таблицу в БД
delcol = mydb['docStructure']

try:
    delcol.drop()
    print('удаление прошло успешно')
except:
    print("не получилось удалить")


#добавляем один элемент
mydict = {"name": "Andrey", 'alt': 16}
result = mycol.insert_one(mydict)
# print(result)
# print(result.inserted_id)
# print()

#добавляем несколько элементов
mydict = [{"name": "Arina", 'alt': 3},{"name": "Alyona", 'alt': 13}]
result = mycol.insert_many(mydict)
# print(type(result))
# print(result.inserted_ids)


#выборка всех по одному признаку
delquery = {'name': "Arina"}
result = mycol.find(delquery)

for x in result:
    print(x)

delcount = mycol.delete_many(delquery)
print(delcount.deleted_count)

# mycol.delete_many(result)
# for x in result:
#     print(x)

#надо понять как перебрать результаты добавления


# nameCol = str(input('Введите название таблицы'))
#
# collist = mydb.list_collection_names()
# if nameCol in collist:
#     print('ich finde')
#
# print(mydb.list_collection_names())
# print(mycol.list_collection_names())
