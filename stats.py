def words_counter(text:str) -> int:
    return len(text.split())

def chars_counter(text:str) -> dict[str, int]:
    chars_dict = {}
    for char in text:
        if char.lower() in chars_dict:
            chars_dict[char.lower()] += 1
        else:
            chars_dict[char.lower()] = 1
    return chars_dict

def sort_on(chars):
    return chars["num"]



def sort(chars: dict[str, int]) -> str:
    final_list = []
    for char in chars:
        final_list.append({"char": char, "num":chars[char]})
    final_list.sort(reverse=True, key=sort_on)
    return final_list

    