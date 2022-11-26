import streamlit as st
from config import tables
from sql.functions import get_items_for_selectbox, get_items_by_primary_keys, update_table

def main():
    st.subheader('Update Entries')

    table_keys = tables.keys()
    selected_table = st.selectbox('**Tables**', table_keys)

    attr = tables[selected_table]
    attr_keys = list(attr.keys())
    new_select_values = []
    select_labels = []
    primary_keys = []

    # select primary keys
    for k in attr['keys']:
        options = get_items_for_selectbox(selected_table, [k])
        primary_keys.append(st.selectbox(k, options))
    
    primary_keys_res = get_items_by_primary_keys(selected_table, attr['keys'], primary_keys)
    if primary_keys_res:
        primary_keys_res = primary_keys_res[0]
    
    c1, c2 = st.columns(2)
    with c1:
        for v1 in range(len(attr['keys']), len(attr_keys) - 1, 2):
            col = attr[attr_keys[v1]]
            func = col['function']
            default_value = primary_keys_res[attr_keys[v1]]
            
            if func == st.radio:
                options = col['options']
                new_select_values.append(func(col['label'], options, index=options.index(default_value)))
                select_labels.append(attr_keys[v1])
            elif func == st.selectbox:
                references = col['references']
                res = get_items_for_selectbox(references if references else selected_table, col['required'])
                new_select_values.append(func(col['label'], res).split(' - ')[0])
                select_labels.append(attr_keys[v1])
            elif func == st.number_input:
                new_select_values.append(func(col['label'], step=1, min_value=0, value=default_value))
                select_labels.append(attr_keys[v1])
            else:
                new_select_values.append(func(col['label'], default_value))
                select_labels.append(attr_keys[v1])
    with c2:
        for v2 in range(len(attr['keys']) + 1, len(attr_keys) - 1, 2):
            col = attr[attr_keys[v2]]
            func = col['function']
            default_value = primary_keys_res[attr_keys[v2]]
            
            if func == st.radio:
                options = col['options']
                new_select_values.append(func(col['label'], options, index=options.index(default_value)))
                select_labels.append(attr_keys[v2])
            elif func == st.selectbox:
                references = col['references']
                res = get_items_for_selectbox(references if references else selected_table, col['required'])
                new_select_values.append(func(col['label'], res).split(' - ')[0])
                select_labels.append(attr_keys[v2])
            elif func == st.number_input:
                new_select_values.append(func(col['label'], step=1, min_value=0, value=default_value))
                select_labels.append(attr_keys[v2])
            else:
                new_select_values.append(func(col['label'], default_value))
                select_labels.append(attr_keys[v2])
    
    if st.button(f"Update {selected_table}"):
        try:
            update_table(selected_table, new_select_values, select_labels, attr['keys'], primary_keys)
            st.success(f"Successfully updated table {selected_table}")
        except Exception as e:
            st.warning(e)


if __name__ == "__main__":
    main()
