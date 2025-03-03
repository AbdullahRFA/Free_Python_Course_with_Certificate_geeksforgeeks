"""
Given an integer n. Write a program to print the Right angle triangle. The length of the perpendicular and base is n.

Examples :

Input: n = 9
Output:
*
* *
*   *
*     *
*       *
*         *
*           *
*             *
* * * * * * * * *
Explanation: Length of perpendicular and base of triangle is 9.
Input: n = 4
Output:
*
* *
*   *
* * * *
Explanation: Length of perpendicular and base of triangle is 4.
"""
n = int(input())

# Your code here
for i in range(n):
    for j in range(i+1):
        if (i==0 or i==n-1 or j==0 or i==j):
            print("*",end=' ')
        else:
            print(" ",end=' ')
    print()


#{
 # Driver Code Starts.

# } Driver Code Ends