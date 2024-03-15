import psycopg2


class Database:
    def __init__(
        self, database="db_name", host="db_host", user="db_user", password="db_pass", port="db_port"
    ):
        self.conn = psycopg2.connect(
            database=database, host=host, user=user, password=password, port=port
        )

    def create_task(self, task_json):
        cursor = self.conn.cursor()
        cursor.execute(
            f"INSERT INTO tasks (title, description, due_date, status, usuario_id) VALUES ('{task_json['title']}', '{task_json['description']}', '{task_json['due_date']}', '{task_json['status']}', '{task_json['usuario_id']}');"
        )
        self.conn.commit()
        cursor.close()
        return task_json

    def get_tasks(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT id, title, description, due_date, status, usuario_id FROM tasks;")
        data = cursor.fetchall()
        cursor.close()
        return data
    
    def get_task_by_id(self, id):
        cursor = self.conn.cursor()
        cursor.execute(f"SELECT id, title, description, due_date, status, usuario_id FROM tasks WHERE id = {id};")
        data = cursor.fetchall()
        cursor.close()
        return data
    
    
    
    def change_status_task(self, id):
        cursor = self.conn.cursor()
        cursor.execute(f"SELECT status FROM tasks WHERE id = {id};")
        data = cursor.fetchall()
        status = str(data[0]) #esto da el str con una coma
        FinalStatus = status.replace(",", "").replace("(", "").replace(")", "")
        NewStatus = True if FinalStatus == "False" else False
        cursor.close()
        cursor2 = self.conn.cursor()
        cursor2.execute(f"UPDATE tasks SET status = {NewStatus} WHERE id = {id};")
        self.conn.commit()
        cursor2.close()
        return NewStatus    

    def update_task(self, id, title, desc):
        cursor = self.conn.cursor()
        cursor.execute(
            f"UPDATE tasks SET title = '{title}', description = '{desc}' WHERE id = {id};"
        )
        self.conn.commit()
        cursor.close()
        return id

    def delete_task(self, id):
        cursor = self.conn.cursor()
        cursor.execute(f"DELETE FROM tasks WHERE id = {id};")
        self.conn.commit()
        cursor.close()
        return id
    
    def create_user(self, username, password):
        try:
            cursor = self.conn.cursor()
            cursor.execute(
                "INSERT INTO users (username, password) VALUES (%s, %s);",
                (username, password)
            )
            self.conn.commit()
            cursor.close()
            return username
        except psycopg2.Error as e:
            print("Error al crear usuario:", e)
            self.conn.rollback()
            raise

    def get_user_by_username(self, username):
        try:
            cursor = self.conn.cursor()
            cursor.execute(
                "SELECT username, password FROM users WHERE username = %s;",
                (username,)
            )
            user = cursor.fetchone()
            cursor.close()
            return user
        except psycopg2.Error as e:
            print("Error al obtener usuario por nombre de usuario:", e)
            raise
    def get_user_ids(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT id FROM users;")
        user_ids = [row[0] for row in cursor.fetchall()]
        cursor.close()
        return user_ids
    
    def get_task_ids(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT id FROM tasks;")
        task_ids = [row[0] for row in cursor.fetchall()]
        cursor.close()
        return task_ids

    


