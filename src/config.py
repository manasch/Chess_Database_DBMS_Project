host = "localhost"
user = "chess_database_user"
password = "chessmaster"
database = "chess_database"

tables = {
    "player": ["player_id", "username", "title", "first_name", "last_name"],
    "player_elo": ["player_id", "_bullet", "_blitz", "_standard"],
    "opening": ["eco", "op_name", "move_set"],
    "game_moves": ["move_id", "move_desc", "move_timestamps"],
    "game": ["game_id", "game_date", "game_type", "rated", "result", "time_control", "termination", "eco", "move_id"],
    "participate": ["pid1", "pid2", "gid"],
    "piece": ["piece_abbrv", "piece_name", "color"],
    "board": ["x", "y", "_square"],
}
