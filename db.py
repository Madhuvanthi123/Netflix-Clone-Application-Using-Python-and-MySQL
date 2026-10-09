import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="127.0.0.1",
        port="3307",
        user="root",
        password="Madhu@pumo123",   
        database="netflix_clonedb"
    )
print("db connected sucessfully")