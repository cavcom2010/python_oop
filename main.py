class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

    def display_info(self):
        return f"Username: {self.username}, Email: {self.email}"


# Creating an object or instance of the user class
user1 = User('Calvin Mazhindu', 'cavcom2010@email.com')

print(user1.display_info())
print(user1.email)


# Inheritance

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello , my name  is {self.name.title()} and I am {self.age} years old."


class Employee(Person):
    def __init__(self, name, age, employee_id):
        super().__init__(name, age)
        self.employee_id = employee_id

    def display_employee_info(self):
        return f"{self.greet()} My employee id is {self.employee_id}."


employee1 = Employee('Muno', 10, 'E123')

print(employee1.display_employee_info())


# Encapsulation is the bundling of data and methods that operate on
# that data within a single unit or class, and restring access to
# some of the object`s components.

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance  # Private attribute

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            return "Insufficient funds"

    def get_balance(self):
        return self.__balance


account = BankAccount('Calvin Mazhindu', 1000)
account.deposit(500)
print(account.get_balance())
# print(account.__balance)
print(account.owner)
print(BankAccount.get_balance(account))


# Polymorphism allows methods to do different things based on
# the object it is acting up on.

class Shape:
    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius


shapes = [Rectangle(3, 4), Circle(5)]

for shape in shapes:
    print(shape.area())





