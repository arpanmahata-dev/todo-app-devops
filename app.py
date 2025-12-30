from flask import Flask, render_template, request, redirect, jsonify
import json
import os

app = Flask(__name__)

DATA_FILE = 'todos.json'

def load_todos():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    return []

def save_todos(todos):
    with open(DATA_FILE, 'w') as f:
        json.dump(todos, f)

@app.route('/')
def index():
    todos = load_todos()
    return render_template('index.html', todos=todos)

@app.route('/add', methods=['POST'])
def add_todo():
    todos = load_todos()
    todo = {
        'id': len(todos) + 1,
        'task': request.form['task'],
        'completed': False
    }
    todos.append(todo)
    save_todos(todos)
    return redirect('/')

@app.route('/delete/<int:todo_id>')
def delete_todo(todo_id):
    todos = load_todos()
    todos = [t for t in todos if t['id'] != todo_id]
    save_todos(todos)
    return redirect('/')

@app.route('/health')
def health():
    return jsonify({'status': 'healthy'}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)