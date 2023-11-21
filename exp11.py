def is_right_triangle(a, b, c):
    sides = [a, b, c]
    sides.sort()

    if sides[0]**2 + sides[1]**2 == sides[2]**2:
        return True
    else:
        return False

def calculate_area(a, b, c):
    s = (a + b + c) / 2
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    return area

def main():
    a = float(input("Enter the length of side a: "))
    b = float(input("Enter the length of side b: "))
    c = float(input("Enter the length of side c: "))

    if is_right_triangle(a, b, c):
        print("The triangle is a right-angled triangle.")
    else:
        print("The triangle is not a right-angled triangle.")

    area = calculate_area(a, b, c)
    print("The area of the triangle is:", area)

if __name__ == "__main__":
    main()
