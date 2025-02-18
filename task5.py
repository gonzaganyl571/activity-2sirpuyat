class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    def give_raise(self, amount):
        self.salary += amount

    def display_employee(self):
        print(f"Employee Name: {self.name}")
        print(f"Position: {self.position}")
        print(f"Salary: ₱{self.salary:.2f}")

employee = Employee("nyl gonzaga", "Chat support", 15000)

print("Before raise:")
employee.display_employee()

employee.give_raise(5000)

print("\nAfter raise:")
employee.display_employee()