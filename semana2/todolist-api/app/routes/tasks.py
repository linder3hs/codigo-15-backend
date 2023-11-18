from flask import Blueprint, request
from datetime import date
from utils import search_task, response_success, response_error

task_route = Blueprint('task_route', __name__)

tasks = [
    {
        "id": 1,
        "title": "Limpiar mi cuarto",
        "category": "Hogar",
        "priority": "Alto",
        "created_at": "2023-11-16"
    }
]


@task_route.route("/tasks")
def get_tasks():
    return response_success(tasks)


@task_route.route("/tasks/<int:task_id>")
def get_task(task_id):
    result = search_task(tasks, task_id)
    if result is None:
        return response_error("Task not found")

    return response_success(result)


@task_route.route("/tasks", methods=["POST"])
def add_task():
    task = request.json
    task["id"] = len(tasks) + 1
    task["created_at"] = date.today()
    tasks.append(task)
    return response_success("Tarea creada correctamente", 201)


@task_route.route("/tasks/<int:task_id>", methods=["PUT"])
def update_task(task_id):
    task = search_task(tasks, task_id)

    if task is None:
        return response_error("Task not found")

    new_task = request.json
    task["title"] = new_task.get("title", task["title"])
    task["category"] = new_task.get("category", task["category"])
    task["priority"] = new_task.get("priority", task["priority"])

    return response_success("Tarea actualizada correctamente")


@task_route.route("/tasks/<int:task_id>", methods=['DELETE'])
def delete_task(task_id):
    task = search_task(tasks, task_id)
    if task is None:
        return response_error("Task not found")

    tasks.remove(task)
    return response_success("Task deleted")
