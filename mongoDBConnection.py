from pymongo import MongoClient
# pprint library is used to make the output look more pretty
#from pprint import pprint
# connect to MongoDB, change the << MONGODB URL >> to reflect your own connection string
client = MongoClient('mongodb://admin:N4r4nj0$@cluster0-shard-00-00.zi9uo.mongodb.net:27017,cluster0-shard-00-01.zi9uo.mongodb.net:27017,cluster0-shard-00-02.zi9uo.mongodb.net:27017/myFirstDatabase?ssl=true&replicaSet=atlas-bht7sv-shard-0&authSource=admin&retryWrites=true&w=majority')
db=client.admin
# Issue the serverStatus command and print the results
serverStatusResult=db.command("serverStatus")
print(serverStatusResult)