import mysql.connector
import config
import streamlit as st

chessDB = mysql.connector.connect(
    host=config.host,
    user=config.user,
    password=config.password,
    database=config.database
)

cur = chessDB.cursor(
    buffered=True,
    dictionary=True
)

def query_execute(query):
    cur.execute(query)
    return cur.fetchall()

def get_items_for_selectbox(referenced, required):
    query = "select distinct "
    for i, req in enumerate(required, 1):
        if i != len(required):
            query += f'{req.split(".")[-1]}, '
        else:
            query += f'{req.split(".")[-1]} '
    
    query += f"from {referenced};"
    query_result = query_execute(query)

    result = []
    for k in query_result:
        result.append(" - ".join(k.values()))

    return result

def insert_into_table(table_name, values, cols):
    query = f"insert into {table_name} ("
    
    for i, col in enumerate(cols, 1):
        if i != len(cols):
            query += f"{col}, "
        else:
            query += f"{col}) "

    query += "values("
    for i, value in enumerate(values, 1):
        if i != len(values):
            query += f"{value}, " if type(value) == bool else f"\"{value}\", "
        else:
            query += f"{value});" if type(value) == bool else f"\"{value}\");"
    
    cur.execute(query)
    chessDB.commit()

def get_items_by_primary_keys(table_name, cols, keys):
    query = f"select * from {table_name} where "

    for i, k in enumerate(zip(cols, keys), 1):
        if i != len(cols):
            query += f"{k[0]} = \"{k[1]}\" and "
        else:
            query += f"{k[0]} = \"{k[1]}\";"
    
    return query_execute(query)

def update_table(table_name, new_values, cols, key_attr, keys):
    query = f"update {table_name} set "
    for i, new_val in enumerate(new_values, 1):
        if i != len(new_values):
            query += f"{cols[i - 1]} = {new_val}, " if type(new_val) == bool else f"{cols[i - 1]} = \"{new_val}\", "
        else:
            query += f"{cols[i - 1]} = {new_val} " if type(new_val) == bool else f"{cols[i - 1]} = \"{new_val}\" "
    
    for j, key in enumerate(keys, 1):
        if j != len(keys):
            query += f"where {key_attr[j - 1]} = \"{key}\", "
        else:
            query += f"where {key_attr[j - 1]} = \"{key}\";"
    
    cur.execute(query)
    chessDB.commit()

def get_all_from_table(table_name):
    query = f"select * from {table_name}"
    return query_execute(query)

def delete_from_table(table_name, table_keys, keys_attr):
    query = f"delete from {table_name} where "
    for i, key in enumerate(table_keys, 1):
        if i != len(table_keys):
            query += f"{keys_attr[i - 1]} = \"{key}\" and "
        else:
            query += f"{keys_attr[i - 1]} = \"{key}\";"
    
    cur.execute(query)
    chessDB.commit()
