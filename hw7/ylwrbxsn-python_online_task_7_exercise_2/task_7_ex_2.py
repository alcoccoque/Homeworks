"""
Task 7_2
Create classes Employee, SalesPerson, Manager and Company with predefined functionality.

Create basic class Employee and declare following content:
• Attributes – `name` (str), `salary` and `bonus` (int), set with property decorator
• Constructor - parameters `name` and `salary`
• Method `bonus` - sets bonuses to salary, amount of which is delegated as `bonus`
• Method `to_pay` - returns the value of summarized salary and bonus.

Create class SalesPerson as class Employee inheritor and declare within it:
• Constructor with parameters: `name`, `salary`, `percent` – percent of plan performance (int, without the % symbol), first two of which are passed from basic class constructor
• Redefine method of parent class `bonus` in the following way: if the sales person completed the plan more than 100%, their bonus is doubled (is multiplied by 2), and if more than 200% - bonus is tripled (is multiplied by 3)

Create class Manager as Employee class inheritor, and declare within it:
• Constructor with parameters: `name`, `salary` and `client_number` (int, number of served clients), first two of which are passed to basic class constructor.
• Redefine method of parent class `bonus` in the following way: if the manager served over 100 clients, their bonus is increased by 500, and if more than 150 clients – by 1000.

Create class Company and declare within it:
• Constructor with parameters: `employees` – list of company`s employees (made up of Employee/SalesPerson/Manager classes instances) with arbitrary length `n`
• Method `give_everybody_bonus` with parameter company_bonus (int) that sets the amount of basic bonus for each employee.
• Method `total_to_pay` that returns total amount of salary of all employees including awarded bonus
• Method `name_max_salary` that returns name of the employee, who received maximum salary including bonus.

Note:
Class attributes and methods should bear exactly the same names as those given in task description
Methods should return only target values, without detailed explanation within `return`
"""


class Employee:
    def __init__(self, name: str, salary):
        self.name = name
        self.salary = salary
        self.bonus = 0
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, salary):
        self.__salary = salary

    @property
    def bonus(self):
        return self.__bonus

    @bonus.setter
    def bonus(self, bonus):
        self.__bonus = bonus

    def to_pay(self):
        return self.salary + self.bonus


class SalesPerson(Employee):
    # __bonus = 0
    def __init__(self, name, salary, percent):
        super().__init__(name, salary)
        self.percent = percent
        # self.__bonus = self.bonus

    @property
    def percent(self):
        return self.__percent

    @percent.setter
    def percent(self, percent):
        self.__percent = percent

    def to_pay(self):
        return self.salary + self.bonus

    @property
    def bonus(self):
        if self.percent >= 200:
            return self.__bonus * 3
        elif self.percent >= 100:
            return self.__bonus * 2
        else:
            return self.__bonus

    @bonus.setter
    def bonus(self, bonus):
        __bonus = bonus
        super(SalesPerson, type(self)).bonus.fset(self, __bonus)


class Manager(Employee):
    # __bonus = 0
    def __init__(self, name, salary, client_number: int):
        super().__init__(name, salary, )
        self.client_number = client_number
        # self.__bonus = self.bonus

    @property
    def client_number(self):
        return self.__client_number

    @client_number.setter
    def client_number(self, client_number):
        self.__client_number = client_number

    @property
    def bonus(self):
        if self.client_number >= 150:
            return self.__bonus + 1000
        elif self.client_number >= 100:
            return self.__bonus + 500
        else:
            return self.__bonus

    @bonus.setter
    def bonus(self, bonus):
        __bonus = bonus
        super(Manager, type(self)).bonus.fset(self, __bonus)
class Company:
    def __init__(self, employees: list, n=0):
        self.employees = employees

    @property
    def employees(self):
        return self.__employees

    @employees.setter
    def employees(self, employees):
        self.__employees = employees

    def give_everybody_bonus(self, bonus):
        Employee.bonus = bonus
        SalesPerson.bonus = bonus
        Manager.bonus = bonus

    def total_to_pay(self):
        return sum(x.to_pay() for x in self.employees)

    def name_max_salary(self):
        return max(self.employees, key=Employee.to_pay).name

employer = Employee("Jir", 2000)
manager = Manager("Zis", 500, 200)
Employee.bonus = 200
salesperson = SalesPerson("Tis", 600, 150)

print(salesperson.bonus)
print(manager.bonus)
manager.bonus = 200
salesperson = 200

print(employer.bonus)
print(employer.to_pay())
company = Company([employer, manager, salesperson], 2)
company.give_everybody_bonus(51000)

print(manager.bonus)
print(employer.bonus)
print(company.name_max_salary())
company.total_to_pay()

