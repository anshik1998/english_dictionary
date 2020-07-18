import json
from difflib import get_close_matches

inp = json.load(open("data.json"))

word = input("Enter the word to search for: ")

def dictionary(word):
    word = word.lower()
    if word in inp:
        return inp[word]
    elif len(get_close_matches(word, inp.keys())) > 0:
        yn = input(f"Did you mean {get_close_matches(word, inp.keys())[0]}? Enter Y if yes, else enter N for no: ")
        if yn == "Y":
            return inp[get_close_matches(word, inp.keys())[0]]
        elif yn == "N":
            return "Sorry, this word doesn't exist within dictionary. Please double check."
        else:
            return "You've entered wrong entry."
    else:
        return "Sorry, this word doesn't exist within dictionary. Please double check."

outputs = dictionary(word)

if type(outputs) == list:
    for output in outputs:   
        print(output)
else:
    print(outputs)