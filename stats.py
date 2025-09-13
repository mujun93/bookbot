def word_counter(read_text):
    counter = 0
    split_words = read_text.split()
    for word in split_words:
        counter += 1
    return counter

def character_counter(read_text):
    lower_text = read_text.lower()
    characters_and_symbols = {}
    for character in lower_text:
        if character not in characters_and_symbols:
            characters_and_symbols[character] = 1
        elif character in characters_and_symbols:
            characters_and_symbols[character] += 1
    return characters_and_symbols

def two_key_two_value(dic):
    
    dictionary_list = []
    
    for key in dic:
        dictionary = {}
        dictionary["char"] = key
        dictionary["num"] = dic[key]
        dictionary_list.append(dictionary)

    return dictionary_list

def helper_num(item):
    return item["num"]

def sort_dictionary(list):

    list.sort(reverse=True, key=helper_num)
    return list

def filter_out(sorted_list):
    filtered_list = []
    
    for item in sorted_list:
        if item["char"].isalpha():
            filtered_list.append(item)
    return filtered_list