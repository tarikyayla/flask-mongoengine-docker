import requests
import json 


API_URL = "https://localhost:5000/projects/"

header ={"Content-Type":"application/json"}

projects = []
tasks = []
comments = [] 

def test_create_new_project_response_201():
	request_object = {
	'name' : "IQ Vizyon Test Projesi"
	}

	response = requests.post(API_URL,json=request_object,headers=header,verify=False)
	assert response.status_code == 201
	projects.append(response.json())

def test_update_project_response_200():

	request_object = {
		'name' : "IQ Vizyon Test Projesi Updated",
		'status' : 4
	}
	url = API_URL + projects[0]["id"]
	response = requests.put(url ,json=request_object,headers=header,verify=False)

	assert response.status_code == 200
	assert str(response.text) == "OK"

def test_get_project_200_and_check_updated_values():
	url = API_URL + projects[0]["id"]
	response = requests.get(url,verify=False)

	assert response.status_code == 200
	assert response.json()["status"] == 4
	assert response.json()["name"] == "IQ Vizyon Test Projesi Updated"


def test_add_task_response_201():
	url = API_URL + projects[0]["id"]
	request_object = {
		"title" :  "database design",
		"content" : "diagram.io kullanılarak yapılacak",
		"plannedStartDate" : "02-07-2020 20:00",
		"plannedEndDate" : "02-07-2020 20:20"
	}
	response = requests.post(url,json=request_object,headers=header,verify=False)
	assert response.status_code == 201
	tasks.append(response.json())

def test_get_task_response_200():
	url = API_URL + projects[0]["id"] +"/" + tasks[0]["id"]
	response = requests.get(url,verify=False)
	assert response.status_code == 200


def test_get_all_projects_response_200_and_check_if_task_added():
	response = requests.get(API_URL + projects[0]["id"],verify=False)
	assert response.status_code == 200
	projects[0] = response.json()
	assert projects[0]["tasks"][0] == tasks[0]


def test_update_task_200_and_values():
	url = API_URL + projects[0]["id"] + "/" + tasks[0]["id"]
	request_object = {
		"content" : "updated task content",
		"status" : 2
	}
	response = requests.put(url,json=request_object,headers=header,verify=False)
	assert response.status_code == 200
	assert response.json()["content"] == request_object["content"]
	assert response.json()["status"] == request_object["status"]
	assert response.json()["changeDate"] != tasks[0]["changeDate"]

def test_add_comment_response_201():
	url = API_URL + projects[0]["id"] + "/" + tasks[0]["id"]
	request_object = {
    	"content" : "Tasarıma burdan ulaşılabilir : link"
	}
	response = requests.post(url,json=request_object,headers=header,verify=False)
	assert response.status_code == 201
	comments.append(response.json())

def test_update_comment_response_200():
	url = API_URL + projects[0]["id"] + "/" + tasks[0]["id"] +"/" + comments[0]["id"]
	request_object = {
		"content" : "UPDATED, tasarım notları"
	}
	response = requests.put(url,json=request_object,headers=header,verify=False)
	assert response.status_code == 200
	assert response.text == "OK"

def test_get_comment_and_validate_changed_values():
	url = API_URL + projects[0]["id"] + "/" + tasks[0]["id"] +"/" + comments[0]["id"]
	response = requests.get(url,verify=False)

	assert response.status_code == 200
	assert comments[0]["content"] != response.json()["content"]
	comments[0] = response.json()


def test_delete_comment_response_200():
	url = API_URL + projects[0]["id"] + "/" + tasks[0]["id"] +"/" + comments[0]["id"]
	response = requests.delete(url,verify=False)
	assert response.status_code == 200
	assert response.text == "OK"

# def test_delete_task_response_200():
# 	url = API_URL + projects[0]["id"] + "/" + tasks[0]["id"]
# 	response = requests.delete(url,verify=False)
# 	assert response.status_code == 200
# 	assert response.text == "OK"

# def test_delete_project_200():
# 	url = API_URL + projects[0]["id"]
# 	response = requests.delete(url,verify=False)
# 	assert response.status_code == 200
# 	assert response.text == "OK"



# TODO
# TEST DELETE TASKS