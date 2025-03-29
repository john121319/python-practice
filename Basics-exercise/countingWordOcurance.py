import string

def read_text_from_file(file_path):
    """Reads text from the given file and returns it as a string."""
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def count_words(text):
    """Counts occurrences of each word in the text, excluding stop words."""
    stop_words = {"the", "is", "in", "and", "to", "of", "a", "that", "it", "on", "for", "with", "as", "this", "was", "at", "by", "an", "be"}

    text = text.translate(str.maketrans('', '', string.punctuation)).lower()
    words = text.split()

    word_count = {}
    for word in words:
        if word not in stop_words:
            word_count[word] = word_count.get(word, 0) + 1

    return word_count

def print_word_count(word_count):
    """Prints the word count in a readable format."""
    for word, count in sorted(word_count.items(), key=lambda x: x[1], reverse=True):
        print(f"{word}: {count}")

def main(file_path):
    """Main function to execute the word count program."""
    text = read_text_from_file(file_path)
    word_count = count_words(text)
    print_word_count(word_count)

file_path = "sample_example.txt"
main(file_path)