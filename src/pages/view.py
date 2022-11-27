import io

import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import chess, chess.pgn

from config import tables, return_html_string, start, parse_game_moves
from sql.functions import get_all_from_table, get_choices_for_game_selectbox, game_joins

def main():
    tab1, tab2 = st.tabs(["View Tables", "Visualize a Game"])
    with tab1:
        st.subheader("View Entries")

        table_keys = tables.keys()
        selected_table = st.selectbox('**Tables**', table_keys)
        data = get_all_from_table(selected_table)

        df = pd.DataFrame(data)
        df.index += 1
        st.dataframe(df, use_container_width=True)

    with tab2:
        st.subheader("Game")
        
        game_data = game_joins()
        game_choices, ids = get_choices_for_game_selectbox()
        selected_game = st.selectbox("Select Game", game_choices)
        selected_game_index = ids.index(ids[game_choices.index(selected_game)])

        move_set = game_data[selected_game_index]['move_desc']

        pgn = io.StringIO(move_set)
        game = chess.pgn.read_game(pgn)
        board = game.board()

        game_fen = []

        for move in game.mainline_moves():
            board.push(move)
            game_fen.append(board.fen())
        
        if 'counter' not in st.session_state:
            st.session_state.counter = -1

        c1, c2, c3 = st.columns(3)
        with c1:
            prev_button = st.button("Prev")
            if prev_button:
                st.session_state.counter -= 1

        with c2:
            next_button = st.button("Next")
            if next_button:
                st.session_state.counter += 1

        with c3:
            reset_button = st.button("Reset")
            if reset_button:
                st.session_state.counter = -1
        
        st.write(f"Move {(st.session_state.counter // 2) + 1 if st.session_state.counter != -1 else 'Start'}")
        col1, col2 = st.columns([3, 2])
        with col1:
            if st.session_state.counter >= 0:
                components.html(return_html_string(game_fen[st.session_state.counter]), height=400, width=400)
            else:
                components.html(return_html_string(start), height=400, width=400)
        
        with col2:
            game_df = parse_game_moves(move_set)
            st.dataframe(game_df, use_container_width=True)
        

if __name__ == "__main__":
    main()
