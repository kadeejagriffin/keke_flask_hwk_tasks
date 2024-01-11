from flask import request
from datetime import datetime
from app import app
from fake_data.tasks import tasks_list

users = []

@app.route('/')
def index():
    first_name = 'Kadeeja'
    last_name = 'Griffin'
    age = 27
    return 'Hello World'

# USER ENDPOINTS

# Create New User
@app.route('/users', methods=['POST'])
def create_user():
    #Check to see that the requset body is JSON
    if not request.is_json:
        return {'error': 'Your contetnt-type must be application/json'}, 400

    # Get that data from teh request body
    data = request.json

    # validate that the data has all of the required fields
    required_fields = ['id', 'title', 'description', 'completed', 'createdAt', 'dueDate']
    missing_fields = []
    for field in required_fields:
        if field not in data:
            missing_fields.append(field)
    if missing_fields:
        return {'error': f"{', '.join(missing_fields)} must be in the request body"}, 400

    # Get the values from the data    
    id = data.get('id')
    title = data.get('title')
    description = data.get('description')
    completed = data.get('completed')
    createdAt = data.get('createdAt')
    dueDate = data.get('dueDate')
    
    # Create a new user dict and append ot users list
#POST ENDPOINTS

#Get all tasks
@app.route('/tasks')
def get_tasks():
    tasks = tasks_list
    return tasks

# Get single task by ID
@app.route('/tasks/<int:task_id>')
def get_task(task_id):
    tasks = tasks_list
    for task in tasks:
        if task['id'] == task_id:
            return task 
    return {'error': f'Task with an ID of {task_id} does not exist'}, 404

# Create new Task route 
@app.route('/tasks', methods=['POST'])
def create_task():
    if not request.is_json:
    # Check to see if the request body is JSON
        return{'error': 'Your content-type must be application/json'}, 400
    # Get the data from the request
    data = request.json
    # Validate the incoming data
    required_fields = ['title', 'description']
    missing_fields = []
    for field in required_fields:
        if field not in data:
            missing_fields.append(field)
        if missing_fields:
            return {'error': f"{', '.join(missing_fields)} must be in the request body"}, 400
    # Get values from the request data
    title = data.get('title')
    description = data.get('description')
    due_date = data.get('dueDate')
    
    #Create a new task with data
    new_task = {
        "id": len(tasks_list) + 1,
        "title": title,
        "description": description,
        "completed": False,
        "createdAt": datetime.utcnow(),
        "dueDate": due_date
    }
    # Add the new task to the list of tasks
    tasks_list.append(new_task)
    return new_task, 201