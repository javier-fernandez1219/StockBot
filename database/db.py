import pymongo
from pymongo import MongoClient

cluster = MongoClient("mongodb+srv://jafernandez1219:Y%40nk1219%21@stockwatch.y4bav.mongodb.net/test")
db = cluster["WatchList"]
collection = db["WatchList"]

