"""
You are given a tuple numbers that contains a A.P sequence integer.
You need to calculate the next three sequences of numbers and return the whole sequence in a tuple.
"""


# {
# Driver Code Starts
# Initial Template for Python 3

# } Driver Code Ends

# User function Template for python3

def sequence(tup):
    # code here to return tuple containing whole sequences
    dif = tup[-1] - tup[-2]
    list1 = list(tup)
    for _ in range(3):
        list1.append(list1[-1] + dif)
    return tuple(list1)


# {
# Driver Code Starts.

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):

        numbers = tuple([int(x) for x in input().strip().split()])

        ans = sequence(numbers)

        if type(ans) != tuple:
            print('your ans is not tuple')
        else:
            print(*ans)

        print("~")
# } Driver Code Ends