from app import app
from fake_data.tasks import tasks_list

@app.route('/')
def index():
    first_name = 'Kadeeja'
    last_name = 'Griffin'
    age = 27
    return 'Hello World'

#POST ENDPOINTS

#Get all tasks
@app.route('/tasks')
def get_tasks():
    tasks = tasks_list
    return tasks

# Get single post by ID
@app.route('/tasks/<int:task_id>')
def get_task(task_id):
    tasks = tasks_list
    for task in tasks:
        if task['id'] == task_id:
            return task 
    return {'error': f'Task with an ID of {task_id} does not exist'}, 404