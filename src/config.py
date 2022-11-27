import streamlit as st
import pandas as pd
import datetime


def return_html_string(fen):
    html = f'''
    <script type="module" src="https://unpkg.com/chessboard-element/bundled/chessboard-element.bundled.js"></script>

    <chess-board
        draggable-pieces
        position={fen}>
    </chess-board>
    '''

    return html

def parse_game_moves(move_set):
    moves = move_set.split()
    white_moves = []
    black_moves = []
    n = len(moves)
    for m in range(0, n, 3):
        if m + 1 < n:
            white_moves.append(moves[m + 1])
        if m + 2 < n:
            black_moves.append(moves[m + 2])

    if len(white_moves) > len(black_moves):
        black_moves.append(' ')
    elif len(white_moves) < len(black_moves):
        white_moves.append(' ')
    else:
        pass
    
    df = pd.DataFrame(data={'white': white_moves, 'black': black_moves})
    df.index += 1
    return df

start = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"

host = 'localhost'
user = 'chess_database_user'
password = 'chessmaster'
database = 'chess_database'

tables = {
    'player': {
        'player_id': {
            'function': st.text_input,
            'key': 'player.player_id',
            'label': 'Player ID',
            'type': str
        },
        'username': {
            'function': st.text_input,
            'key': 'player.username',
            'label': 'Username',
            'type': str
        },
        'title': {
            'function': st.text_input,
            'key': 'player.title',
            'label': 'Title',
            'type': str
        },
        'first_name': {
            'function': st.text_input,
            'key': 'player.first_name',
            'label': 'First Name',
            'type': str
        },
        'last_name': {
            'function': st.text_input,
            'key': 'player.last_name',
            'label': 'Last Name',
            'type': str
        },
        'keys': [
            'player_id'
        ]
    },
    'player_elo': {
        'player_id': {
            'function': st.selectbox,
            'key': 'player_elo.player_id',
            'label': 'Player ID',
            'type': str,
            'references': 'player',
            'required': [
                'player.player_id',
                'player.username'
            ]
        },
        '_bullet': {
            'function': st.number_input,
            'key': 'player_elo._bullet',
            'label': 'Bullet ELO',
            'type': int
        },
        '_blitz': {
            'function': st.number_input,
            'key': 'player_elo._blitz',
            'label': 'Blitz ELO',
            'type': int
        },
        '_standard': {
            'function': st.number_input,
            'key': 'player_elo._standard',
            'label': 'Standard ELO',
            'type': int
        },
        'keys': [
            'player_id'
        ]
    },
    'opening': {
        'eco': {
            'function': st.selectbox,
            'key': 'opening.eco',
            'label': 'ECO Code',
            'type': str,
            'references': '',
            'required': [
                'opening.eco'
            ]
        },
        'op_name': {
            'function': st.text_input,
            'key': 'opening.op_name',
            'label': 'Opening Name',
            'type': str
        },
        'move_set': {
            'function': st.text_area,
            'key': 'opening.move_set',
            'label': 'Mainline Moves',
            'type': str
        },
        'keys': [
            'eco',
            'op_name',
            'move_set'
        ]
    },
    'game_moves': {
        'move_id': {
            'function': st.text_input,
            'key': 'game_moves.move_id',
            'label': 'Move ID',
            'type': str
        },
        'move_desc': {
            'function': st.text_area,
            'key': 'game_moves.move_desc',
            'label': 'Move Description / Set',
            'type': str
        },
        'move_timestamps': {
            'function': st.text_area,
            'key': 'game_moves.move_timestamps',
            'label': 'Move Timestamps',
            'type': str
        },
        'keys': [
            'move_id'
        ]
    },
    'game': {
        'game_id': {
            'function': st.text_input,
            'key': 'game_moves.game_id',
            'label': 'Game ID',
            'type': str
        },
        'game_date': {
            'function': st.date_input,
            'key': 'game_moves.game_date',
            'label': 'Date',
            'type': datetime.date
        },
        'game_type': {
            'function': st.radio,
            'key': 'game_moves.game_type',
            'label': 'Game Type',
            'type': str,
            'options': ['Standard', 'Bullet', 'Blitz']
        },
        'rated': {
            'function': st.radio,
            'key': 'game_moves.rated',
            'label': 'Rated',
            'type': bool,
            'options': [True, False]
        },
        'result': {
            'function': st.radio,
            'key': 'game_moves.result',
            'label': 'Result',
            'type': str,
            'options': ['1-0', '0-1', '1/2-1/2']
        },
        'time_control': {
            'function': st.text_input,
            'key': 'game_moves.time_control',
            'label': 'Time Control',
            'type': str
        },
        'termination': {
            'function': st.text_input,
            'key': 'game_moves.termination',
            'label': 'Termination',
            'type': str
        },
        'eco': {
            'function': st.selectbox,
            'key': 'game_moves.eco',
            'label': 'ECO Code',
            'type': str,
            'references': 'opening',
            'required': [
                'opening.eco',
                'opening.op_name',
                'opening.move_set'
            ]
        },
        'move_id': {
            'function': st.selectbox,
            'key': 'game_moves.move_id',
            'label': 'Move ID',
            'type': str,
            'references': 'game_moves',
            'required': [
                'game_moves.move_id',
                'game_moves.move_desc'
            ]
        },
        'keys': [
            'game_id'
        ]
    },
    'participate': {
        'pid1': {
            'function': st.selectbox,
            'key': 'participate.pid1',
            'label': 'Player 1',
            'type': str,
            'references': 'player',
            'required': [
                'player.player_id',
                'player.username'
            ]            
        },
        'pid2': {
            'function': st.selectbox,
            'key': 'participate.pid2',
            'label': 'Player 2',
            'type': str,
            'references': 'player',
            'required': [
                'player.player_id',
                'player.username'
            ]
        },
        'gid': {
            'function': st.selectbox,
            'key': 'participate.gid',
            'label': 'Game ID',
            'type': str,
            'references': 'game',
            'required': [
                'game.game_id'
            ]
        },
        'keys': [
            'pid1',
            'pid2',
            'gid'
        ]
    }
}
