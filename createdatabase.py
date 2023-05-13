import sqlite3
from sqlite3 import Error
from settings import *

def create_connection(db_file):
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def insert_user(conn, user):
    sql = ''' INSERT INTO users(id, username)
              VALUES(?,?) '''
    cur = conn.cursor()
    cur.execute(sql, user)
    conn.commit()
    return cur.lastrowid

def insert_guild(conn, guild):
    sql = ''' INSERT INTO guilds(id, guildname)
              VALUES(?,?) '''
    cur = conn.cursor()
    cur.execute(sql, guild)
    conn.commit()
    return cur.lastrowid

def main():
    database = r"./sqlite3-database-creator-tool/database.sqlite"

    sql_create_table_users = """CREATE TABLE IF NOT EXISTS users (
                                    id INTEGER PRIMARY KEY,
                                    username TEXT
    );"""

    sql_create_table_guilds = """CREATE TABLE IF NOT EXISTS guilds (
                                    id INTEGER PRIMARY KEY,
                                    guildname TEXT
    );"""

    conn = create_connection(database)

    if conn is not None:
        create_table(conn, sql_create_table_users)
        create_table(conn, sql_create_table_guilds)
    else:
        print("Error! cannot create the database connection.")

    with conn:
        user = (f'{first_user_id}', 'username')
        user_id = insert_user(conn, user)
        guild = (f'{first_guild_id}', 'guildname')
        guild_id = insert_guild(conn, guild)

if __name__ == '__main__':
    main()
