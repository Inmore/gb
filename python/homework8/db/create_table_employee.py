import sqlite3


def create_table_employee():
    con = sqlite3.connect('database.db')
    cur = con.cursor()

    with open('create_table_employee.sql', 'r') as sql:
        sql = sql.read()

    cur.executescript(sql)
    con.close()


if __name__ == '__main__':
    create_table_employee()
