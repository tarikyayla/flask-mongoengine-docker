class ObjectNotFoundException(Exception):
    def __init__(self):
        self.message = "Object not found"
        self.statusCode = 404