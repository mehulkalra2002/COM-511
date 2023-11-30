def generate_square_list(n):
    square_list = [i**2 for i in range(1, n+1)]
    return square_list

# Example usage:
try:
    n = int(input("Enter a number: "))
except ValueError:
    print("Invalid input. Please enter a valid number.")
    exit()

result = generate_square_list(n)

print("Output:")
print(result)
