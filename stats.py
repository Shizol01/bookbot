def word_count(text):
    words = text.split()
    count = 0 
    for word in words:
        count +=1

    return count


def character_count(text):
    char_dict = {}
    for character in text.lower():
        if character not in char_dict:
            char_dict[character] = 1
        else:
            char_dict[character] += 1

    char_dict = display(char_dict)

    return char_dict



def display(char_dict):
    sort_list = sorted(char_dict.items(), key=lambda item: item[1], reverse=True)
    alpha = []
    for char in sort_list:
        if char[0].isalpha():
            alpha.append(f"{char[0]}: {char[1]}")

    return alpha             