#{
 # Driver Code Starts
#Initial Template for Python 3
import math


# } Driver Code Ends

#User function Template for python3
def is_prime(n):
    for i in range(2, int(n**0.5)+1):
        if n%i==0:
            return False
    return True


class Solution:
    def printPrimeFactorization(self, n):
        # Your code here
        for i in range(2,n+1):
            if is_prime(i):
                while n%i==0:
                    print(i,end=' ')
                    n//=i

#{
 # Driver Code Starts.

def main():
    T = int(input())
    while (T > 0):

        N = int(input())

        ob = Solution()
        ob.printPrimeFactorization(N)
        print()
        print('~')
        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends