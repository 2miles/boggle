def main():
    # Read the list of English words from the file
    with open("words.txt", "r") as file:
        words = file.read().splitlines()

    # Filter the words
    filtered_words = []
    for word in words:
        if not any(char.isupper() or not char.isalpha() for char in word):
            if len(word) >= 3 and len(word) <= 16:
                filtered_words.append(word)

    # Write the filtered words to a new file
    with open("boggle_words.txt", "w") as file:
        for word in filtered_words:
            file.write(word + "\n")


if __name__ == "__main__":
    main()
