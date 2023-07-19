-- Create the table unique_id if it doesn't already exist
CREATE TABLE IF NOT EXISTS unique_id (
  id INT DEFAULT 1,
  UNIQUE (id),
  name VARCHAR(256)
);
