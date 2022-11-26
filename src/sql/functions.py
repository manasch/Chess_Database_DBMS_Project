import mysql.connector
import config

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
    query = 'select '
    for i, req in enumerate(required, 1):
        if i != len(required):
            query += f'{req.split(".")[-1]}, '
        else:
            query += f'{req.split(".")[-1]} '
    
    query += f'from {referenced};'
    query_result = query_execute(query)

    result = []
    for k in query_result:
        result.append(" - ".join(k.values()))

    return result
