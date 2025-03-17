# {
# Driver Code Starts
# Initial Template for Python 3

# } Driver Code Ends

# User function Template for python3

# Write the helloFunction below. It should have one statement
# print("Hello")
# code here
def helloFunction():
    print("Hello")


# {
# Driver Code Starts.


def main():
    t = int(input())
    while (t > 0):
        helloFunction()
        t -= 1

        print("~")


if __name__ == "__main__":
    main()
# } Driver Code Ends