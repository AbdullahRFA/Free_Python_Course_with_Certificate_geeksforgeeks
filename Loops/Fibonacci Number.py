"""
Given an integer n. Write a program to find the nth Fibonacci number.

F(0)= 0, F(1)=1
The nth Fibonacci number is given by the forumla F(n) = F(n-1) + F(n-2). The first few fibonacci numbers are: 0 1 1 2 3 5. . . .

Examples:

Input: n = 4
Output: 3
Explanation: In the series 0 1 1 2 3 5...... the fourth fibonacci number is 3.
Input: n = 5
Output: 5
Explanation: In the series 0 1 1 2 3 5 8...... the fifth fibonacci number is 5.
"""

# {
# Driver Code Starts
# Initial Template for Python 3

# } Driver Code Ends

# User function Template for python3
# Back-end complete function Template for Python 3
n = int(input())


########### Write your code below ###############
def fibu(n):
    n1 = 1
    n2 = 1

    if n == 1 or n == 2:
        return n1
    else:
        for i in range(3, n + 1):
            fib = n1 + n2
            n2 = n1
            n1 = fib

        return fib


fib = fibu(n)

########### Write your code above ###############
print(fib)

# {
# Driver Code Starts.

# } Driver Code Ends