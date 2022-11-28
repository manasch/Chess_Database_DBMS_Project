-- Join 1, 2
-- Join tables game, moves, participate to get game details
select pid1, pid2, gid, game.move_id, move_desc
from participate
left join game on gid = game_id
join game_moves on game.move_id = game_moves.move_id;

-- Join 3
-- Getting the player and their elo ratings
select player.player_id, username, _bullet, _standard, _blitz
from player
natural join player_elo;

-- Join 4
-- Generating all the possible moves in chess
select r.x, r.y, r._square, o.x, o.y, o._square
from board as r cross join board as o
where r._square != o._square;

-- Aggregate 1
-- Finding the maximum blitz elo rating
select max(_blitz) as "max blitz"
from player_elo;

-- Aggregate 2
-- Finding the minimum standard elo rating
select min(_standard) as "min standard"
from player_elo;

-- Aggregate 3
-- Finding the average bullet elo rating
select avg(_standard) as "avg bullet"
from player_elo;

-- Aggregate 4
-- Finding the count of players with standard elo greater than 1500
select count(_standard) as "Standard gt 1500"
from player_elo
where _standard > 1500;

-- Set 1
-- Listing players with both bullet rating and standard rating above 1500
select player_id, username, _bullet, _standard from player natural join player_elo where _bullet > 1500
union
select player_id, username, _bullet, _standard from player natural join player_elo where _standard > 1500;

-- Set 2
-- Joining bishop and rook moves to get valid moves by queen
select * from moves_bishop
union all
select * from moves_rook;

-- Set 3
-- List players who have never played a game
select player_id as 'pid', username from player
except
(select pid1 as 'pid', username from participate natural join player union select pid2 as 'pid', username from participate natural join player);

-- Set 4
-- List players who have played atleast one game
select player_id as 'pid', username from player
intersect
(select pid1 as 'pid', username from participate natural join player union select pid2 as 'pid', username from participate natural join player);

-- Procedure 1
-- Set default elo to 600
delimiter $$
create procedure default_elo()
    begin
    update player_elo set _bullet = 600 where player_elo._bullet = 0;
    update player_elo set _blitz = 600 where player_elo._blitz = 0;
    update player_elo set _standard = 600 where player_elo._standard = 0;
    commit;
    end $$
delimiter ;

call default_elo;

-- Procedure 2
delimiter $$
create procedure player_play_count()
    begin
        drop table if exists temp_count;
        create table if not exists temp_count(username varchar(50), game_count int, player_id varchar(50));
        create or replace view play_count as
        (select pid1 as 'pid' from participate
        union all
        select pid2 as 'pid' from participate);
        insert into temp_count
        select username, count(*) as 'game_count', player_id
        from player join play_count on player.player_id = play_count.pid
        group by player.player_id
        having count(*) >= 2;
    end $$
delimiter ;

call player_play_count;

-- Function
-- Show the number of games won by a player
delimiter $$
create function count_wins(pid varchar(50))
returns int
deterministic
begin
    declare win_count, done int default 0;
    select count(*) from game inner join participate on game_id = gid where (pid1 = pid and result = "1-0") or (pid2 = pid and result = "0-1")
    into win_count;
    
    return win_count;
end $$
delimiter ;

select player_id, username, count_wins(player_id) as "# wins" from player;

-- Trigger
-- Check for elo on insert, should not cross 3000
delimiter $$
create trigger elo_check
before insert
on player_elo for each row
begin
    declare msg varchar(255);
    set msg = "ELO can't be above 3000";
    if new._standard >= 3000 or new._bullet >= 3000 or new._blitz >= 3000 then
        signal sqlstate '45000'
        set message_text = msg;
    end if;
end $$
delimiter ;

-- Cursor
-- Iterate through the player table and display full name

drop table if exists full_names;
create table if not exists full_names(
    full_name varchar(255)
);

delimiter $$
create procedure generate_fullname()
begin
    declare done int default 0;
    declare fn, ln varchar(50);
    declare cur cursor for select first_name, last_name from player;
    declare continue handler for not found set done = 1;
    open cur;
    label:
        loop
            fetch cur into fn, ln;
            if done = 1 then leave label;
            end if;
            insert into full_names values(concat(fn, ' ', ln));
        end loop;
    close cur;
end $$
delimiter ;

call generate_fullname;
