import mysql.connector as mysql
from mysql.connector import Error
from mysql.connector import errorcode

table = ""

def selectTable(myCursor):

    table = input("Choose the table you want to use")
    myCursor.execute('use '+ table)

def initializeDB():
    try:
        rootpass = input("Input password: ")
        print("\n")
        conn = mysql.connect(host='localhost',user='root',passwd=rootpass)
        cursor = conn.cursor()
        cursor.execute("use data_analysis")
        print("Database connected and cursor initialized. Showing tables.\n")
        cursor.execute("show tables")
        cursor.fetchall()
        return cursor
    except:
        print("Connection error")

def showTable(myCursor):
    myCursor.execute('select * from ' + table)
    myCursor.fetchall()

def main():
    myCursor = initializeDB()
    selectTable(myCursor)
    showTable(myCursor)

main()