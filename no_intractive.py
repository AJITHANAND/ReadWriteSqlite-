from sqlite_opr import create_database,display,create_table

my_fav=[["Hridayam","Pranav","Kalyani",2022,"Vineeth"],["Aamis","Arghadeep","Lima Das",2019,"Bhaskar"]]

def insert_values(con):
    with con:
        for i in my_fav:
            con.execute("insert into Movies values(?,?,?,?,?)",(i[0],i[1],i[2],i[3],i[4]))

def main():
    con = create_database("MovieDB.db")
    cursor = con.cursor()
    create_table(cursor)
    insert_values(con)
    display(con)
    cursor.close()
    con.close()

if __name__=="__main__":
    main()