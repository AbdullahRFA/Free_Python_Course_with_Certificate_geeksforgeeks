"""
Given an integer n. Write a program to print the inverted "Right angle triangle" wall. The length of the perpendicular and base is n.

Note: Use string multiplication for python.

Examples:

Input: n = 4
Output:
* * * *
* * *
* *
*
Explanation: Length of perpendicular and base of triangle is 4 .
Input: n = 3
Output:
* * *
* *
*
Explanation: Length of perpendicular and base of triangle is 3 .
"""

#{
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends

#User function Template for python3
n = int(input())

# Your code here
for i in range(n):
    for j in range(n-i):
        print("*", end=' ')
    print()


#{
 # Driver Code Starts.

# } Driver Code Ends