import streamlit as st
import datetime

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
        }
    },
    'player_elo': {
        'player_id': {
            'function': st.selectbox,
            'key': 'player_elo.player_id',
            'label': 'Player ID',
            'type': str
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
        }
    },
    'opening': {
        'eco': {
            'function': st.selectbox,
            'key': 'opening.eco',
            'label': 'ECO Code',
            'type': str
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
        }
    },
    'game_moves': {
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
            'function': st.text_input,
            'key': 'game_moves.game_type',
            'label': 'Game Type',
            'type': str
        },
        'rated': {
            'function': st.radio,
            'key': 'game_moves.rated',
            'label': 'Rated',
            'type': bool
        },
        'result': {
            'function': st.radio,
            'key': 'game_moves.result',
            'label': 'Result',
            'type': str
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
            'type': str
        },
        'move_id': {
            'function': st.selectbox,
            'key': 'game_moves.move_id',
            'label': 'Move ID',
            'type': str
        }
    },
    'participate': {
        'pid1': {
            'function': st.selectbox,
            'key': 'participate.pid1',
            'label': 'Player 1',
            'type': str
        },
        'pid2': {
            'function': st.selectbox,
            'key': 'participate.pid2',
            'label': 'Player 2',
            'type': str
        },
        'gid': {
            'function': st.selectbox,
            'key': 'participate.gid',
            'label': 'Game ID',
            'type': str
        }
    }
}
