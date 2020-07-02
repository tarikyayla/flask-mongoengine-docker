# Flask-RestApi-Celery-Redis
*Python 3.6 ve daha üzeri sürümleri destekler*
### Ayarlar 
Celery için zaman ayarı : [/celery-tasks/task.py](/celery-tasks/task.py)
Api ayarları :[/api/settings.py](/api/settings.py)

### Test 
```bash
pip install requests 
pip install pytest
pytest tests/test.py
```

### Çalıştırma
 Sisteminizde dockerın kurulu olduğunu varsayıyorum.
  
 docker-compose Docker Desktop ile birlikte geliyor ancak windows olmayan bir sistemde kullanacaksanız ve docker-compose komutunu çalıştıramıyosanız, `apt-get install docker-compose` ile yükleyebilirsiniz


```bash
docker-compose up --build 
```






### Linkler
Api Default :  https://localhost:5000
Flower Dashboard: http://localhost:5555


## API Requests & Responses

### GET /projects : Proje listesi 
**Response**
```json
[
  {
    "createDate": "02-07-2020 15:30", 
    "id": "5efdfd7e0e20cc0b962ed858", 
    "name": "IQ Vizyon Test Projesi Updated", 
    "status": 1, 
    "tasks": [
      {
        "changeDate": "02-07-2020 15:30", 
        "comments": [
          {
            "content": "UPDATED, tasarım notları", 
            "createDate": "02-07-2020 15:30", 
            "id": "5efdfd7e0e20cc0b962ed85a"
          }
        ], 
        "content": "updated task content", 
        "createDate": "02-07-2020 15:30", 
        "endDate": null, 
        "endDateNotified": false, 
        "id": "5efdfd7e0e20cc0b962ed859", 
        "plannedEndDate": "02-07-2020 00:00", 
        "plannedStartDate": "02-07-2020 00:00", 
        "startDate": null, 
        "startDateNotified": false, 
        "status": 0, 
        "title": "database design"
      }
    ]
  }
]

```
### POST /projects : Yeni proje
**Request**
 
```json
{
	"name" : "project name"
}
```
**Response** : 201 
 
```json
  {
    "createDate": "02-07-2020 15:30", 
    "id": "5efdfd7e0e20cc0b962ed858", 
    "name": "project name", 
    "status": 0, 
    "tasks": []
  }
```
### GET /projects/*projectId*

**Response** : 200 
```json
  {
    "createDate": "02-07-2020 15:30", 
    "id": "5efdfd7e0e20cc0b962ed858", 
    "name": "project name", 
    "status": 0, 
    "tasks": []
  }
  ```

### PUT /projects/projectId
**Request** 
```json
 {
    "name": "project name updated", 
    "status": 2, 
  }
```
**Response** OK, 200 
### DELETE /projects/*projectId*
**Response** OK,200

### POST /projects/*projectId* : New Task 
**Request**
```json
{
	"title" :  "database design",
	"content" : "diagram.io kullanılarak yapılacak",
	"plannedStartDate" : "02-07-2020 20:00",
	"plannedEndDate" : "02-07-2020 20:20"
}
```

**Response** 201

```json
{
  "changeDate": "02-07-2020 15:30", 
  "comments": [], 
  "content": "updated task content", 
  "createDate": "02-07-2020 15:30", 
  "endDate": null, 
  "endDateNotified": false, 
  "id": "5efdfd7e0e20cc0b962ed859", 
  "plannedEndDate": "02-07-2020 00:00", 
  "plannedStartDate": "02-07-2020 00:00", 
  "startDate": null, 
  "startDateNotified": false, 
  "status": 0, 
  "title": "database design"
}
```

#### Geri kalanı için testleri veya api.txt dosyasını inceleyebilirsiniz.
