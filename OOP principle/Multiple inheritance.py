"""
Implement the following classes to understand multiple inheritance in Python:

Class Name: Student
Attributes:
sid (int) — Student ID.
deptid (int) — Department ID.
Constructor: __init__(self, sid, deptid) — Initializes the sid and deptid attributes.
Method: get_info(self) — Returns a formatted string with the student ID and department ID, eg., "StudentID:101 DepartmentID:42"
Class Name: Faculty
Attributes:
eid (int) — Employee ID.
deptid (int) — Department ID.
Constructor: __init__(self, eid, deptid) — Initializes the eid and deptid attributes.
Method: get_info(self) — Returns a formatted string with the employee ID and department ID, eg., "EmployeeID:555 DepartmentID:42"
Class Name: PhDStudent (Inherits from both Student and Faculty)
Constructor: __init__(self, sid, eid, deptid) — Calls the constructors of Student and Faculty to initialize sid, eid, and deptid.
Method: get_info(self) — Returns a formatted string with the student ID, employee ID and department ID, eg., "Student ID:101 EmployeeID:555 DepartmentID:42".
Example:

Input: sid = 101, eid = 555, deptid = 42
Output:
StudentID:101 DepartmentID:42
EmployeeID:555 DepartmentID:42
Student ID:101 EmployeeID:555 DepartmentID:42
"""


# {
# Driver Code Starts
# Initial Template for Python 3

# } Driver Code Ends

# User function Template for python3
# Implement Student, Faculty and PhdStudent classes here
class Student:
    def __init__(self, id, depid):
        self.id = id
        self.depid = depid

    def get_info(self):
        return f"StudentID:{self.id} DepartmentID:{self.depid}"


class Faculty:
    def __init__(self, eid, depid):
        self.eid = eid
        self.depid = depid

    def get_info(self):
        return f"EmployeeID:{self.eid} DepartmentID:{self.depid}"


class PhDStudent(Student, Faculty):
    def __init__(self, sid, eid, depid):
        Student.__init__(self, sid, depid)
        Faculty.__init__(self, eid, depid)

    def get_info(self):
        return f"StudentID:{self.id} EmployeeID:{self.eid} DepartmentID:{self.depid}"


phds = PhDStudent(101, 555, 42)
std = Student(101, 42)
fct = Faculty(555, 42)
std.get_info()
fct.get_info()
phds.get_info()

# {
# Driver Code Starts.

if __name__ == "__main__":
    t = int(input())
    while t:
        t -= 1
        sid = int(input())
        eid = int(input())
        deptid = int(input())

        # Create a Student object
        student = Student(sid, deptid)
        # Create a Faculty object
        faculty = Faculty(eid, deptid)
        # Create a PhDStudent object
        phd_student = PhDStudent(sid, eid, deptid)

        if not isinstance(phd_student, Student):
            print("phd_student doesn't inherit from Student class")
        elif not isinstance(phd_student, Faculty):
            print("phd_student doesn't inherit from Faculty class")
        else:
            print(student.get_info())
            print(faculty.get_info())
            print(phd_student.get_info())

# } Driver Code Ends
