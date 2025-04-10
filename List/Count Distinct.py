# You are given a list arr that contains integers. You need to count distinct integers in list.

# {
# Driver Code Starts
# Initial Template for Python 3

# } Driver Code Ends

# User function Template for python3

def countDistinct(arr):
    # Write your code below to count distinct
    return len(set(arr))
    # Return the output


# {
# Driver Code Starts.

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        numbers = [int(x) for x in input().strip().split()]

        ans = countDistinct(numbers)
        print(ans)
        print("~")
# } Driver Code Ends