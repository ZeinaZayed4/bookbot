def num_of_words(text):
    words = text.split()
    return len(words)

def char_count(text):
    text = text.lower()
    counts = {}

    for char in text:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1

    return counts

def sort_on(item):
    return item["num"]

def sort_char_counts(char_dict):
    char_list = [{"char": c, "num": n} for c, n in char_dict.items()]
    char_list.sort(reverse=True, key=sort_on)

    return char_list


