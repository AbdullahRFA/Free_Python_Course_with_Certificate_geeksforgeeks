"""
Given an integer n find the sum of the first n natural number.

Examples:

Input: n = 10
Output: 55
Explanation: 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 = 55.
Input: n = 5
Output: 15
Explanation: 1 + 2 + 3 + 4 + 5 = 15.
"""

#{
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends

#User function Template for python3
n = int(input())
# Your code here
sum = 0
for i in range(1,n+1):
    sum += i
print(sum)


#{
 # Driver Code Starts.
# } Driver Code Ends