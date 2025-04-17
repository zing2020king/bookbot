import sys
from stats import get_num_words, count_characters, sorted_character_count

def get_book_text(filepath):
  with open(filepath, 'r', encoding='utf-8') as f:
    return f.read()
  
def main():
  if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

  path = sys.argv[1]
  book_text = get_book_text(path)
  num_words = get_num_words(book_text)
  char_counts = count_characters(book_text)
  sorted_chars = sorted_character_count(char_counts)
  
  print("============ BOOKBOT ============")
  print({f"Analyzing book found at {path}..."})
  print("---------- Words Count ----------")
  print(f"Found {num_words} total words")
  print("-------- Character Count --------")

  for item in sorted_chars:
    print(f"{item['char']}: {item['count']}")

main()