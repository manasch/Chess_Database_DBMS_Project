import streamlit as st
import pandas as pd

from config import tables
from sql.functions import get_all_from_table, delete_from_table, get_items_for_selectbox

def main():
    st.subheader("Delete Entries")

    table_keys = tables.keys()
    selected_table = st.selectbox('**Tables**', table_keys)
    attr = tables[selected_table]
    selected_values = []

    data = get_all_from_table(selected_table)

    df = pd.DataFrame(data)
    df.index += 1

    with st.expander(f"Table **{selected_table}** Before Deletion"):
        st.dataframe(df, use_container_width=True)
    
    for k in attr['keys']:
        options = get_items_for_selectbox(selected_table, [k])
        selected_values.append(st.selectbox(k, options))

    if st.button("Delete Entry"):
        try:
            delete_from_table(selected_table, selected_values, attr['keys'])
            st.success(f"Successfully deleted entry from {selected_table}")

            new_df = pd.DataFrame(get_all_from_table(selected_table))
            new_df.index += 1
            
            with st.expander(f"Table **{selected_table}** After Deletion"):
                st.dataframe(new_df, use_container_width=True)
        except Exception as e:
            st.warning(e)

if __name__ == "__main__":
    main()
