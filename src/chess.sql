use chess_database

-- Creating the tables

create table player (
    player_id varchar(50) not null,
    username varchar(50) not null,
    title varchar(50),
    fist_name varchar(50) not null,
    last_name varchar(50),
    primary key (player_id)
);

create table player_elo (
    player_id varchar(50) not null,
    bullet int default 0,
    blitz int default 0,
    rapid int default 0,
    classical int default 0,
    primary key (player_id),
    foreign key (player_id) references player(player_id)
);

create table opening (
    op_id varchar(50) not null,
    op_name varchar(50) not null,
    move_set text not null,
    primary key (op_id)
);

create table moves (
    move_id varchar(50) not null,
    move_desc text not null,
    move_timestamps text not null,
    primary key (move_id)
);

create table game (
    game_id varchar(50) not null,
    game_date date not null,
    game_type varchar(50) not null,
    rated boolean not null,
    result char(3) not null,
    time_control varchar(50) not null,
    termination varchar(50) not null,
    op_id varchar(50) not null,
    move_id varchar(50) not null,
    primary key (game_id),
    foreign key (op_id) references opening(op_id),
    foreign key (move_id) references moves(move_id)
);

create table board (
    x smallint not null,
    y smallint not null,
    sqre varchar(50),
    primary key (x, y)
);

create table piece (
    piece_id varchar(50) not null,
    piece_name varchar(50) not null,
    piece_abbrv varchar(50) not null,
    primary key (piece_id)
);

create table participate (
    pid1 varchar(50) not null,
    pid2 varchar(50) not null,
    gid varchar(50) not null,
    primary key (pid1, pid2, gid),
    foreign key (pid1) references player(player_id),
    foreign key (pid2) references player(player_id),
    foreign key (gid) references game(game_id),
);

-- Inserting into the tables

insert into player values
('a9c3f817', 'jgourdy', null, 'james', 'smith'),
('9680d588', 'cheese', 'GM', 'alex', 'holmes'),
('4382df4d', 'ace', 'IM', 'bob', 'whales'),
('03273bbc', 'zdragon', 'GM', 'ramsundar', 'kiran'),
('2e5681b8', 'calcius', 'CM', 'lucidia', 'hales'),
('5b846587', 'destich', null, 'ivan', 'torento'),
('09e357bc', 'sdrag', 'IM', 'ravi', 'krishnan'),
('c529685f', 'katana', 'IM', 'mukesh', 'yadav'),
('c008d88b', 'franco', 'CM', 'abhi', 'kumar'),
('cf7732fa', 'timtom', null, 'aryan', 'johnson')

insert into player_elo values
('a9c3f817', 500, 240, 400, 0),
('9680d588', 2013, 1500, 1800, 1529),
('4382df4d', 1403, 800, 1200, 1100),
('03273bbc', 2206, 1201, 1943, 1219),
('2e5681b8', 1013, 891, 481, 838),
('5b846587', 200, 0, 310, 320),
('09e357bc', 2325, 1989, 1023, 1634),
('c529685f', 1429, 1132, 1420, 1656),
('c008d88b', 1123, 800, 1592, 1294),
('cf7732fa', 0, 250, 346, 563)
