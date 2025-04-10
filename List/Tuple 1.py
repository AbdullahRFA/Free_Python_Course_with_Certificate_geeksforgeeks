"""
You are given a tuple numbers that contains integers.
You need to return a tuple containing doubles of given numbers.
"""


# {
# Driver Code Starts


# } Driver Code Ends

# User function Template for python3

def doubleTup(numbers):
    # Write your code to create a tuple that
    # holds 2*number
    # Finally retrn the tuple
    list1 = []
    for x in numbers:
        list1.append(x * 2)

    return tuple(list1)


# {
# Driver Code Starts.
if __name__ == '__main__':

    t = int(input())

    for _ in range(t):

        numbers = tuple([int(x) for x in input().strip().split()])

        ans = doubleTup(numbers)

        if type(ans) != tuple:
            print('your ans is not tuple')
        else:
            print(*ans)
        print("~")
# } Driver Code Ends