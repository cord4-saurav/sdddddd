from django.shortcuts import render

import pymongo
from pymongo.errors import BulkWriteError



myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["mydatabase"]

mycol = mydb["customers"]

mylist = [
  {"_id": 1, "name": "John", "address": "Highway 37"}

]

x = mycol.insert_many(mylist)





print(myclient.list_database_names())




