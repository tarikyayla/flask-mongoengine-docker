import mongoengine,models,schemas,settings
from utils import date_from_string,add_set_dict_keys
from exceptions import ObjectNotFoundException
from datetime import datetime 

mongodb = mongoengine.connect(
    db=settings.DB["db"],
    host=settings.DB["host"],
    port=settings.DB["port"]
)



projectSchema = schemas.ProjectSchema()
taskSchema = schemas.TaskSchema()
commentSchema = schemas.CommentSchema()

# /projects

def list_all_projects():
    objects = projectSchema.dump(models.Project.objects(),many=True)
    return objects

def create_new_project(name):
    new_project = models.Project(name=name)
    new_project.save(validate=True)
    return projectSchema.dump(new_project)

# /projects/<projectId>

# GET
def get_project(id):
    try:
        obj = models.Project.objects.get(id=id)
    except:
        raise ObjectNotFoundException
    
    return projectSchema.dump(obj)

# POST
def create_new_task(projectId,post_data):
    new_task_object = taskSchema.load(post_data)
    new_task = models.Task(**new_task_object)
    new_task.save()
    project = models.Project.objects(id=projectId).update_one(push__tasks=new_task)
    return taskSchema.dump(new_task)

# DELETE
def delete_project(projectId):
    # Silinmesede olur, modele deleted(bool),deleteDate(date) 
    # alanları eklenip onlarda düzenlenebilirdi.
    models.Project.objects(id=projectId).delete()
# PUT 
def update_project(projectId,post_data):
    try:
        project = models.Project.objects.get(id=projectId)
    except:
        raise ObjectNotFoundException
    
    projectPostData = add_set_dict_keys(post_data)
    models.Project.objects(id=projectId).update(**projectPostData)
    return "OK"
    

# /projects/<projectId>/<taskId>

def create_comment(taskId,post_data):
    try:
        task = models.Task.objects(id=taskId)
    except:
        raise ObjectNotFoundException
    
    comment = commentSchema.load(post_data)
    comment_object = models.Comment(**comment)
    comment_object.save()
    task =  models.Task.objects(id=taskId).update_one(push__comments=comment_object)
    return commentSchema.dump(comment_object)

def get_task(taskId):

    try:
        task = models.Task.objects.get(id=taskId)
    except:
        raise ObjectNotFoundException
    
    return taskSchema.dump(task)


def delete_task(projectId,taskId):
    try:
        task = models.Task.objects.get(id=taskId)
    except:
        raise ObjectNotFoundException
    models.Project.objects(id=projectId).update_one(pull__tasks=task)
    task.delete()

def update_task(taskId,post_data):
    try:
        task = models.Task.objects.get(id=taskId)
    except:
        raise ObjectNotFoundException
    
    if "plannedStartDate" in post_data:
        post_data["startDateNotified"] = False
    
    if "plannedEndDate" in post_data:
        post_data["endDateNotified"] = False
    
    if "status" in post_data:
        if post_data["status"] == 1:
            post_data["startDate"] = datetime.now()
        if post_data["status"] == 2:
            post_data["endDate"] = datetime.now()


    post_data["changeDate"] = datetime.now()
    taskPostData = add_set_dict_keys(post_data)

    models.Task.objects(id=taskId).update(**taskPostData)
    return taskSchema.dump(models.Task.objects.get(id=taskId))

# /projects/<projectId>/<taskId>/<commentId>

def get_comment(commentId):
    try:
        comment = models.Comment.objects.get(id=commentId)
    except:
        raise ObjectNotFoundException

    return commentSchema.dump(comment)

def delete_comment(taskId,commentId):
    try:
        comment = models.Comment.objects.get(id=commentId)
        task = models.Task.objects.get(id=taskId)
    except:
        raise ObjectNotFoundException

    models.Task.objects(id=taskId).update_one(pull__comments=comment)
    comment.delete()

def update_comment(commentId,post_data):
    try:
        comment = models.Comment.objects.get(id=commentId)
    except:
        raise ObjectNotFoundException
    
    commentPostData = add_set_dict_keys(post_data)
    models.Comment.objects(id=commentId).update(**commentPostData)
    return "OK"




def check_tasks():
    # Başlangıç tarihi girdiği halde, başlanmamış taskler için
    startReminder = [task for task in models.Task.objects(plannedStartDate__ne=None,startDateNotified__ne=True,status='0')]
    endReminder = [task for task in models.Task.objects(plannedEndDate__ne=None,endDateNotified__ne=True,status='1')]
    for task in startReminder:
        if task.plannedStartDate > datetime.now():
            send_mail(task) # send_mail, tabi sıkıntı olmaması için async yapılması gerekiyor.
            models.Task.objects(id=task.id).update_one(startDateNotified=True)
    
    for task in endReminder:
        if task.plannedEndDate > datetime.now():
            send_mail(task)
            models.Task.objects(id=task.id).update_one(endDateNotified=True)

    return [obj.to_json() for obj in startReminder + endReminder]
    
        



def send_mail(task):
    print("Mail gönderildi")
        
