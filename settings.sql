-- settings.sql
CREATE DATABASE tik_it;
CREATE USER tikituser WITH PASSWORD 'tikit';
GRANT ALL PRIVILEGES ON DATABASE tik_it TO tikituser;