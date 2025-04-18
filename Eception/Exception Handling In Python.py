"""
You are given two integers a and b. Your task is to find the minimum value obtained from performing any of the following arithmetic operations between a and b: addition (+), subtraction (-), multiplication (*), and division (/).
Make sure to use exception handling to manage any potential division by zero errors.
Note: If division by zero is attempted, handle the exception and exclude the division operation from consideration.

Examples:

Input: a = 5, b = -5
Output: -25
Explanation:
The results of the operations are:
5+(−5)=0
5−(−5)=10
5×(−5)=−25
5/(−5)=−1
The minimum value is -25.
Input: a = 5, b = 0
Output: 0
Explanation:
The results of the operations are:
5+0=5
5−0=5
5×0=0
5/0 raises a "Division by zero" exception.
Thus, the minimum value among valid operations is 0.
"""

#{
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends

#User function Template for python3
def find_minimum(a, b):
    list1 = []
    list1.append(a+b)
    list1.append(a-b)
    list1.append(a*b)
    # Your code here
    try:
        list1.append(a/b)
    except ZeroDivisionError:
        pass
    return min(list1)
    # Return the minimum of all the valid operations


#{
 # Driver Code Starts.

a = int(input())
b = int(input())
print(find_minimum(a,b))
# } Driver Code Ends