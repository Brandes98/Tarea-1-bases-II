\c tasks;

INSERT INTO users (username, password) 
VALUES 
  ('a', 'a');
  
INSERT INTO tasks (title, description, due_date, status, usuario_id) 
VALUES 
  ('Task 1', 'Description 1', '2021-12-31', TRUE, 1), 
  ('Task 2', 'Description 2', '2021-12-03', TRUE, 1),
  ('Task 3', 'Description 3', '2021-12-01', FALSE, 1),
  ('Task 4', 'Description 4', '2021-12-12', TRUE, 1),
  ('Task 5', 'Description 5', '2021-12-29', FALSE, 1),
  ('Task 6', 'Description 6', '2021-12-28', TRUE, 1),
  ('Task 7', 'Description 7', '2021-12-23', TRUE, 1),
  ('Task 8', 'Description 8', '2021-12-13', FALSE, 1),
  ('Task 9', 'Description 9', '2021-12-12', TRUE, 1),
  ('Task 11', 'Description 10', '2021-12-10', FALSE, 1);

