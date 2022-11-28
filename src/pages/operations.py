import streamlit as st
import pandas as pd
from sql.functions import query_execute, get_all_from_table

def main():
    tab1, tab2, tab3 = st.tabs(["Procedure", "Function", "Cursor"])
    with tab1:
        st.subheader("Procedure Call")
        with st.expander("Player ELO"):
            df = pd.DataFrame(get_all_from_table("player_elo"))
            df.index += 1
            st.dataframe(df, use_container_width=True)
        
        if st.button("Execute Procedure"):
            query = "call default_elo;"
            try:
                query_execute(query)
            except Exception as e:
                st.warning(e)
            finally:
                st.info("Executed")
                new_df = pd.DataFrame(get_all_from_table("player_elo"))
                new_df.index += 1
                st.dataframe(new_df, use_container_width=True)
        
        st.subheader("Players who played games >= 2")
        if st.button("Game Count"):
            try:
                query_execute("call player_play_count;")
                res = query_execute("select * from temp_count;")
            except Exception as e:
                st.warning(e)
            finally:
                st.info("Executed")
                df = pd.DataFrame(res)
                df.index += 1
                st.dataframe(df, use_container_width=True)

    with tab2:
        st.subheader("Function Call")
        if st.button("Win Count"):
            try:
                res = query_execute("select player_id, username, count_wins(player_id) as \"# wins\" from player;")
            except Exception as e:
                st.warning(e)
            finally:
                st.info("Executed")
                df = pd.DataFrame(res)
                df.index += 1
                st.dataframe(df, use_container_width=True)
    with tab3:
        st.subheader("Cursor Call")
        if st.button("Display Fullnames"):
            try:
                query_execute("call generate_fullname;")
                res = query_execute("select * from full_names;")
            except Exception as e:
                st.warning(e)
            finally:
                st.info("Executed")
                df = pd.DataFrame(res)
                df.index += 1
                st.dataframe(df, use_container_width=True)


if __name__ == "__main__":
    main()
