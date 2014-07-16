#encoding: utf-8
from misc.store import doubanDB


class MoviePipeline(object):
    def process_item(self, item, spider):
        if spider.name != "movie":  return item
        if item.get("subject_id", None) is None: return item

        spec = { "subject_id": item["subject_id"] }
        doubanDB.movie.update(spec, {'$set': dict(item)}, upsert=True)

        return None


class MovieReviewPipeline(object):
    def process_item(self, item, spider):
        if spider.name != "movie_review": return item
        
        return None


class GroupPipeline(object):
    def process_item(self, item, spider):
        if spider.name != "group": return item

        return None


class BookPipeline(object):
    def process_item(self, item, spider):
        if spider.name != "book": return item

        return None

class DongxiPipeline(object):
    def process_item(self, item, spider):
        if spider.name != "dongxi": return item

        return None        