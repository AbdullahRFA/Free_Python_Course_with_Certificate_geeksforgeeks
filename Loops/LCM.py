"""
Given two numbers a and b. The task is to find out their LCM.

Examples:

Input: a = 5, b = 10
Output: 10
Explanation: LCM of 5 and 10 is 10
Input: a = 14, b = 8
Output: 56
Explanation: LCM of 14 and 8 is 56
"""

#{
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends

#User function Template for python3
import math
a = int(input())
b = int(input())

# Your code here
print((a*b)//math.gcd(a,b))


#{
 # Driver Code Starts.

# } Driver Code Ends