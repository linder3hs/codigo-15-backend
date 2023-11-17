def search_task(tasks, task_id):
    result = None
    for task in tasks:
        if task['id'] == task_id:
            result = task

    return result