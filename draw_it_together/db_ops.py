import os
import psycopg2

PASSWD_FILE = os.path.join(os.path.dirname(__file__), "password")

PASSWD = open(PASSWD_FILE).read()

CONN_STR = "host='traphouse.us'" \
           " dbname='draw_it_together'" \
           " user='drawsite'" \
           " password='{}'".format(PASSWD) 

def connect():
    return psycopg2.connect(CONN_STR)

def db_add_user(user_id, user):
    insert_str = "INSERT INTO users (id, name)\n" \
                 "  VALUES ('{}', '{}');".format(user_id, user)
    conn = connect()
    cur = conn.cursor()
    cur.execute(insert_str)
    conn.commit()
    cur.close()

def db_clear_table(table):
    conn = connect()
    cur = conn.cursor()
    cur.execute('DELETE FROM {}'.format(table))
    conn.commit()
    cur.close()

def db_reset_serial(table, column):
    conn = connect()
    cur = conn.cursor()
    reset_str = "ALTER SEQUENCE {}_{}_seq RESTART WITH 1".format(table, column)
    cur.execute(reset_str)
    conn.commit()
    cur.close()

def db_check_for_name(name):
    conn = connect()
    cur = conn.cursor()
    select_str = "SELECT name \n" \
                 "  FROM users \n" \
                 "  WHERE name = '{}'".format(name)
    cur.execute(select_str)
    return cur.fetchone() is not None

def db_add_image(name, image):
    select_str = "SELECT count(name)\n" \
                 "  FROM pictures\n" \
                 "  WHERE name='{}'".format(name)
    conn = connect()
    cur = conn.cursor()
    cur.execute(select_str)
    count = cur.fetchone()
    insert_str = "INSERT INTO pictures (image, name, order_num)\n" \
                 "  VALUES ('{}', '{}', {});".format(image, name, count[0]+1)
    cur.execute(insert_str)
    conn.commit()
    cur.close()