def max_of_three(a, b, c):
    return max(a, b, c)

def is_armstrong(number):
    # Function to check if a number is an Armstrong number
    order = len(str(number))
    temp = number
    sum = 0

    while temp > 0:
        digit = temp % 10
        sum += digit ** order
        temp //= 10

    if number == sum:
        return True
    else:
        return False

# Example usage of max_of_three function
num1 = 15
num2 = 29
num3 = 10

largest = max_of_three(num1, num2, num3)
print(f"The largest number among {num1}, {num2}, {num3} is: {largest}")

# Example usage of is_armstrong function
armstrong_num = 153
non_armstrong_num = 123

if is_armstrong(armstrong_num):
    print(f"{armstrong_num} is an Armstrong number.")
else:
    print(f"{armstrong_num} is not an Armstrong number.")

if is_armstrong(non_armstrong_num):
    print(f"{non_armstrong_num} is an Armstrong number.")
else:
    print(f"{non_armstrong_num} is not an Armstrong number.")
