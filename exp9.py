class Employee:
    def __init__(self, name, employee_id):
        self.name = name
        self.employee_id = employee_id

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Employee ID: {self.employee_id}")


class Manager(Employee):
    def __init__(self, name, employee_id, department):
        super().__init__(name, employee_id)
        self.department = department
        self.employees_managed = []

    def assign_employee(self, employee):
        self.employees_managed.append(employee)

    def display_info(self):
        super().display_info()
        print(f"Department: {self.department}")
        if self.employees_managed:
            print("Employees Managed:")
            for employee in self.employees_managed:
                print(f"- {employee.name}")


# Example usage:

# Create regular employees
employee1 = Employee("John Doe", 1001)
employee2 = Employee("Alice Smith", 1002)

# Create a manager
manager = Manager("Jane Johnson", 5001, "HR")

# Assign employees to the manager
manager.assign_employee(employee1)
manager.assign_employee(employee2)

# Display information about the manager and employees managed
manager.display_info()
