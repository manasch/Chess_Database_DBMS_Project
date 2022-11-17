import uuid
from helper import extract_from_moves, generate_games

opening = []
moves = []
game = []

n = int(input("Enter games: "))

games = generate_games(n)

for i in range(n):
    l = games[i]
    p = extract_from_moves(l[-2])
    t = str(uuid.uuid4())[:8]
    u = l[11][6:-2]
    moves.append((t, p[1], p[0]))
    if "standard" in l[0].lower():
        game.append((str(uuid.uuid4())[:8], l[5][10:-2], 1, "Standard", p[-1][1:], l[13][14:-2], l[14][14:-2], u, t))
    elif "blitz" in l[0].lower():
        game.append((str(uuid.uuid4())[:8], l[5][10:-2], 1, "Blitz", p[-1][1:], l[13][14:-2], l[14][14:-2], u, t))
    elif "bullet" in l[0].lower():
        game.append((str(uuid.uuid4())[:8], l[5][10:-2], 1, "Bullet", p[-1][1:], l[13][14:-2], l[14][14:-2], u, t))
    else:
        pass

game_query = "insert into game values\n"
moves_query = "insert into moves values\n"
for i in range(n):
    if i < n - 1:
        game_query += f"('{game[i][0]}', '{game[i][1]}', '{game[i][3]}', '{game[i][2]}', '{game[i][4]}', '{game[i][5]}', '{game[i][6]}', '{game[i][7]}', '{game[i][8]}'),\n"
        moves_query += f"('{moves[i][0]}', '{moves[i][1]}', '{moves[i][2]}'),\n"
    else:
        game_query += f"('{game[i][0]}', '{game[i][1]}', '{game[i][3]}', '{game[i][2]}', '{game[i][4]}', '{game[i][5]}', '{game[i][6]}', '{game[i][7]}', '{game[i][8]}');\n"
        moves_query += f"('{moves[i][0]}', '{moves[i][1]}', '{moves[i][2]}');\n"


with open('test.sql', 'w') as f:
    f.write(moves_query)
    f.write("\n")
    f.write(game_query)
