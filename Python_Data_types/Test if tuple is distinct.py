"""
Given a tuple arr , print "True" if all elements of tuple are different otherwise print "False".

A tuple is a collection of items that are ordered and unchangeable.

Examples:

Input:
arr = (1, 2, 3, 4, 5, 4)
Output: False
Input:
arr = (1, 2, 3, 4, 5)
Output: True

"""

#{
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3
arr = tuple(map(int, input().split()))

########### Write your code below ###############
# Print "True" if all elements of tuple are different, otherwise print "False"
if len(arr) == len(set(arr)):
    print("True")
else:
    print("False")
########### Write your code above ###############

#{
 # Driver Code Starts.
# } Driver Code Ends