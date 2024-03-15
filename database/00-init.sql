CREATE DATABASE tasks;

\c tasks;


CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  username VARCHAR(50) UNIQUE NOT NULL,
  password VARCHAR(100) NOT NULL
);

CREATE TABLE tasks (
  id SERIAL PRIMARY KEY,
  title VARCHAR(100) NOT NULL,
  description VARCHAR(255) NOT NULL,
  due_date DATE NOT NULL,
  status BOOLEAN NOT NULL,
  usuario_id INTEGER NOT NULL,
  FOREIGN KEY (usuario_id) REFERENCES users(id)
);
