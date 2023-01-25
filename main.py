# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import pymongo
from pymongo.server_api import ServerApi
from pymongo import MongoClient

cluster = "mongodb+srv://dayogreats:passphrase2a@bororodb.3nhijyk.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(cluster)

# print(client.list_database_names())

db = client.bororodb

dl = client.list_database_names()
print(dl)

col = db.list_collectio_names()

# print(col)

print(db.list_collectio_names())

todo1 = {
    "name": "Patcrik",
    "text": "My first todos",
    "status": "open"
}
#
todos = db.bororocollection

print(todos)

#
result = todos.insert_one(todo1)



# print(db.list_collection_names())

# class MongoDBConnection:
#     def __init__(self, dbname, host='localhost', port=27017):
#         self.client = MongoClient(host, port)
#         self.db = self.client[dbname]
#
#     def close(self):
#         self.client.close()
#
#     def collection(self, col):
#         return self.db[f"{col}"]
#
#     # Usage
#
#
# def main():
# conn = MongoDBConnection(dbname='mydb')
# collection = conn.db.mycollection
# # do something with collection
# conn.collection('hero_colletn')
# conn.close()

# cloud connection options
# cluster = "mongodb+srv://dayogreats:passphrase2@bororo-cluster.3nhijyk.mongodb.net/?retryWrites=true&w=majority"
# client = MongoClient(cluster)
#
# print(client.list_database_names())
#
# db = client.hero_test
#
# print(db.list_collection_names())


# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     main()
