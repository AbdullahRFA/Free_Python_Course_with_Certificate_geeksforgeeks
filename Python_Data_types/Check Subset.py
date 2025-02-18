"""
Given two sets a and b. check whether a is subset of b ?

a is subset of b, if all elements of a set a are present in another set b.

Examples:

Input: a = [1, 4, 3], b = [1, 4, 3, 2]
Output: True

"""

#{
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
a = set(list(map(int, input().split())))
b = set(list(map(int, input().split())))

########### Write your code below ###############
res = a.issubset(b)
# Is a subset of b?

########### Write your code above ###############
# Print True or False
print(res)


#{
 # Driver Code Starts.
# } Driver Code Ends