import json
from pymongo import MongoClient


conn = MongoClient('localhost', 27017)
db = conn.amazondb  #连接mydb数据库，没有则自动创建
reviews_set1 = db.reviews_set1 #使用test_set1集合，没有则自动创建


def convert(path):
    f = open(path, 'r')
    return f.readlines()


def insert_record(line):
    js = json.dumps(eval(line))
    #print(js)
    reviews_set1.insert(json.loads(js))
    return js

for line in convert("../resources/Cell_Phones_and_Accessories_5.json"):
    insert_record(line)

# not working map(insert_record, convert("../resources/Cell_Phones_and_Accessories_5.json"))
conn.close()
