-- Creating database

create database if not exists chess_database;
use chess_database;

-- Creating a user

create user if not exists 'chess_database_user'@localhost identified by 'chessmaster';

-- Granting all permissions

grant all on *.* to 'chess_database_user'@localhost;
