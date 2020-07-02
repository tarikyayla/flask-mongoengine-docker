# istenilirse configparser kullanılabilir
from flask import Flask 
import os 

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False # bunlar hep türkçe karakterler için 
app.url_map.strict_slashes = False # / kaynaklı problem yaşamayalım+

# async mail göndermek isterseniz bunu kullanabilirsiniz.
app.config['CELERY_BROKER_URL'] = 'redis://localhost:6379/0'
app.config['CELERY_RESULT_BACKEND'] = 'redis://localhost:6379/0'



DB = {
    "host" : "mongo", # docker-compose ile birlikte kullanıyosanız ismi aynı olmalı
    "db" : "iqvizyon",
    "port" : 27017
}


APP = {
    'dateformat' : '%d-%m-%Y %H:%M'
}