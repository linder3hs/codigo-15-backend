from flask import jsonify


def search_task(tasks, task_id):
    result = None
    for task in tasks:
        if task['id'] == task_id:
            result = task

    return result


def response_success(data, status=200):
    return jsonify({
        "ok": True,
        "data": data
    }), status


def response_error(data, status=500):
    return jsonify({
        "data": data,
        "ok": False
    }), status
