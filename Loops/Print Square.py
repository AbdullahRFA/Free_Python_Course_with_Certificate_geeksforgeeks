"""
Given an integer n, write a program to print the square of size n using "*" character.

Examples :

Input: n = 4
Output:
* * * *
*     *
*     *
* * * *
Explanation: It's a square! Each side contains n = 4 .
Input: n = 3
Output:
* * *
*   *
* * *
Explanation: It's a square! Each side contains n = 3
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
        if i == 0 or i == n-1 or j==0 or j==n-1:
            print("*",end=' ')
        else:
            print(" ",end=' ')
    print()


#{
 # Driver Code Starts.

# } Driver Code Ends