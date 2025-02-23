"""
Given three integers a, d and n. Where a is the first term, d is the common difference of an A.P.  Calculate the nth term of A.P.
The nth term is given by an = a + (n-1)d

Examples:

Input: a = 5, d = 2, n = 5
Output: 13
Explanation: anth = a + (n-1)d = 5 + (5-1)*2 = 5 + 8 = 13
Input: a = 10, d = 10, n = 101
Output: 1010
Explanation: anth = a + (n-1)d = 10 + (101-1)*10 = 10 + 1000 = 1010.
"""

#{
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3
a=int(input())
d=int(input())
n=int(input())

########### Write your code below ###############
# Compute the AP Term
ans = a+(n-1)*d
########### Write your code above ###############

print(ans)

#{
 # Driver Code Starts.

# } Driver Code Ends