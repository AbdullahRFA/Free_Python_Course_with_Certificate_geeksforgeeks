#{
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends

#User function Template for python3
def findPattern(s,p):
    return s.find(p)
    #Your code below


#{
 # Driver Code Starts.


def main():
    t=int(input())
    while(t>0):
        s=input()
        p=input()
        print(findPattern(s,p))
        t-=1

        print("~")
if __name__ == "__main__":
    main()
# } Driver Code Ends