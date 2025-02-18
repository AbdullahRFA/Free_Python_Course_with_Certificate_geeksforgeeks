"""
Given two sets a and b, the task is to find the number of elements in the union between these two sets.

The Union of the two sets can be defined as the set containing distinct elements from both sets. If there are repetitions, then only one element occurrence should be there in the union.

Note: Elements are not necessarily distinct.

Examples

Input: a = [1, 2, 3, 4, 5], b = [1, 2, 3]
Output: 5
Explanation: 1, 2, 3, 4 and 5 are the elements which comes in the union of both sets. So count is 5.
Input: a = [85, 25, 1, 32, 54, 6], b = [85, 2]
Output: 7
Explanation: 85, 25, 1, 32, 54, 6, and 2 are the elements which comes in the union of both sets. So count is 7.
Input: a[] = [1, 2, 1, 1, 2], b[] = [2, 2, 1, 2, 1]
Output: 2
Explanation: We need to consider only distinct. So count is 2.


"""


a = set([int(x) for x in input().strip().split()])
b = set([int(x) for x in input().strip().split()])

########### Write your code below ###############
st = a.union(b)
# Union of a and b

########### Write your code above ###############

# Printing the size of the set which is the total number of elements in the set.
print(len(st))



#{
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends