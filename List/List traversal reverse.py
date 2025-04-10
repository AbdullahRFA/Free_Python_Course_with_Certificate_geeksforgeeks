# {
# Driver Code Starts
# Initial Template for Python 3

# } Driver Code Ends

# User function Template for python3
def listTraversalReverse(arr):
    # Write your code below

    # for i in range(-1,-len(arr)-1,-1):
    #     print(arr[i],end=' ')
    arr.reverse()
    for x in arr:
        print(x, end=' ')

    # Don't add a new line as it is provided by the driver code


# {
# Driver Code Starts.

def main():
    t = int(input())

    while (t > 0):
        numbers = [int(x) for x in input().strip().split()]

        listTraversalReverse(numbers)
        print()  # New line
        t -= 1

        print("~")


if __name__ == "__main__":
    main()
# } Driver Code Ends