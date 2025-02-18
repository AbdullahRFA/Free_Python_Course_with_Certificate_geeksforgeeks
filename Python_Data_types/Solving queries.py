"""
Given a dictionary, and a list of queries(keys), you have to find and print the value of each query from the dictionary if present else it prints "None".

Examples:

Input:
dict = {1:"abc", 2: "cde", 3: "fgh"}
query = [2, 3, 4]
Output:
cde
fgh
None


"""
a = list(map(int, input().split()))
b = list(map(str, input().split()))
query = list(map(int, input().split()))
dict = {}
for i in range(len(a)):
    dict[a[i]] = b[i]

ans = []
for key in query:
    ########### Write your code below ###############
    # get value for given key
    val = dict.get(key, "None")
    ########### Write your code above ###############

    # append to ans
    ans.append(val)

# Print ans
print(*ans, sep='\n')

# {
# Driver Code Starts
# Driver Code
# } Driver Code Ends
