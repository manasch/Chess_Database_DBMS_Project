import io

import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import chess, chess.pgn

from config import tables, return_html_string, start
from sql.functions import get_all_from_table

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
        move_set = "1. e4 e5 2. Nf3 Nf6 3. d4 exd4 4. e5 Nd5 5. Nxd4 c5 6. Nf3 Nb6 7. Bd3 d5 8. O-O Be7 9. Bb5+ Bd7 10. Bxd7+ N8xd7 11. Re1 O-O 12. Bf4 Nc4 13. b3 Qc7 14. bxc4 Bf6 15. exf6 Qxf4 16. fxg7 Kxg7 17. Qxd5 Qf6 18. Nbd2 Rad8 19. Ne4 Qg6 20. Ne5 Nxe5 21. Qxe5+ f6 22. Qxc5 Rfe8 23. Nd6 Rxe1+ 24. Rxe1 Qxc2 25. Qc7+ Kg6 26. Qxd8 Qc3 27. Qg8+ Kh6 28. Nf7+ Kh5 29. g4+ Kh4 30. Qxh7+ Kxg4 31. Re4+ Kf3 32. Qf5#"
        pgn = io.StringIO(move_set)
        game = chess.pgn.read_game(pgn)

        board = game.board()
        mainline_moves = game.mainline_moves()
        counter = 0

        col1, col2 = st.columns(2)
        st.write(mainline_moves.start)

        if st.button("Next"):
            board.push(mainline_moves[counter])
            counter += 1

        if st.button("Prev"):
            board.pop()
            counter -= 1

        with col1:
            components.html(return_html_string(board.fen()), height=350, width=350)
        
        with col2:
            st.write("test")
        # pgn = 

        # pgn = io.StringIO(pgn)
        # game = chess.pgn.read_game(pgn)

        # board = game.board()
        # st.write(game.turn)

        # for move in game.mainline_moves():
        #     board.push(move)
        #     print(board.fen())

    

if __name__ == "__main__":
    main()
