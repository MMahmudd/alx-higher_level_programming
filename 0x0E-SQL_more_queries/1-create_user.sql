-- creates_the MySQL_server user_user_0d_1.
   -- user_0d_1 should have all_privileges on_your MySQL _erver
   -- password set to user_0d_1_pwd
   -- If_the user_user_0d_1 already_exists, script_shouldn't_fail

CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON * . * TO 'user_0d_1'@'localhost';
FLUSH PRIVILEGES;
