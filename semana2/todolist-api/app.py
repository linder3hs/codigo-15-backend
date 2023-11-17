from flask import Flask, jsonify, request
from datetime import date
from utils import search_task

# instancia de Flaks
app = Flask(__name__)

tasks = [
    {
        "id": 1,
        "title": "Limpiar mi cuarto",
        "category": "Hogar",
        "priority": "Alto",
        "created_at": "2023-11-16"
    }
]


@app.route("/")
def hola_mundo():
    return jsonify({
        "message": "Hola mundo"
    })


@app.route("/tasks")
def get_tasks():
    return jsonify({
        "ok": True,
        "data": tasks
    })


@app.route("/tasks/<int:task_id>")
def get_task(task_id):
    result = search_task(tasks, task_id)
    if result is None:
        return jsonify({
            "ok": False,
            "data": "Task not found"
        })

    return jsonify({
        "ok": True,
        "data": result
    })


@app.route("/tasks", methods=["POST"])
def add_task():
    task = request.json
    task["id"] = len(tasks) + 1
    task["created_at"] = date.today()
    tasks.append(task)
    return jsonify({
        "ok": True,
        "data": "Tarea creada correctamente"
    }), 201


@app.route("/tasks/<int:task_id>", methods=["PUT"])
def update_task(task_id):
    task = search_task(tasks, task_id)

    if task is None:
        return jsonify({
            "ok": False,
            "data": "Task not found"
        })

    new_task = request.json
    task["title"] = new_task.get("title", task["title"])
    task["category"] = new_task.get("category", task["category"])
    task["priority"] = new_task.get("priority", task["priority"])

    return jsonify({
        "ok": True,
        "data": "Tarea actualizada correctamente"
    })


if __name__ == "__main__":
    app.run(debug=True)
