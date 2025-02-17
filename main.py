def main():
    # Logic to read the file
    with open("books/frankenstein.txt") as f:
        # Writing the contents of the file to a variable
        file_contents = f.read()
        
        # Convert the contents to lowercase
        lower_file_contents = file_contents.lower()
        
        # Initialize a dictionary to store the counts of each alphabet character
        character_counts = {}

        characters = len(file_contents.split())
        
        # Iterate through each character in the contents
        for character in lower_file_contents:
            if character.isalpha():
                if character in character_counts:
                    character_counts[character] += 1
                else:
                    character_counts[character] = 1
        
        print("--- Begin report of books/frankenstein.txt ---")
        print(f"{characters} words found in the document")
        # Print the dictionary with the counts of each alphabet character
        for character, count in character_counts.items():
            print(f"The '{character}' character was found {count} times")
        print("--- End repot ---")
# Calling main to run the program
if __name__ == '__main__':
    main()