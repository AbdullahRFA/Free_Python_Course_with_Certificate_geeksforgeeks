"""
You are given a list arr that contains integers.
You need to return average of the non negative integers.
"""


# {
# Driver Code Starts
# Initial Template for Python 3

# } Driver Code Ends

# User function Template for python3

def nonNegativeAverage(arr):
    # Write your code to find average of positive numbers in number list
    sm = 0
    cnt = 0
    for x in arr:
        if x >= 0:
            sm += x
            cnt += 1

    return sm / cnt

    # Return the answer


# {
# Driver Code Starts.

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        numbers = [int(x) for x in input().strip().split()]

        avg = nonNegativeAverage(numbers)
        avg = (int)(avg * 100) / 100.0
        print('%.2f' % avg)
        print("~")
# } Driver Code Ends