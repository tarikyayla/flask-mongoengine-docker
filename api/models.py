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
    status = ma.IntField(min_value=0,max_value=3,default=0)
    # 0 Initial 1 Started 2 Completed 3 Archived
    plannedStartDate = ma.DateTimeField()
    plannedEndDate = ma.DateTimeField()
    startDateNotified = ma.BooleanField(default=False)
    endDateNotified = ma.BooleanField(default=False)
    createDate = ma.DateTimeField(default=datetime.utcnow)
    startDate = ma.DateTimeField()
    endDate = ma.DateTimeField()
    changeDate = ma.DateTimeField()
    comments = ma.ListField(ma.ReferenceField('Comment'))



class Comment(ma.Document):
    content = ma.StringField()
    createDate = ma.DateTimeField(default=datetime.utcnow)
