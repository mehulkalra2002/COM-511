def get_unique_words(file_name):
    unique_words = set()

    try:
        with open(file_name, 'r') as file:
            for line in file:
                words = line.strip().split()
                unique_words.update(words)

        unique_words = sorted(unique_words)
        
        for word in unique_words:
            print(word)

    except FileNotFoundError:
        print("File not found.")

# Replace 'file.txt' with the name of your text file
get_unique_words('file.txt')
