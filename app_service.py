import json
from db import Database

class AppService:

    def __init__(self, database: Database):
        self.database = database

    def create_task(self, task):
        self.database.create_task(task)
        return task

    def get_tasks(self):
        data = self.database.get_tasks()
        return data
    
    def get_task_ids(self):
        task_ids = self.database.get_task_ids()  # Asumiendo que tienes una función get_task_ids() en tu Database
        return task_ids
    
    def get_task_by_id(self, id):
        task_id = self.database.get_task_by_id(id)  
        return task_id


    def update_task(self, id, title, desc):
        self.database.update_task(id, title, desc)
        return id
    
    def change_status(self, id):
        task_id = self.database.change_status_task(id)  
        return task_id

    def delete_task(self, task_id):
        self.database.delete_task(task_id)
        return task_id

    def register_user(self, username, password):
        return self.database.create_user(username, password)
    
    def authenticate_user(self, username, password):
        user = self.database.get_user_by_username(username)
        if user and user[1] == password:
            return user
        return None

     
    def get_user_ids(self):
        # Lógica para obtener los IDs de usuario desde la base de datos
        # Supongamos que tienes un método en tu base de datos para obtener los IDs de usuario
        user_ids = self.database.get_user_ids()  # Implementa este método en tu clase Database
        return user_ids