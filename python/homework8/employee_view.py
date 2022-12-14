def add_employee(employee):
    employee['last_name'] = input('last_name: ')
    employee['first_name'] = input('first_name: ')
    employee['position'] = input('position: ')
    employee['salary'] = input('salary: ')
    employee['bonus'] = input('bonus: ')
    return employee


def show_employees(employees):
    for i in employees:
        print(i)
    return None


def show_employees_by_last_name(employees):
    for i in employees:
        print(i)
    return None


def show_employees_by_position(employees):
    for i in employees:
        print(i)
    return None


def show_changed_employee(id):
    print(f'Изменена зарплата работнику с id={id}')


def show_general_payroll(sum):
    print(f'Общий фонд заработной платы={sum}')
