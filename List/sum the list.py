# {
# Driver Code Starts
# Initial Template for Python 3

# } Driver Code Ends

# User function Template for python3

def listSum(arr):
    # Just return the sum of the list
    # Don't print here
    return sum(arr)


# {
# Driver Code Starts.


def main():
    t = int(input())

    while (t > 0):
        numbers = [int(x) for x in input().strip().split()]

        print(listSum(numbers))
        t -= 1

        print("~")


if __name__ == "__main__":
    main()
# } Driver Code Ends