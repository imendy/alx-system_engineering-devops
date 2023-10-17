# MySQL Replication Setup

The MySQL server provides a robust database management system with querying and connectivity capabilities, enabling excellent data structure and integration with various platforms.

## Needed Knowledge

- What is a primary-replica cluster
- MySQL primary replica setup
- Build a robust database backup strategy
- `mysqldump`

## Learning Objectives

- Understand the main role of a database
- Know what a database replica is and its purpose
- Understand the need to store database backups in different physical locations
- Regularly perform operations to ensure the effectiveness of the database backup strategy

## Project Requirements

- Allowed editors: `vi`, `vim`, `emacs`
- Files interpreted on Ubuntu 16.04 LTS
- Files should end with a new line
- A `README.md` file at the root of the project folder is mandatory
- Bash script files must be executable
- Bash scripts must pass Shellcheck without any error
- The first line of Bash scripts should be exactly `#!/usr/bin/env bash`
- The second line of all your Bash scripts should be a comment explaining what is the script doing

## Installation Guide for MySQL 5.7.*

1. Go to [dev.mysql.com](https://dev.mysql.com/) and copy the PGP PUBLIC KEY just immediately under the Notice section to your clipboard.

2. Create a new file in your terminal with a `.key` extension and paste the PGP PUB KEY copied to the clipboard.

3. Execute the following commands in your terminal:

```bash
sudo apt-key add name_of_file.key

# Adding MySQL to the apt repo
sudo sh -c 'echo "deb http://repo.mysql.com/apt/ubuntu bionic mysql-5.7" >> /etc/apt/sources.list.d/mysql.list'

# Updating the apt repo
sudo apt-get update

# Now check your available versions
sudo apt-cache policy mysql-server

# Now installing MySQL 5.7.*
sudo apt-get install -f mysql-client=5.7* mysql-community-server=5.7* mysql-server=5.7* -y

## Project Task

## Creating a User and Granting Privileges in MySQL

```bash

mysql -uroot -p
# Type root password

mysql> CREATE USER 'holberton_user'@'localhost' IDENTIFIED BY 'projectcorrection280hbtn';

mysql> GRANT GRANT REPLICATION CLIENT ON *.* TO 'holberton_user'@'localhost';

mysql> FLUSH PRIVILEGES;
Creating Database, Tables, and Adding Data

```bash

mysql> CREATE DATABASE db_name_;

## Verify if the database is created
mysql> SHOW DATABASES;

mysql> USE db_name;

mysql> CREATE TABLE table_name (
    -> col_1 data_type,
    -> col_2 data_type);

## Continue adding more columns as needed

mysql> INSERT INTO table_name VALUES (val_1, val_2);

## Verify if data was added successfully
mysql> SELECT col_1, col_2 FROM tb_name;
Setting Up MySQL Replication
Create replication user and grant replication privilege:

```bash
mysql> CREATE USER 'replica_user'@'%' IDENTIFIED BY 'replica_user_pwd';

mysql> GRANT REPLICATION SLAVE ON *.* TO 'replica_user'@'%';

mysql> FLUSH PRIVILEGES;

## To verify
mysql> SELECT user, Repl_slave_priv FROM mysql.user;

mysql> exit
Update /etc/mysql/mysql.conf.d/mysqld.cnf:

```bash
# By default we only accept connections from localhost
# bind-address = 127.0.0.1
server-id = 1
log_bin = /var/log/mysql/mysql-bin.log
binlog_do_db = db_name
Enable incoming connection to port 3306 and restart mysql-server:

```bash
sudo ufw allow from 'replica_server_ip' to any port 3306

sudo service mysql restart
Log back into the mysql-server to lock the database and prepare binary file for replication:

```bash
mysql -uroot -p

mysql> FLUSH TABLES WITH READ LOCK;

mysql> SHOW MASTER STATUS;

# Note down the binary log and the position.

# 5. Export the database from the mysql-server to the local machine:

```bash
mysqldump -uroot -p db_name > export_db_name.sql

scp -i _identity_file_ export_db_name.sql user@machine_ip:location
SSH to the replica machine's IP address to import the tables to the replica mysql-server:

```bash
mysql -uroot -p

mysql> CREATE DATABASE db_name;

mysql> exit

mysql -uroot p db_name < export_db_name.sql

# Now edit the config file in /etc/mysql/mysql.conf.d/mysqld.cnf and then reload mysql-server

```bash
server-id = 2
log_bin = /var/log/mysql/mysql-bin.log
binlog_do_db = db_name_from_master_mysql-server
relay_log = /var/log/mysql/mysql-relay-bin.log

sudo service mysql restart
Login to MySQL Server in Replica to Configure Replication

```bash
mysql -uroot -p
password:

mysql>
mysql> CHANGE MASTER TO
    -> MASTER_HOST='source_host_name',
    -> MASTER_USER='replication_user_name',
    -> MASTER_PASSWORD='replication_password',
    -> MASTER_LOG_FILE='recorded_log_file_name',
    -> MASTER_LOG_POS=recorded_log_position;

-- Then you start slave
mysql> START SLAVE;
