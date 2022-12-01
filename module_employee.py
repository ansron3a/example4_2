import datetime as DT


def str_to_date(self_date, other_date):
    dt1 = self_date.split(".")
    dt2 = other_date.split(".")
    self_bdate = DT.date(int(dt1[2]), int(dt1[1]), int(dt1[0]))
    other_bdate = DT.date(int(dt2[2]), int(dt2[1]), int(dt2[0]))
    return self_bdate, other_bdate


class Employee:
    def __init__(self, number, fio, bdate, oklad, on_leave=False):
        if oklad < 0:
            raise ValueError("Оклад не может быть отрицательным")
        if type(number) != int:
            raise TypeError("Номер сотрудника должен быть числовым")
        self.number = number
        self.fio = fio
        self.bdate = bdate
        self.salary = oklad
        self.on_leave = on_leave

    # Изменяем оклад
    def increase_salary(self, summa):
        self.salary += summa

    # Перехват функции print, когда она преобразует свое значение в строку
    def __str__(self):
        return f"Сотрудник {self.number} {self.fio}, {self.bdate}," \
               f" оклад: {self.salary}, в отпуске: {'да' if self.on_leave else 'нет'}"

    # Здесь и ниже операции сравнения >, >=, <, <=, ==, !=
    def __lt__(self, other):  # <
        self_bdate, other_bdate = str_to_date(self.bdate, other.bdate)
        return self_bdate < other_bdate

    def __eq__(self, other):  # ==
        self_bdate, other_bdate = str_to_date(self.bdate, other.bdate)
        return self_bdate == other_bdate

    def __le__(self, other):  # <=
        if self.__eq__(other):
            return True

        if self.__lt__(other):
            return True
        else:
            return False


class Department:
    def __init__(self, title, chief=None, employees=None):
        self.title = title
        if employees is None:
            employees = list()
        self.employees = employees
        self.chief = chief

    # Добавляем сотрудника в отдел
    def append(self, emp):
        if type(emp) != Employee:
            raise TypeError("Атрибут содержит тип {} вместо Employee".format(type(emp)))
        self.employees.append(emp)

    # Перехват функции print, когда она преобразует свое значение в строку
    # Возврат информации об отделе
    def __str__(self):
        return f"Отдел: {self.title}, Начальник: {self.chief.fio}, Количество сотрудников: {len(self.employees)} "

    # Вывод сотрудников отдела
    def print_employees(self):
        for emp in self.employees:
            print(emp)

    # Вывод сотрудников отдела в отпуске/не в отпуске
    def print_employees_on_leave(self, status=True):
        for emp in self.employees:
            if emp.on_leave == status:
                print(emp.number, emp.fio)


emp_1 = Employee(1, 'Василий Иванович Гришкавец', '12.12.1970', 35000)
emp_2 = Employee(2, 'Елизавета Петровна Кочедыкова', '17.10.1980', 33000)
# Сравним по датам рождения
print(emp_1 < emp_2)
print(emp_1 > emp_2)
print(emp_1 == emp_2)
print(emp_1 <= emp_2)
print(emp_1 >= emp_2)

depart_1 = Department('архив', emp_1)
depart_1.append(emp_1)
depart_1.append(emp_2)
print(depart_1)
depart_1.print_employees()
emp_1.increase_salary(1333)
emp_1.on_leave = True
emp_2.on_leave = True
print(emp_1)
depart_1.print_employees_on_leave()
