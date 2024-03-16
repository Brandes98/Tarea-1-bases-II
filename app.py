import os
from flask import Flask, request, render_template, session, redirect, url_for
from flask import jsonify
from app_service import AppService
from db import Database

DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")

db = Database(database=DB_NAME, host=DB_HOST, user=DB_USER, password=DB_PASSWORD, port=DB_PORT)

app = Flask(__name__)
app.secret_key = 'your_secret_key' 

appService = AppService(db)

@app.route("/")
def home():
    return render_template("home.html")


@app.route("/user_ids")
def get_user_ids():
    user_ids = appService.get_user_ids()  
    return jsonify(user_ids)


@app.route("/main_page")
def main_page():
    return render_template("main_page.html")


@app.route("/main_menu")
def main_menu():
    return render_template("main_menu.html")


@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = appService.authenticate_user(username, password)
        if user:
            session['username'] = username
            return redirect(url_for('main_menu'))
        else:
            return 'Credenciales inválidas. <a href="/login">Intentar de nuevo</a>'
    return render_template("login.html")


@app.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        success = appService.register_user(username, password)
        if success:
            return redirect(url_for('login'))
        else:
            return 'El nombre de usuario ya está en uso. <a href="/register">Intentar de nuevo</a>'
    return render_template("register.html")


@app.route("/tasks", methods=["POST"])
def create_task():
    request_data = request.get_json()
    if 'usuario_id' in request_data:
        usuario_id = request_data['usuario_id']
        return appService.create_task(request_data)
    else:
        return "Error: El usuario_id no está especificado en los datos de la tarea", 400  


@app.route("/tasks")
def tasks():
    tasks_data = appService.get_tasks()  
    return render_template("tasks.html", tasks=tasks_data)


@app.route("/task_details")
def task_details():
    return render_template("task_details.html", task_id=id)


@app.route("/tasks_details/<int:id>")
def detailOfTask(id):
    tasks = appService.get_task_by_id(id)
    return render_template("detailOfTask.html", tasks=tasks)


@app.route("/task_ids")
def get_task_ids():
    task_ids = appService.get_task_ids() 
    return jsonify(task_ids)


@app.route("/tasks-changed/<int:id>", methods=['GET', 'PUT'])
def changed_status_task(id):
    appService.change_status(id)
    return redirect(url_for('tasks'))


@app.route("/tasks-update/<int:id>")
def view_update_task(id):
    tasks = appService.get_task_by_id(id)
    return render_template("update.html", tasks=tasks)


@app.route("/tasks-update-done/<int:id>", methods=['GET','POST'])
def update_task(id):
    if request.method == 'GET':
        newTitle = request.args.get('newTitle')
        newDesc = request.args.get('newDesc')

        appService.update_task(id, newTitle, newDesc)

        return redirect(url_for('tasks'))

@app.route('/tasks-delete/<int:id>', methods=['GET', 'DELETE'])
def delete_task(id):
    appService.delete_task(str(id))
    return redirect(url_for('tasks'))

if __name__ == '__main__':
    app.run(debug=True)

