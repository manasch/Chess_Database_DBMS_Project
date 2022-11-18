import mysql.connector
import config

chessDB = mysql.connector.connect(
    host=config.host,
    user=config.user,
    password=config.password,
    database=config.database
)

cur = chessDB.cursor()

def query_execute(query):
    cur.execute(query)
    return cur.fetchall()
