# {
# Driver Code Starts
# Initial Template for Python 3

# } Driver Code Ends

# User function Template for python3

def changeCase(s):
    # code here to print capitalized,  and then in the upper case
    print(s.capitalize())
    print(s.upper())


# {
# Driver Code Starts.

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input()

        changeCase(s)
        print("~")
# } Driver Code Ends