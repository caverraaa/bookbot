import sys
from stats import words_counter, chars_counter, sort


def main():
    if len(sys.argv) >= 2:
        text = get_book_text(sys.argv[1])
        num_words = words_counter(text)
        #print (f"Found {num_words} total words")
        chars = chars_counter(text)
        #print(chars)
        final = sort(chars)
        final_string = str()
        for d in final:
            if d["char"].isalpha():
                final_string += f"{d['char']}: {d['num']}\n"
        #print(final_string)

  
        print(f"""
============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...
----------- Word Count ----------
Found {num_words} total words
--------- Character Count -------
{final_string}
============= END ===============
            """ 
        )
    else:
        print(f"Usage: python3 main.py <path_to_book>")
        sys.exit(1)

        




def get_book_text(path_to_file:str) -> str:
    with open(path_to_file) as f:
        contents = f.read()
        return contents





if __name__ == "__main__":
    main()