#{
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends

#User function Template for python3

#Write the complete argumentFunction below.
#The function should take two arguments a and b
#The function should return a+b
#code here
def argumentFunction(a,b):
    return a+b
#Write the argumentFunction above.


#{
 # Driver Code Starts.


def main():
    t=int(input())
    while(t>0):
        a=int(input())
        b=int(input())
        ans=argumentFunction(a,b)
        t-=1
        print(ans)
        print("~")
if __name__ == "__main__":
    main()
# } Driver Code Ends