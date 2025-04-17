# {
# Driver Code Starts
# Initial Template for Python 3

# } Driver Code Ends

# User function Template for python3
# Implement Addition class here

class Addition:
    def __init__(self):
        pass

    @staticmethod
    def add(a, b):
        return a + b


# result = Addition.add(a,b)


# {
# Driver Code Starts.

# Example usage:
if __name__ == "__main__":
    t = int(input())
    while t:
        t -= 1
        a = int(input())
        b = int(input())
        result = Addition.add(a, b)
        print(result)
# } Driver Code Ends