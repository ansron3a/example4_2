import pytest
from module_employee import Employee, Department


class Testing:
    # Проверка на отрицательный оклад
    def test_wrong_salary(self):
        with pytest.raises(ValueError):
            employee_1 = Employee(1, "Семенов М.А.", "12.12.2000", -100)

    # Номер сотрудника должен быть числовой
    def test_wrong_type_Employee(self):
        with pytest.raises(TypeError):
            employee_1 = Employee("1", "Семенов М.А.", "12.12.2000", 10000)

    # Проверяем увеличение оклада
    def test_increase_salary(self):
        employee_1 = Employee(1, "Семенов М.А.", "12.12.2000", 10000)
        employee_1.increase_salary(5000)
        assert employee_1.salary == 15000

    # Сравниваем двух сотрудников по ДР
    def test_employees_lt(self):
        employee_1 = Employee(1, "Семенов М.А.", "12.12.2000", 10000)
        employee_2 = Employee(2, "Семенова М.М.", "12.12.1999", 10000)
        assert (employee_1 < employee_2) == False

    # Проверка при добавлении сотрудника в отдел. (неверный тип)
    def test_wrong_type_Department(self):
        with pytest.raises(TypeError):
            emp1 = Employee(1, "Холодов А.А.", "12.12.2000", 10000)
            emp1 = Employee(1, "Семенов А.А.", "12.12.2000", 10000)
            emp2 = Employee(1, "Семенов К.Н.", "12.12.1999", 10000)
            dep1 = Department("Закупки", emp1, emp2)
            dep1.append("Петров А.Н.")

    # Проверка при добавлении сотрудника в отдел (добавили правильно)
    def test_append_Department(self):
        with pytest.raises(TypeError):
            emp1 = Employee(1, "Холодов А.А.", "12.12.2000", 10000)
            emp2 = Employee(1, "Семенов А.А.", "12.12.2000", 10000)
            dep1 = Department("Закупки", emp1, emp2)
            count_before = len(dep1.employees)
            dep1.append(emp2)
            assert count_before == len(dep_1.employees) - 1


if __name__ == "__main__":
    ex = Testing
