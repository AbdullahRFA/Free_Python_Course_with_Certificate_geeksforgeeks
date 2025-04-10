# {
# Driver Code Starts
# Initial Template for Python 3

# } Driver Code Ends

# User function Template for python3

def decrementList(arr):
    # Write the code below to decrement the numbers by 1
    ##After decrementing return the list
    # Don't print it here
    res = []
    for x in arr:
        res.append(x - 1)
    return res


# {
# Driver Code Starts.

def main():
    t = int(input())

    while (t > 0):

        numbers = [int(x) for x in input().strip().split()]

        for x in (decrementList(numbers)):
            print(x, end=" ")
        print()
        t -= 1

        print("~")


if __name__ == "__main__":
    main()
# } Driver Code Ends