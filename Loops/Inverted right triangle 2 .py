"""
Inverted Right Angle Triangle 2
Difficulty: BasicAccuracy: 95.2%Submissions: 234+Points: 1
Given an integer n. Write a program to print the Inverted "Right angle triangle" wall. The length of the perpendicular and base is n. Use double loop.

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