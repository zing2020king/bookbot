def get_num_words(text):
  words = text.split()
  return len(words)

def count_characters(text):
  text = text.lower() #convert everything to lowecase
  char_counts = {}

  for char in text:
    if char in char_counts:
      char_counts[char] += 1
    else:
      char_counts[char] = 1

  return char_counts
  
def sorted_character_count(char_counts):
  sorted_list = []

  for char, count in char_counts.items():
    if char.isalpha():
      sorted_list.append({"char": char, "count": count})
  sorted_list.sort(key = lambda item : item["count"] , reverse= True)

  return sorted_list