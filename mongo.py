
import pymongo
client = pymongo.MongoClient("mongodb+srv://padmesh:lovers9081@cluster0.sbvylrz.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print (db)

data = {
    "name": "Padmesh",
    "emailid" : "padmeshkg@gmail.com",
    "subject": ["data science", 'sql', 'python']
}

list_of_records = [
    {'companyName': 'iNeuron',
     'product': 'Affordable AI',
     'courseOffered': 'Machine Learning with Deployment'},

    {'companyName': 'iNeuron',
     'product': 'Affordable AI',
     'courseOffered': 'Deep Learning for NLP and Computer vision'},

    {'companyName': 'iNeuron',
     'product': 'Master Program',
     'courseOffered': 'Data Science Masters Program'}
]


database  = client['myinfo']
collection = database['padmesh']
#collection.insert_one(data)
collection.insert_many(list_of_records)

