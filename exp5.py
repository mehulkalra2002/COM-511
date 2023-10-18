def reverse_kth_row(matrix, k):
    if k < 0 or k >= len(matrix):
        print("Invalid row index")
        return

    matrix[k] = matrix[k][::-1]

# Example usage
if __name__ == "__main__":
    # Example matrix
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    k = 1  # Specify the row index you want to reverse

    print("Original Matrix:")
    for row in matrix:
        print(row)

    reverse_kth_row(matrix, k)

    print("\nMatrix with row", k, "reversed:")
    for row in matrix:
        print(row)
