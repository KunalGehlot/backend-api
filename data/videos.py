import mongoengine

from mongoengine import DateTimeField, StringField


class Video(mongoengine.Document):
    """Video model"""

    title = StringField(required=True)
    videoId = StringField(required=True)
    description = StringField(required=False)
    publishedAt = DateTimeField(required=True)
    channelTitle = StringField(required=True)
    thumb = StringField(required=False)
    URL = StringField(required=False)

    meta = {
        "collection": "videos",
        "db_alias": "default",
        "indexes": [
            {
                "fields": ["$title", "$description"],
                "default_language": "english",
                "weights": {"title": 10, "description": 5},
                "cls": False,
            }
        ],
    }
