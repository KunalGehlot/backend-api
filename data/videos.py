import mongoengine

from mongoengine import DateTimeField, StringField


class Video(mongoengine.Document):
    title = StringField(required=True)
    videoId = StringField(required=True)
    description = StringField(required=True)
    publishedAt = DateTimeField(required=True)
    channelTitle = StringField(required=True)
    thumb = StringField(required=True)
    URL = StringField(required=True)

    meta = {"collection": "videos", "db_alias": "default"}
