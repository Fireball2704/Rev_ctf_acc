CREATE DATABASE ctf_db;
USE ctf_db;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL
);

INSERT INTO users (first_name, last_name) VALUES
('Bruce', 'Wayne'),
('Harvey', 'Dent'),
('Selina', 'Kyle'),
('Pamela', 'Isley'),
('Oswald', 'Cobblepot'),
('Edward', 'Nigma'),
('Jonathan', 'Crane'),
('Harleen', 'Quinzel'),
('acc_ctf', '{h@rd_w0rk_p@ys}'),
('Barbara', 'Gordon'),
('Dick', 'Grayson'),
('Jason', 'Todd'),
('Tim', 'Drake'),
('Damian', 'Wayne'),
('Cassandra', 'Cain'),
('Stephanie', 'Brown'),
('Kate', 'Kane');