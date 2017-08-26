class Review:
    # asin,亚马逊对产品的唯一编码，reviewerId，用户Id，reviewerName用户名，reviewTime评论时间unix时间挫
    # reviewText评论内容，作为主题情感分析的文本基础，helpful是否有帮助是个模糊值，summary，overall总体打分
    # Sentiment情感值
    sentiment=None
    def __init__(self, asin='', reviewerId='', reviewerName='',
                 reviewTime='', reviewText='', helpful='',
                 summary='', overall='', sentiment=None,unixReviewTime=0):
        self.asin = asin
        self.reviewerId = reviewerId
        self.reviewerName = reviewerName
        self.reviewTime = reviewTime
        self.reviewText = reviewText
        self.helpful = helpful
        self.summary = summary
        self.overall = overall
        self.sentiment = sentiment
        self.unixReviewTime = unixReviewTime
        self.keywords = []
        self.sentiment = sentiment

    def set_sentiment(self, sentiment):
        self.sentiment = sentiment

    def add_keyword(self, keyword):
        self.keywords.append(keyword)

#emotion set [sadness,joy,fear,disgust,anger] value from 0,1
#sentiment  (-1, 1)
class Keyword:
    def __init__(self, keyword='', sentiment=None, relevance=None, emotion=[]):
        self.keyword = keyword
        self.sentiment = sentiment
        self.relevance = relevance
        self.emotion = emotion
