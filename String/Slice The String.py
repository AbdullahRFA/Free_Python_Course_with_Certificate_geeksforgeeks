#{
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends

#User function Template for python3

def sliceString(s):
    #Write your code below
    return s[1:len(s)-1]




#{
 # Driver Code Starts.




def main():
    t=int(input())
    while(t>0):
        s=input()
        print(sliceString(s))
        t-=1

        print("~")
if __name__ == "__main__":
    main()
# } Driver Code Ends