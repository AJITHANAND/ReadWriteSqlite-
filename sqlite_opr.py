import sqlite3
import pandas as pd
#create database or connect if its exist..
def create_database(name):
    try:
        connection = sqlite3.connect(name)
        return connection
    except Exception as e:
        print("connection err"+e)

# create table Movies 
def create_table(cursor):
    cursor.execute("CREATE TABLE IF NOT EXISTS Movies (Name TEXT,Actor TEXT,Actress TEXT,Released INT,Director TEXT)")

#insert values to table
def insert_values(con):
    movie_name = input("Movie name:")
    movie_actor = input("Actor name:")
    movie_actress = input("Actress name:")
    moive_released = int(input("Released Year:"))
    movie_director = input("Director name:")
    with con:
        con.execute("insert into Movies values(?,?,?,?,?)",(movie_name,movie_actor,movie_actress,moive_released,movie_director))

#print values in table
def display(con):
    data=pd.read_sql_query("SELECT * FROM Movies", con)
    if data.empty:
        print("Table is empty")
    else:
        print(data)
     
def main():
    con = create_database("Movie_database")
    cursor = con.cursor()
    create_table(cursor)
    n = int(input("No of Movies wants to insert :"))
    while(n>0):
        n-=1
        insert_values(con)
    display(con)
    cursor.close()
    con.close()
if __name__=="__main__":
    main()