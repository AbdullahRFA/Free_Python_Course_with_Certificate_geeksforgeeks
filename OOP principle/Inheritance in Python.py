"""
Implement the following classes to understand inheritance in Python:

Class Name: Employee
Attributes:
id (int)
salary (int)
Constructor: __init__(self, id, salary) — Initializes the values to respective variables.
Class Name: SalesEmployee (Subclass of Employee)
Attributes:
Inherited from Employee: id, salary
New attribute: sales (int)
Constructor: __init__(self, id, salary, sales) — Calls super().__init__(id, salary) to initialize id and salary, and initializes the sales attribute.
Examples:

Input: id = 14, salary = 30000, sales = 20
Output:
14 30000
14 30000 20
"""


# {
# Driver Code Starts
# Initial Template for Python 3

# } Driver Code Ends

# User function Template for python3
# Implement Employee and SalesEmployee classes here
class Employee:
    def __init__(self, id, salary):
        self.id = id
        self.salary = salary

    def printDetails(self):
        print(f"{self.id} {self.salary}")


class SalesEmployee(Employee):
    def __init__(self, id, salary, sales):
        super().__init__(id, salary)
        self.sales = sales

    def printDetails(self):
        super().printDetails()
        print(self.sales)


# e = Employee(14,30000)
slp = SalesEmployee(14, 30000, 20)
# e.printDetails
Employee.printDetails
slp.printDetails

# {
# Driver Code Starts.

if __name__ == "__main__":
    t = int(input())
    while t:
        t -= 1
        emp_id = int(input())
        emp_salary = int(input())
        emp_sales = int(input())

        # Create an Employee object
        employee = Employee(emp_id, emp_salary)
        print(f"{employee.id} {employee.salary}")

        # Create a SalesEmployee object
        sales_employee = SalesEmployee(emp_id, emp_salary, emp_sales)
        print(f"{sales_employee.id} {sales_employee.salary} {sales_employee.sales}")
# } Driver Code Ends