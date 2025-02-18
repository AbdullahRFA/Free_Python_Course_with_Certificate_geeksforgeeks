"""

Given a tuple arr with distinct elements and an integer x, find the index position of x. Assume to have x in the tuple always. Print the index (0-based).

Examples:

Input: arr = (1, 2, 3, 4, 5), x = 3
Output: 2
Input: arr = (3, 2, 1, 5, 4), x = 5
Output: 3
"""

#{
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

arr = tuple(map(int, input().split()))
x = int(input())

########### Write your code below ###############
# Print the index of x in arr
print(arr.index(x))

########### Write your code above ###############

#{
 # Driver Code Starts.()
# } Driver Code Ends