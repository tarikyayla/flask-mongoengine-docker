from datetime import datetime 

def date_from_string(date_string):
    date_format = "%d-%m-Y %H:%M"
    return datetime.strptime(date_string,date_format)


def add_set_dict_keys(obj):
    return dict(("set__" + key,value) for key,value in obj.items())
