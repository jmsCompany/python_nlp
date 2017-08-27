from pymongo import MongoClient
import ibm.ibm.review as review
from watson_developer_cloud import NaturalLanguageUnderstandingV1
import watson_developer_cloud.natural_language_understanding.features.v1 as \
    Features
import json


natural_language_understanding = NaturalLanguageUnderstandingV1(
    version='2017-02-27',
    username='9b62acbd-73fb-4c20-8105-b1767a224b1c',
    password='t6BS8FkVNdkf')


def analyze(s):
    response = natural_language_understanding.analyze(
    text=s,
    features=[
        Features.Keywords(
            emotion=True,
            sentiment=True,
            limit=2
        ),
        Features.Sentiment()])
    return response


conn = MongoClient('localhost', 27017)
db = conn.amazondb  #连接mydb数据库，没有则自动创建
reviews_set1 = db.reviews_set1 #使用test_set集合，没有则自动创建
reviews_set3 = db.reviews_set3


# natural language understanding
# def nlu(s):
#     rv = review.Review(asin=s.get('asin')
#                        , reviewerId=s.get('reviewerId')
#                        , summary=s.get('summary')
#                        , reviewerName=s.get('reviewerName')
#                        , reviewText=s.get('reviewText')
#                        , helpful=s.get('helpful')
#                        , overall=s.get('overall')
#                        , unixReviewTime=s.get('unixReviewTime')
#                        , reviewTime=s.get('reviewTime')
#                        )
#     reviewText = s.get('reviewText')
#     res = analyze(reviewText)
#     #print(json.dumps(res, indent=2))
#     sentiment = res.get('sentiment').get('document').get('score')
#     rv.set_sentiment(sentiment)
#     for keyword in res.get('keywords'):
#         em = keyword.get('emotion')
#         kw = review.Keyword(keyword=keyword.get('text')
#                             , sentiment=keyword.get('sentiment').get('score')
#                             , relevance= keyword.get('relevance')
#                             , emotion = em.values())
#         rv.add_keyword(kw)
#     return rv


# natural language understanding
def nlu1(s):
    reviewText = s.get('reviewText')
    res = analyze(reviewText)
    sentiment = res.get('sentiment').get('document').get('score')
    s['sentiment'] = sentiment
    s['keywords'] = []
    for keyword in res.get('keywords'):
        kw = {}
        em = keyword.get('emotion')
        kw['keyword'] = keyword.get('text')
        kw['sentiment'] = keyword.get('sentiment').get('score')
        kw['relevance'] = keyword.get('relevance')
        kw['emotion'] = list(em.values())
        s['keywords'].append(kw)

    return s



m = map(nlu1, reviews_set1.find({"reviewerID":"A1NHB2VC68YQNM"}))

# for rev in list(m):
#     print('sentiment: %s '%(rev.sentiment))
#     for k in rev.keywords:
#         print('keyword: %s, relevance: %f,  sentiment: %f, emotion: %s '
#               %(k.keyword,k.relevance, k.sentiment, list(k.emotion)))

for rev in list(m):
    #js = json.dumps(review.Review(), default=lambda obj: obj.__dict__)
    # print(rev)
    reviews_set3.insert(rev)

conn.close()