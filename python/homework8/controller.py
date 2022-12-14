import employee_model
import employee_view


def add_employee():
    employee = employee_model.get_employee()
    employee = employee_view.add_employee(employee)
    employee_model.insert_employee(employee)
    return None


def show_all_employees():
    employees = employee_model.select_all()
    employee_view.show_employees(employees)
    return None


def find_by_last_name(last_name):
    employees = employee_model.select_all_by_last_name(last_name)
    employee_view.show_employees_by_last_name(employees)
    return None


def find_by_position(position):
    employees = employee_model.select_all_by_position(position)
    employee_view.show_employees_by_position(employees)
    return None


def change_salary(id, salary):
    employee_id = employee_model.update_salary_by_id(id, salary)
    employee_view.show_changed_employee(employee_id)
    return None


def get_general_payroll():
    sum = employee_model.get_general_payroll()
    employee_view.show_general_payroll(sum)
    return None
