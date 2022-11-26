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
    
    print(query)
    cur.execute(query)
    chessDB.commit()
