-- Show_privileges_for user_0d_1
SELECT *
FROM mysql.user
WHERE User = 'user_0d_1'
  AND Host = 'localhost';

-- Show_privileges_for user_0d_2
SELECT *
FROM mysql.user
WHERE User = 'user_0d_2'
  AND Host = 'localhost';
