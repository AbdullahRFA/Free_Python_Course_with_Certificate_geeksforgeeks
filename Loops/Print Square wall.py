"""
Given an integer n,  write a program to print the square wall of size n using a single loop and string multiplication.

Examples:

Input: n = 5
Output:
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *
Explanation: Its perfect square wall.
Input: n = 4
Output:
* * * *
* * * *
* * * *
* * * *
Explanation: Its perfect square wall.
"""
#{
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends

#User function Template for python3
n = int(input())

# Your code here
for i in range(n):
    for j in range(n):
        print("*",end=' ')
    print()


#{
 # Driver Code Starts.

# } Driver Code Ends