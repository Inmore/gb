import sqlite3


def select_all():
    con = sqlite3.connect('db/database.db')
    cur = con.cursor()
    cur.execute('SELECT * FROM employee')
    res = cur.fetchall()
    con.close()

    return res


def get_employee():
    return {
        'last_name': '',
        'first_name': '',
        'position': '',
        'salary': 0,
        'bonus': None
    }


def insert_employee(employee):
    con = sqlite3.connect('db/database.db')
    cur = con.cursor()
    sql = ''' INSERT INTO employee(last_name,first_name,position,salary,bonus)
                  VALUES(?,?,?,?,?) '''
    res = cur.execute(sql, (employee['last_name'], employee['first_name'], employee['position'], employee['salary'], employee['bonus']))
    con.commit()
    con.close()
    return res


def select_all_by_last_name(last_name):
    con = sqlite3.connect('db/database.db')
    cur = con.cursor()
    cur.execute('SELECT * FROM employee WHERE last_name=?', (last_name,))
    res = cur.fetchall()
    con.close()

    return res


def select_all_by_position(position):
    con = sqlite3.connect('db/database.db')
    cur = con.cursor()
    cur.execute('SELECT * FROM employee WHERE position=?', (position,))
    res = cur.fetchall()
    con.close()

    return res


def update_salary_by_id(id, salary):
    con = sqlite3.connect('db/database.db')
    cur = con.cursor()
    cur.execute('UPDATE employee SET salary=? WHERE id=?', (salary, id))
    con.commit()
    con.close()

    return id


def get_general_payroll():
    con = sqlite3.connect('db/database.db')
    cur = con.cursor()
    res = cur.execute('SELECT SUM(salary), SUM(bonus) FROM employee').fetchall()
    sum = 0
    for i in res:
        for item in i:
            sum += item
    con.close()
    return sum