"""
Given two lists of integers, perform the following operations:

zip(): Combine both lists into one iterable of tuples.

filter(): Filter out all elements in list1 that are less than or equal to 2.

map(): Multiply each element of list1 by 2 using a lambda function.

You need to complete the given program.

Examples:

Input: list1 = [1, 2, 3, 4, 5], list2 = [6, 7, 8, 9, 10]
Output:
[(1, 6), (2, 7), (3, 8), (4, 9), (5, 10)]
[1, 2]
[2, 4, 6, 8, 10]
"""

#{
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends

#User function Template for python3
list1 = list(map(int, input().split()))
list2 = list(map(int, input().split()))

# 1. Use zip() to combine multiple lists into a single iterable
########### Write your code below ###############
zipped = zip(list1,list2)# Your code here
########### Write your code above ###############
print(list(zipped))  # Converts to list for display

# 2. Use filter() with lambda function to filter out numbers greater than 2 in list1
########### Write your code below ###############
is_gt_than_2 = lambda x : x<=2
filtered = filter(is_gt_than_2,list1)# Your code here
########### Write your code above ###############
print(list(filtered))

# 3. Using map() with lambda function to multiply each number of list1 by 2
########### Write your code below ###############
mul_by_2 = lambda x : x*2
mapped = map(mul_by_2,list1)# Your code here
########### Write your code above ###############
print(list(mapped))



#{
 # Driver Code Starts.

print('~')
# } Driver Code Ends