#{
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends

#User function Template for python3

def reverseString(s):
    #Write your code below to reverse s and return it
    res=""
    for i in s:
        res = i + res
    return res
    # return s[::-1]


#{
 # Driver Code Starts.



def main():
    t=int(input())
    while(t>0):
        s=input()
        print(reverseString(s))
        t-=1

        print("~")
if __name__ == "__main__":
    main()
# } Driver Code Ends