def count_set_bits(num):
    # Convert the number to binary and count the '1' bits
    binary_representation = bin(num)[2:]  # [2:] to remove the '0b' prefix
    return binary_representation.count('1')

# Get input from the user
try:
    number = int(input("Enter an integer: "))
except ValueError:
    print("Invalid input. Please enter a valid integer.")
    exit()

# Call the function to count set bits
result = count_set_bits(number)

# Display the result
print(f"Number of set bits in the binary representation of {number}: {result}")
