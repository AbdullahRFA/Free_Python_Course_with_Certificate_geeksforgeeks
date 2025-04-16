# {
# Driver Code Starts
import re


# Initial Template for Python 3

#
# } Driver Code Ends

# User function Template for python3

# Define the Person class
class Person:
    def __init__(self, name='Geeks', age=10):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def set_name(self, name):
        self.__name = name

    def set_age(self, age):
        self.__age = age


person = Person()
person.get_name()
person.set_name("John")
person.set_age(21)
person.get_name()
person.get_age()


# {
# Driver Code Starts.


# Function to parse function calls similar to parseFunction in Java
def parse_function(input_str):
    # Regular expression to match method name and optional parameter
    pattern = re.compile(r"([a-zA-Z_]+)\((.*?)\)")
    match = pattern.match(input_str)
    if match:
        method_name = match.group(1)
        parameter = match.group(2)
        return method_name, parameter
    return None, None


# Main execution block similar to the Java main method
if __name__ == "__main__":
    tc = int(input())  # Read the number of test cases
    for _ in range(tc):
        func = input().strip().split(" ")
        ans = []
        called = False
        person = Person()  # Person object creation

        for call in func:
            method_name, param = parse_function(call)

            if method_name == "Person":
                called = True
                continue

            if method_name == "get_name" and called:
                ans.append(person.get_name())
                continue

            if method_name == "get_age" and called:
                ans.append(str(person.get_age()))
                continue

            if method_name == "set_name" and called:
                param = param[1:-1]  # Removing quotes around the parameter
                person.set_name(param)
                continue

            if method_name == "set_age" and called:
                person.set_age(int(param))
                continue

            if not called:
                ans.append("Person object not created")
                break

        if len(ans) == 0:
            print("[]")
        else:
            print(" ".join(ans))
        print("~")

# } Driver Code Ends