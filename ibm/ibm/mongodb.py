from pymongo import MongoClient
import ibm.ibm.review as review

conn = MongoClient('localhost', 27017)
db = conn.amazondb  #连接mydb数据库，没有则自动创建
reviews_set1 = db.reviews_set1 #使用test_set集合，没有则自动创建


# natural language understanding
def nlu(s):
    keyword = review.Keyword('key1', 0.964)
    rv = review.Review(asin=s.get('asin')
                       , reviewerId=s.get('reviewerId')
                       , summary=s.get('summary')
                       , reviewerName=s.get('reviewerName')
                       , reviewText=s.get('reviewText')
                       , helpful=s.get('helpful')
                       , overall=s.get('overall')
                       , unixReviewTime=s.get('unixReviewTime')
                       , reviewTime=s.get('reviewTime')
                       )
    rv.add_keyword(keyword)
    return rv


m = map(nlu, reviews_set1.find())

for rev in list(m):
    print(rev.asin)
