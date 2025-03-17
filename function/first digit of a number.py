#{
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends

#User function Template for python3
def firstDigit(n):
    # Your code here
    while n>=10:
        n//=10
    return n

#{
 # Driver Code Starts.


def main():
    t=int(input())
    while(t>0):
        n=int(input())
        print(firstDigit(n))
        t-=1
        print("~")

if __name__ == "__main__":
    main()
# } Driver Code Ends