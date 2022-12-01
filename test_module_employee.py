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