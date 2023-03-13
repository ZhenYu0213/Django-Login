-- Alter user 'dbuser'@'%' IDENTIFIED WITH mysql_native_password BY 'password';
-- GRANT ALL PRIVILEGES ON myproject.* TO 'dbuser'@'%';
-- FLUSH PRIVILEGES;

CREATE TABLE if not exists equipmentsManager.user (
  id INT NOT NULL AUTO_INCREMENT,
  account VARCHAR(12) NOT NULL,
  password VARCHAR(12) NOT NULL,
  email VARCHAR(50) NOT NULL,
  PRIMARY KEY (id));
CREATE TABLE if not exists equipmentsManager.equipment (
  id INT NOT NULL AUTO_INCREMENT,
  owner VARCHAR(50) NULL,
  status VARCHAR(50) NULL,
  PRIMARY KEY (id));