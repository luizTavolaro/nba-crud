import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="nba-database.c0yjdr9hfgdy.us-east-1.rds.amazonaws.com",
        port=3306,
        user="admin",
        password="admin@123!",
        database='nba'
    )