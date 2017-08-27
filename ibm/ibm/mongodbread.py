from pymongo import MongoClient
import ibm.ibm.review as review

conn = MongoClient('localhost', 27017)
db = conn.amazondb  #连接mydb数据库，没有则自动创建

reviews_set3 = db.reviews_set3 #使用test_set集合，没有则自动创建
for v in reviews_set3.find():
    print(v)
