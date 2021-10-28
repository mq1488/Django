import sqlite3
import mysql.connector as mysql
import psycopg2


def clear(root):
    item = root.grid_slaves()
    for i in item:
        i.destroy()


def connect_mysql():
    db = mysql.connect(
        host="localhost",
        user="root",
        database='python_mysql',
        passwd="admin"
    )
    cur = db.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS products(
               pname VARCHAR(255),
               price VARCHAR(255),
               in_stock BOOLEAN);
            """)
    return db


def connect_postgers():
    conn = psycopg2.connect(
        host="localhost",
        database="product",
        user="odoo",
        password="odoo")
    cur = conn.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS products(
               pname VARCHAR(255),
               price VARCHAR(255),
               in_stock BOOLEAN);
            """)
    return conn


def insert_table_mysql(name, price, in_stock):
    db = connect_mysql()
    cur = db.cursor()
    try:
        sql = "INSERT INTO products (pname, price,in_stock) VALUES (%s, %s, %s)"
        val = (name.get(), price.get(), in_stock.get())
        cur.execute(sql, val)
    except ValueError:
        print('Error')
    db.commit()
    db.close()


def select_table_mysql(output):
    db = connect_mysql()
    cur = db.cursor()
    cur.execute("SELECT * FROM products;")
    myresult = cur.fetchall()
    text = ''
    for x in myresult:
        text = text + str(x) + ' '
    output.configure(text=text)
    db.close()


def update_table_mysql(name, price, in_stock):
    db = connect_mysql()
    cur = db.cursor()
    cur.execute("UPDATE products SET price={} ,in_stock={} WHERE pname='{}'".format(name.get(), price.get(), in_stock.get()))
    db.commit()
    db.close()


def delete_table_mysql(name):
    db = connect_mysql()
    cur = db.cursor()
    cur.execute("DELETE FROM products WHERE pname='{}'".format(name.get()))
    db.commit()
    db.close()


def export_to_db2(output):
    conn = connect_postgers()
    cur = conn.cursor()

    mysqldb = connect_mysql()
    mysql_cur = mysqldb.cursor()
    mysql_cur.execute("SELECT * FROM products;")
    mysql_result = mysql_cur.fetchall()

    sql = "INSERT INTO products (pname, price,in_stock) VALUES (%s, %s, %s)"
    for item in mysql_result:
        if item[2] == 0:
            lis = list(item)
            lis[2] = False
            item = tuple(lis)
        elif item[2] == 1:
            lis = list(item)
            lis[2] = True
            item = tuple(lis)
        cur.execute(sql, item)
        conn.commit()

    cur.execute("SELECT * FROM products;")
    post_result = cur.fetchall()
    text = ''
    for x in post_result:
        text = text + str(x) + ' '
    output.configure(text=text)


def export_to_db3(output):
    conn = connect_postgers()
    cur = conn.cursor()
    cur.execute("SELECT * FROM products;")
    postgers_result = cur.fetchall()

    lite_conn = sqlite3.connect('products.db')
    lite_cur = lite_conn.cursor()
    lite_cur.execute("""CREATE TABLE IF NOT EXISTS products(
                       pname VARCHAR(255),
                       price VARCHAR(255),
                       in_stock BOOLEAN);
                    """)
    sql = "INSERT INTO products VALUES(?, ?, ?);"
    for item in postgers_result:
        if item[2] == None:
            lis = list(item)
            lis[2] = ''
            item = tuple(lis)
        lite_cur.execute(sql, item)
        lite_conn.commit()

    lite_cur.execute("SELECT * FROM products;")
    lite_result = lite_cur.fetchall()
    text = ''
    for x in lite_result:
        text = text + str(x) + ' '
    output.configure(text=text)
