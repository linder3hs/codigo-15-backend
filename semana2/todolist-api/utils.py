from flask import jsonify


def search_task(tasks, task_id):
    result = None
    for task in tasks:
        if task['id'] == task_id:
            result = task

    return result


def response_success(data):
    return jsonify({
        "ok": True,
        "data": data
    })


def response_error(data):
    return jsonify({
        "data": data,
        "ok": False
    })
