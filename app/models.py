import mongoengine as ma
from datetime import datetime




class Project(ma.Document):
    name = ma.StringField(required=True)
    status = ma.IntField(default=0,max=1)
    createDate = ma.DateTimeField(default=datetime.utcnow)
    tasks = ma.ListField(ma.ReferenceField('Task'))


class Task(ma.Document):
    title = ma.StringField(required=True)
    content = ma.StringField()
    status = ma.IntField(min_value=0,max_value=4,default=0)
    plannedStartDate = ma.DateTimeField()
    plannedEndDate = ma.DateTimeField()
    createDate = ma.DateTimeField(default=datetime.utcnow)
    startDate = ma.DateTimeField()
    endDate = ma.DateTimeField()
    changeDate = ma.DateTimeField()
    comments = ma.ListField(ma.ReferenceField('Comment'))



class Comment(ma.Document):
    content = ma.StringField()
    createDate = ma.DateTimeField(default=datetime.utcnow)
