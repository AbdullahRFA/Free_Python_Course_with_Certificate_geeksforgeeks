#{
 # Driver Code Starts
#Initial Template for Python 3

import math


# } Driver Code Ends

#User function Template for python3
#Complete the below function
def toBinary(n):
    #Your code here
    return bin(n)[2:]

#{
 # Driver Code Starts.

def main():
    T = int(input())
    while (T > 0):
        n = int(input())
        print(toBinary(n))
        print('~')
        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends