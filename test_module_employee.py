import pytest
from module_employee import Employee, Department

# Проверка на отрицательный оклад
def test_wrong_salary():
    with pytest.raises(ValueError):
        employee_1 = Employee(1, "Семенов М.А.", "12.12.2000", -100)

# Номер сотрудника должен быть числовой
def test_wrong_type_Employee():
    with pytest.raises(TypeError):
        employee_1 = Employee("1", "Семенов М.А.", "12.12.2000", 10000)

# Проверяем увеличение оклада
def test_increase_salary():
    employee_1 = Employee(1, "Семенов М.А.", "12.12.2000", 10000)
    employee_1.increase_salary(5000)
    assert employee_1.salary == 15000

# Сравниваем двух сотрудников по ДР
def test_employees_lt():
    employee_1 = Employee(1, "Семенов М.А.", "12.12.2000", 10000)
    employee_2 = Employee(2, "Семенова М.М.", "12.12.1999", 10000)
    assert (employee_1 < employee_2) == False