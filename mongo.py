
import pymongo
client = pymongo.MongoClient("mongodb+srv://padmeshkg:lovers9081@padmesh.jw0quv5.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print (db)

d ={
    "name": "Padmesh",
    "emailid" : "padmeshkg@gmail.com",
    "surname": "kumar"
}

db1 = client['mongo']
coll = db1['test']
coll.insert(d)

