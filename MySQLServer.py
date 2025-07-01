import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(
        host = "localhost",
        username = "root",
        password = "Charity@100604"
    )

    if connection.is_connected():
        # cursor object to execute sql
        mycursor = connection.cursor()

        # SQL to create database if it doesn't exist
        create_db_query = "CREATE DATABASE IF NOT EXISTS alx_book_store"

        # Execute to create the db
        mycursor.execute(create_db_query)

        # print success
        print("Database 'alx_book_store' created successfully!")

except Error as e:
    # print errro if there is error
    print(f"Error while connecting to MYSQL or creating the database: {e}")

finally:
    # close cursor and connection
    if 'cursor' in locals() and mycursor:
        mycursor.close()

    if 'connection' in locals() and connection.is_connected():
        connection.close()