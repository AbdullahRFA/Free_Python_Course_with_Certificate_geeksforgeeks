# {
# Driver Code Starts
# Initial Template for Python 3

# } Driver Code Ends

# User function Template for python3

def alphabets(c1, c2):
    # Code below to print alphabets from c1 to c2
    # Don't provide a new line after printing
    for x in range(ord(c1), ord(c2) + 1):
        print(chr(x), end=' ')


# {
# Driver Code Starts.

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        c1 = input()
        c2 = input()

        alphabets(c1, c2)
        print()  # This provides new line
        print("~")
# } Driver Code Ends