#encoding: utf-8
from scrapy import Field, Item

class MovieItem(Item):
    subject_id = Field()
    name = Field()
    year = Field()
    directors = Field()
    actors = Field()
    languages = Field()
    genres = Field() #类型
    runtime = Field()
    stars = Field() #5星 4星 3星 2星 1星各个数量, 次序为：5 4 3 2 1
    channel = Field()
    average = Field() #平均分
    vote = Field() #评分人数
    tags = Field()
    watched = Field() #看过
    wish = Field() #想看
    comment = Field() #短评数
    question = Field() #提问数
    review = Field() #影评数
    discussion = Field() #讨论
    image = Field() #图片数
    countries = Field() #制片国家
    summary = Field()

class GroupItem(Item):
    pass

class DongxiItem(Item):
    pass

class BookItem(Item):
    pass