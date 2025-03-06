s = input("Enter a sentence: ")

# Split the input string into words
my_list = s.split(' ')

# Capitalize each word in the list
my_list = [word.capitalize() for word in my_list]

# Join the words back into a string with spaces
my_str = ' '.join(my_list)

# Get the number of words in the list
length = len(my_list)

# Print results
print(my_str)
print(length)