"""
You are given a number k and a list arr that contains integers. You need to return list of numbers that are less than k.
"""


# {
# Driver Code Starts
# Initial Template for Python 3

# } Driver Code Ends

# User function Template for python3


def lessThan(arr, k):
    ans = []

    # write your code below to append all numbers to ans which are less than k
    for x in arr:
        if x < k:
            ans.append(x)

    return ans


# {
# Driver Code Starts.

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        numbers = numbers = [int(x) for x in input().strip().split()]
        k = int(input())

        ans = lessThan(numbers, k)
        print(*ans)
        print("~")
# } Driver Code Ends