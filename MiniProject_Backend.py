#backend
import sqlite3

import sqlite3

def MovieData():
    # Connect to the SQLite database 'movie1.db'
    con = sqlite3.connect('movie1.db')
    cur = con.cursor()

    # Corrected SQL query with a closing parenthesis
    cur.execute('''
        CREATE TABLE IF NOT EXISTS book (
            id INTEGER PRIMARY KEY, 
            Movie_ID TEXT, 
            Movie_Name TEXT, 
            Release_Date TEXT, 
            Director TEXT, 
            Cast TEXT, 
            Budget TEXT, 
            Duration TEXT, 
            Rating TEXT
        )
    ''')

    # Commit the changes and close the connection
    con.commit()
    con.close()

    
def AddMovieRec(Movie_ID,Movie_Name,Release_Date,Director,Cast,Budget,Duration,Rating):
    con=sqlite3.connect("movie1.db")    
    cur=con.cursor()
    cur.execute("INSERT INTO book VALUES (NULL, ?,?,?,?,?,?,?,?)", (Movie_ID,Movie_Name,Release_Date,Director,Cast,Budget,Duration,Rating))
    con.commit()
    con.close()

def ViewMovieData():
    con=sqlite3.connect("movie1.db")    
    cur=con.cursor()
    cur.execute("SELECT * FROM book")
    rows=cur.fetchall()
    con.close()    
    return rows

def DeleteMovieRec(id):    
    con=sqlite3.connect("movie1.db")    
    cur=con.cursor()
    cur.execute("DELETE FROM book WHERE id=?", (id,))
    con.commit()
    con.close()  

def SearchMovieData(Movie_ID="",Movie_Name="",Release_Date="",Director="",Cast="",Budget="",Duration="",Rating=""):  
    con=sqlite3.connect("movie1.db")    
    cur=con.cursor()
    cur.execute("SELECT * FROM book WHERE Movie_ID=? OR Movie_Name=? OR Release_Date=? OR Director=? OR Cast=? OR Budget=? OR Duration=? OR Rating=?",(Movie_ID,Movie_Name,Release_Date,Director,Cast,Budget,Duration,Rating))
    rows=cur.fetchall()
    con.close()    
    return rows

def UpdateMovieData(id,Movie_ID="",Movie_Name="",Release_Date="",Director="",Cast="",Budget="",Duration="",Rating=""):
    con=sqlite3.connect("movie1.db")    
    cur=con.cursor()
    cur.execute("UPDATE book SET Movie_ID=?,Movie_Name=?,Release_Date=?,Director=?,Cast=?,Budget=?,Duration=?,Rating=?, WHERE id=?",(Movie_ID,Movie_Name,Release_Date,Director,Cast,Budget,Duration,Rating))
    con.commit()
    con.close()
    


