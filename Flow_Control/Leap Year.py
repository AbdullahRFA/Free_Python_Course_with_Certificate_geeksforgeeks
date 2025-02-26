"""
Given an integer year. Print "True" (without quotes) if it can represent a leap year, otherwise print "False" (without quotes).

Examples:

Input: year = 2020
Output: True
Explanation: 2020 is leap year as it multilpe of 4 but not a multiple of 100.
Input: year = 2022
Output: False
Explanation: 2022 is not a leap year, as its neither multiple of 400 nor of 4.
"""
#{
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends

#User function Template for python3
# Take year input and print if year is a leap year
year = int(input())
if (year%4==0 and year%100!=0) or (year%400==0):
    print("True")
else:
    print("False")

#{
 # Driver Code Starts.

# } Driver Code Ends