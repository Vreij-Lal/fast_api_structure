INSERT INTO users (username, email, is_active)
VALUES (:username, :email, :is_active)
RETURNING id, username, email, is_active;
