# {
# Driver Code Starts
# Initial Template for Python 3
from tabnanny import check


# } Driver Code Ends

# User function Template for python3

def is_prime(num):
    check = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            check = False
            break
    return check


def next_prime(n):
    num = n + 1
    while True:
        if is_prime(num):
            return num
        num += 1


n = int(input())
print(next_prime(n))

# {
# Driver Code Starts.

# } Driver Code Ends