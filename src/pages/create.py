import streamlit as st
import pandas as pd
from config import tables
from sql.functions import get_items_for_selectbox, insert_into_table, get_all_from_table

def main():
    st.subheader("Add Entries")
    
    table_keys = tables.keys()
    selected_table = st.selectbox('**Tables**', table_keys)

    attr = tables[selected_table]
    attr_keys = list(attr.keys())
    select_values = []
    select_labels = []

    # insert keys
    for k in attr['keys']:
        func = attr[k]['function']
        if func == st.selectbox:
            references = attr[k]['references']
            res = get_items_for_selectbox(references if references else selected_table, attr[k]['required'])
            select_values.append(func(attr[k]['label'], res).split(' - ')[0])
            select_labels.append(k)
        else:
            select_values.append(func(attr[k]['label']))
            select_labels.append(k)

    # insert other values
    c1, c2 = st.columns(2)
    with c1:
        for v1 in range(len(attr['keys']), len(attr_keys) - 1, 2):
            col = attr[attr_keys[v1]]
            func = col['function']
            
            if func == st.radio:
                options = col['options']
                select_values.append(func(col['label'], options))
                select_labels.append(attr_keys[v1])
            elif func == st.selectbox:
                references = col['references']
                res = get_items_for_selectbox(references if references else selected_table, col['required'])
                select_values.append(func(col['label'], res).split(' - ')[0])
                select_labels.append(attr_keys[v1])
            elif func == st.number_input:
                select_values.append(func(col['label'], step=1, min_value=0))
                select_labels.append(attr_keys[v1])
            else:
                select_values.append(func(col['label']))
                select_labels.append(attr_keys[v1])
    with c2:
        for v2 in range(len(attr['keys']) + 1, len(attr_keys) - 1, 2):
            col = attr[attr_keys[v2]]
            func = col['function']
            
            if func == st.radio:
                options = col['options']
                select_values.append(func(col['label'], options))
                select_labels.append(attr_keys[v2])
            elif func == st.selectbox:
                references = col['references']
                res = get_items_for_selectbox(references if references else selected_table, col['required'])
                select_values.append(func(col['label'], res).split(' - ')[0])
                select_labels.append(attr_keys[v2])
            elif func == st.number_input:
                select_values.append(func(col['label'], step=1, min_value=0))
                select_labels.append(attr_keys[v2])
            else:
                select_values.append(func(col['label']))
                select_labels.append(attr_keys[v2])

    if st.button(f"Add new {selected_table} entry"):
        try:
            insert_into_table(selected_table, select_values, select_labels)
            st.success(f"Successfully added new entry to {selected_table}")

            new_df = pd.DataFrame(get_all_from_table(selected_table))
            new_df.index += 1

            with st.expander(f"Table **{selected_table}** After Insertion"):
                st.dataframe(new_df, use_container_width=True)
        except Exception as e:
            st.warning(e)


if __name__ == "__main__":
    main()
