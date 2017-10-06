# Create a function called `unique_characters` that takes a string as parameter
# and returns a list with the unique letters of the given string
# Create basic unit tests for it with at least 3 different test cases
# print(unique_characters("anagram"))
# Should print out:
# ["n", "g", "r", "m"]

def unique_characters(word):
  
    list_of_letters = list(word)
 
    if word is str:
        return True
    elif list_of_letters is not dict or str:
        return True
    else:
        unique_characters = set(list_of_letters)
    return unique_characters
    
# print(unique_characters("anagram"))