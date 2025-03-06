"""
Given a string s of single space-separated words. Capitalize the first letter of all words and count the number of the words in the string. Print the line and the number in separate lines with new line character at the end.

Examples:

Input: s = "welcome to the world of geeks"
Output:
Welcome To The World Of Geeks
6
Input: s = "are you enjoying programming"
Output:
Are You Enjoying Programming
4
"""
# {
# Driver Code Starts
# Initial Template for Python 3

# } Driver Code Ends

# User function Template for python3
s = input()

# Your code here
my_list = s.split(' ')
my_list = [word.capitalize() for word in my_list]
my_str = ' '.join(my_list)
length = len(my_list)

print(my_str)
print(length)

# {
# Driver Code Starts.

# } Driver Code Ends