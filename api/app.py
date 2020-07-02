from flask import Flask,request,jsonify,redirect
import functions
from exceptions import ObjectNotFoundException
from settings import app 




@app.route("/projects",methods=['GET','POST'])
def projects():
	if request.method == 'GET':
		return jsonify(functions.list_all_projects()),200
	else:
		return functions.create_new_project(request.json['name']),201

@app.route("/projects/<projectId>",methods=['GET','POST','PUT','DELETE'])
def get_project(projectId):
	try:
		if request.method == 'GET':
			return functions.get_project(projectId),200
		elif request.method == 'POST':
			return functions.create_new_task(projectId,request.json),201
		elif request.method == "PUT":
			return functions.update_project(projectId,request.json),200
		else:
			functions.delete_project(projectId)
			return "OK",200
	except ObjectNotFoundException as exception:
		return exception.message,exception.statusCode
	except Exception as ex:
		return str(ex),500



@app.route("/projects/<projectId>/<taskId>",methods=['GET','POST','PUT','DELETE'])
def get_tasks(projectId,taskId):
	try:
		if request.method == 'GET':
			return functions.get_task(taskId),200
		elif request.method == 'POST':
			return functions.create_comment(taskId,request.json),201
		elif request.method == "PUT":
			return functions.update_task(taskId,request.json),200
		else:
			functions.delete_task(projectId,taskId)
			return "OK",200
	except ObjectNotFoundException as exception:
		return exception.message,exception.statusCode
	except Exception as ex:
		return str(ex),500


@app.route("/projects/<projectId>/<taskId>/<commentId>",methods=['GET','DELETE','PUT'])
def get_comment(projectId,taskId,commentId):
	try:
		if request.method == 'GET':
			return functions.get_comment(commentId),200
		elif request.method == 'DELETE':
			functions.delete_comment(taskId,commentId)
			return "OK",200
		else:
			return functions.update_comment(commentId,request.json),200
	except ObjectNotFoundException as NFException:
		return NFException.message,404
	except Exception as ex:
		return str(ex),500


@app.route("/task-reminder",methods=["GET"])
def task_reminder():
	try:
		return jsonify(functions.check_tasks()),200
	except Exception as ex:
		return str(ex),500




if __name__ == "__main__":
	app.run(host='0.0.0.0',debug=True,ssl_context='adhoc')