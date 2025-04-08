def get_num_words(text):
    """
    Counts the number of words in a text.
    :param text: The text to count words in.
    :return: Number of words.
    """
    return len(text.split())

def get_char_frequency(text):
    """
    Counts the frequency of each character in a text, including symbols, numbers, and spaces.
    :param text: The text to count characters in.
    :return: Dictionary with character frequencies.
    """
    frequency = {}
    
    for char in text:
        frequency[char.lower()] = frequency.get(char.lower(), 0) + 1
    return frequency

def sort_on(dict):
    return dict["count"]

def sort_dict(dict):
    
    sorted_list = []
    
    for key, value in dict.items():
        sorted_list.append({"char": key, "count": value})
        
    return sorted(sorted_list, reverse=True, key=sort_on)
    
        
      
            