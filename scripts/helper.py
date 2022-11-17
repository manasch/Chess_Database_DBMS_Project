import re
from pathlib import Path

def extract_from_moves(game_moves):
    # clock_pattern = r"({.*?\[%clk.*?\].*?})"

    # Searches for the time pattern
    clock_pattern = r"(\d:\d{2}:\d{2})"
    clocks = re.findall(clock_pattern, game_moves)

    # Replaces the time pattern with an empty string to give only the set of moves played
    moves_pattern = r"{.*?\[%clk.*?\].*?} "
    moves = re.subn(moves_pattern, '', game_moves)

    # returns the clocktimes, moves and result
    return (" ".join(clocks), moves[0][:-4], moves[0][-4:])

def generate_games(n):
    # Just prints the games from the lichess database
    # A new game every 18 lines
    current_dir = Path.cwd().resolve()

    res = []
    with open(current_dir.parent / "db" / "games.pgn") as g:
        for _ in range(n):
            temp = []
            for _k in range(18):
                temp.append(g.readline().strip())
            res.append(temp)
    return res
