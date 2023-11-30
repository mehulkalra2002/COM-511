
def unique_elements(input_list):
# Use a set to store unique elements
unique_set = set(input_list)
# Convert the set back to a list
unique_list = list(unique_set)
return unique_list

# Example usage:
input_list = [1, 2, 3, 3, 4, 5, 5, 6]
result = unique_elements(input_list)

print("Original List:", input_list)
print("List with Unique Elements:", result)

