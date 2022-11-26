import streamlit as st
from config import tables
from sql.functions import get_items_for_selectbox

def main():
    st.subheader("Add Entries")
    
    table_keys = tables.keys()
    selected_table = st.selectbox('**Tables**', table_keys)

    attr = tables[selected_table]
    attr_keys = list(attr.keys())

    # insert keys
    for k in attr['keys']:
        func = attr[k]['function']
        if func == st.selectbox:
            references = attr[k]['references']
            res = get_items_for_selectbox(references if references else selected_table, attr[k]['required'])
            func(attr[k]['label'], res)
        else:
            func(attr[k]['label'])

    # insert other values
    c1, c2 = st.columns(2)
    with c1:
        for v1 in range(len(attr['keys']), len(attr_keys) - 1, 2):
            col = attr[attr_keys[v1]]
            func = col['function']
            
            if func == st.radio:
                options = col['options']
                func(col['label'], options)
            elif func == st.selectbox:
                references = col['references']
                res = get_items_for_selectbox(references if references else selected_table, col['required'])
                func(col['label'], res)
            elif func == st.number_input:
                func(col['label'], step=1, min_value=0)
            else:
                func(col['label'])
    with c2:
        for v2 in range(len(attr['keys']) + 1, len(attr_keys) - 1, 2):
            col = attr[attr_keys[v2]]
            func = col['function']
            
            if func == st.radio:
                options = col['options']
                func(col['label'], options)
            elif func == st.selectbox:
                references = col['references']
                res = get_items_for_selectbox(references if references else selected_table, col['required'])
                func(col['label'], res)
            elif func == st.number_input:
                func(col['label'], step=1, min_value=0)
            else:
                func(col['label'])


if __name__ == "__main__":
    main()
