def remove_exclamation_marks(s):
    #your code here
    no_punc = s.replace("!", "")
    return no_punc

#Test cases
print(remove_exclamation_marks("Hello World!"))
print(remove_exclamation_marks("Hello World!!!"))
print(remove_exclamation_marks("Hi! Hello!"))
print(remove_exclamation_marks(""))
print(remove_exclamation_marks("Oh, no!!!"))