import sqlite3

def connect():
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS book(id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, rating INTEGER, publishing TEXT, noreading INTEGER, closet INTEGER, shelf INTEGER)")
    conn.commit()
    conn.close()

def insert(title, author, year, rating, publishing, noreading, closet, shelf ):
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO book VALUES(NULL,?,?,?,?,?,?,?,?)",(title, author, year, rating, publishing, noreading, closet, shelf))
    conn.commit()
    conn.close()

def view():
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM book ")
    rows=cur.fetchall()
    conn.close()
    return rows


def view_without_index():
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM book ") #NULL yazınca python onu kendisi sıradan vermesi gerektiğini anlıyormuş
    rows=cur.fetchall()
    without_index= [x[1:] for x in rows]
    conn.close()
    return without_index

def search(title="", author="", year="", rating="", publishing="", noreading="", closet="", shelf="" ):
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR rating=? OR publishing=? OR noreading=? OR closet=? OR shelf=? ",(title,author,year,rating, publishing, noreading, closet, shelf))
    rows=cur.fetchall()
    conn.close()
    return rows

def delete(id):
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM book WHERE id=?",(id,))
    conn.commit()
    conn.close()

def update(id, title, author, year, rating, publishing, noreading, closet, shelf):
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("UPDATE book SET title=? ,author=?, year=?, rating=?, publishing=?, noreading=?, closet=?, shelf=? WHERE id=?",(title, author, year, rating, publishing, noreading, closet, shelf, id))
    conn.commit()
    conn.close()

connect()
#insert("The sun", "John Smith", 1918, 9, 1999, 2,1,2)
#delete(5)
#update(6, "The moon","John Smooth",1999,1233455)
#print(view())
#print(search(author="John Smith"))
