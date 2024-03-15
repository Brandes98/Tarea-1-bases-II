# TC01
# Despliegue de Aplicaciones con Docker y PostgreSQL

# Funcionalidades
# 3.2.1 Crear Tarea
Ruta: http://localhost:5002/tasks
Método: POST
Envia: JSON con toda la información de la tarea para añadir en la base de datos
Recibe: Lista con toda la información de la tarea

# 3.2.2 Listar Tareas
Ruta: http://localhost:5002/tasks
Método: GET
Envia: Nada
Recibe: lista de las tareas

# 3.2.3 Obtener Detalle de Tareas
Ruta: http://localhost:5002/tasks/id
Método: GET
Envia: Nada
Recibe: lista con información de la tarea

# 3.2.4 Actualizar Tarea
Ruta: http://localhost:5002/tasks/id
Método: PUT
Envia: JSON con toda la información de la tarea para actualizar en la base de datos (menos id)
Recibe: lista con información actualizada de la tarea

# 3.2.5 Eliminar Tarea
Ruta: http://localhost:5002/tasks/id
Método: PUT
Envia: nada
Recibe: id de la tarea eliminada

# Commandos 
## Montar RestAPI
``` bash
docker-compose -f docker-compose.yml up --build
```

# JSON Formato
{
    "title": "Task New",
    "description": "Task Description New",
    "due_date": "2021-12-31",
    "status": 0,
    "usuario_id": 1
} 