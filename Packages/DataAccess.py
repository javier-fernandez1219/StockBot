from pymongo import MongoClient

class dal:
    def __init__(self):
        self.connection = 'mongodb://admin:N4r4nj0$@cluster0-shard-00-00.zi9uo.mongodb.net:27017,cluster0-shard-00-01.zi9uo.mongodb.net:27017,cluster0-shard-00-02.zi9uo.mongodb.net:27017/myFirstDatabase?ssl=true&replicaSet=atlas-bht7sv-shard-0&authSource=admin&retryWrites=true&w=majority'
    def add_user(self, user):
        client = MongoClient(self.connection)
        db = client.sw
        db.users.insert_one(user)
    def get_user(self, userid):
        client = MongoClient(self.connection)
        db = client.sw
        return db.users.find_one({'userid': userid})
    def upd_user(self, userwl):
        client = MongoClient(self.connection)
        db = client.sw
        db.users.replace_one({'_id': userwl.get('_id')},userwl)
