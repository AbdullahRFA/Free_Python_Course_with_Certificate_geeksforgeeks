"""
You are given a string s, you need to print its characters at even indices (index starts at 0).

Examples:

Input: s = "Geeks"
Output: Ges
Explanation: The even indices characters are printed.
Input: s = "DoctorPhenomenal"
Output: DcoPeoea
Explanation: The even indices characters are printed.
"""
#{
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends

#User function Template for python3
# Your code here
s = input()
length = len(s)
for i in range(length):
    if i%2==0:
        print(s[i],end='')

#{
 # Driver Code Starts.

# } Driver Code Ends