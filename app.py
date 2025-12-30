from flask import Flask, render_template, request, redirect, jsonify
import json
import os
from datetime import datetime

app = Flask(__name__)

DATA_FILE = 'todos.json'

def load_todos():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    return []

def save_todos(todos):
    with open(DATA_FILE, 'w') as f:
        json.dump(todos, f, indent=2)

@app.route('/')
def index():
    todos = load_todos()
    # Separate completed and pending tasks
    pending = [t for t in todos if not t['completed']]
    completed = [t for t in todos if t['completed']]
    return render_template('index.html', pending=pending, completed=completed, total=len(todos))

@app.route('/add', methods=['POST'])
def add_todo():
    todos = load_todos()
    task = request.form['task'].strip()
    priority = request.form.get('priority', 'medium')
    
  #  if task:
        todo = {
            'id': max([t['id'] for t in todos], default=0) + 1,
            'task': task,
            'completed': False,
            'priority': priority,
            'created_at': datetime.now().strftime('%Y-%m-%d %H:%M')
        }
        todos.append(todo)
        save_todos(todos)
    return redirect('/')

@app.route('/toggle/<int:todo_id>')
def toggle_todo(todo_id):
    todos = load_todos()
    for todo in todos:
        if todo['id'] == todo_id:
            todo['completed'] = not todo['completed']
            if todo['completed']:
                todo['completed_at'] = datetime.now().strftime('%Y-%m-%d %H:%M')
            else:
                todo.pop('completed_at', None)
            break
    save_todos(todos)
    return redirect('/')

@app.route('/delete/<int:todo_id>')
def delete_todo(todo_id):
    todos = load_todos()
    todos = [t for t in todos if t['id'] != todo_id]
    save_todos(todos)
    return redirect('/')

@app.route('/edit/<int:todo_id>', methods=['POST'])
def edit_todo(todo_id):
    todos = load_todos()
    new_task = request.form['task'].strip()
    new_priority = request.form.get('priority', 'medium')
    
    for todo in todos:
        if todo['id'] == todo_id:
            todo['task'] = new_task
            todo['priority'] = new_priority
            break
    save_todos(todos)
    return redirect('/')

@app.route('/clear-completed')
def clear_completed():
    todos = load_todos()
    todos = [t for t in todos if not t['completed']]
    save_todos(todos)
    return redirect('/')

@app.route('/health')
def health():
    return jsonify({'status': 'healthy'}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)