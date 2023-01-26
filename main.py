# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import pymongo
from pymongo.server_api import ServerApi
from pymongo import MongoClient


#


class MongoDBConnecx:
    data = {
        "name": "Patcrik",
        "text": "My first todos",
        "status": "open"
    }

    def __init__(self, db, user, password):
        self.db = db
        self.user = user
        self.password = password

        self.cluster = f"mongodb+srv://{user}:{password}@{db}.3nhijyk.mongodb.net/?retryWrites=true&w=majority"
        self.cliente = MongoClient(self.cluster)

    def closer(self):
        self.cliente.close()

    def collex_list(self):
        cl = self.cliente.list_collection_names()
        print(cl)
        # return cl

    def db_list(self):
        dl = self.cliente.list_database_names()
        print(dl)
        return dl

    def collexion(self, cname, data):
        todos = self.cliente[f'{cname}']
        result = todos.insert_one(data)
        print(todos)


# print(db.list_collection_names())

class MongoDBConnection:
    def __init__(self, dbname, host='localhost', port=27017):
        self.client = MongoClient(host, port)
        self.db = self.client[dbname]

    def close(self):
        self.client.close()

    def collectx(self, coll):
        return self.db[f"{coll}"]

    # Usage


def main():
    #  OPTION 1 local db
    conn = MongoDBConnection(dbname='testDB')
    # print(conn.list_database_names())
    # conn.
    cs = conn.collectx('testCollection')
    print(cs)
    # do something with collection
    # conn.collection('hero_colletn')
    conn.close()

    # OPTION 2 cloud db
    mcon = MongoDBConnecx('bororodb', 'dayogreats', 'Password2a')

    # mcon.collexion('bororocollection', 'data')

    mcon.collex_list()
    mcon.db_list()
    mcon.closer()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
