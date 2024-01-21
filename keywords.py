def read_word_list(file_path):
    with open(file_path, 'r') as file:
        return set(word.strip().lower() for word in file)

def find_words_in_paragraph(word_list, paragraph):
    found_words = set()
    for word in word_list:
        if word.lower() in paragraph.lower():
            found_words.add(word)
    return found_words

def main():
    word_list_file = "words.txt"
    paragraph_file = "search.txt"

    word_list = read_word_list(word_list_file)

    with open(paragraph_file, 'r') as file:
        paragraph = file.read()

    found_words = find_words_in_paragraph(word_list, paragraph)

    if found_words:
        print("The paragraph contains the following words from the list:")
        print(', '.join(found_words))
    else:
        print("The paragraph does not contain any words from the list.")

if __name__ == "__main__":
    main()
