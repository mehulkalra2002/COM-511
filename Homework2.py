# Get input from the user
try:
n = int(input("Enter the number of entries: "))
except ValueError:
print("Invalid input. Please enter a valid number.")
exit()

# Create an empty dictionary
my_dict = {}

# Populate the dictionary with user input
for _ in range(n):
name = input("Enter a name: ")
value = int(input("Enter a value: "))
my_dict[name] = value

# Display keys and values
print("\nKeys:")
for key in my_dict:
print(key, end=' ')

print("\nValues:")
for value in my_dict.values():
print(value, end=' ')


