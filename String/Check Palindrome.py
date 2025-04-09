#{
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends

#User function Template for python3
def isPalindrome(s):
    #Your code below
    s = s.lower()
    return s == s[::-1]
    #Remeber to ignore the case when comparing


#{
 # Driver Code Starts.


def main():
    t=int(input())
    while(t>0):
        s=input()
        print(isPalindrome(s))
        t-=1

        print("~")
if __name__ == "__main__":
    main()
# } Driver Code Ends