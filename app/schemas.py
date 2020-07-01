import models
from marshmallow import fields, Schema
from settings import APP
# serializer 

# Örnek olması için bu şekilde bırakıyorum
# Bütün verilerin görünmemesini istiyorsanız farklı şemalar üretebilirsiniz

class CommentSchema(Schema):
    id = fields.Str()
    content = fields.Str()
    createDate = fields.Date()
    
    class Meta:
        dateformat = APP["dateformat"]

class TaskSchema(Schema):
    id = fields.Str()
    title = fields.Str(required=True)
    content = fields.Str()
    status = fields.Int()
    plannedStartDate = fields.Date()
    plannedEndDate = fields.Date()
    createDate = fields.Date()
    startDate = fields.Date()
    endDate = fields.Date()
    changeDate = fields.Date()
    comments = fields.Nested(CommentSchema,many=True)

    class Meta:
        dateformat = APP["dateformat"]


class ProjectSchema(Schema):
    id = fields.Str()
    name = fields.Str()
    createDate = fields.Date()
    tasks = fields.Nested(TaskSchema,many=True)    
    status =  fields.Int()

    class Meta:
        dateformat = APP["dateformat"]
