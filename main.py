from stats import character_counter
from stats import word_counter
from stats import sort_dictionary
from stats import two_key_two_value
from stats import helper_num
from stats import filter_out
import sys


def get_book_text(bookpath):
    with open(bookpath) as txt:
        return txt.read()


    
def main():
   if len(sys.argv) == 1:
       print("Usage: python3 main.py <path_to_book>")
       sys.exit(1)
   else: 
       bookpath = sys.argv[1]

   read_text = get_book_text(bookpath)
   counted_words = word_counter(read_text)
   counted_characters = character_counter(read_text)
   list_to_sort = two_key_two_value(counted_characters)
   sorted_list = sort_dictionary(list_to_sort)
   filtered_list = filter_out(sorted_list)

   print (f"""============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...
----------- Word Count ----------
Found {counted_words} total words
--------- Character Count ------- """)

        
   for item in filtered_list:
      print (f"{item["char"]}: {item["num"]}")

   print ("============= END ===============")
          
main()


