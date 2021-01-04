import json
from difflib import SequenceMatcher, get_close_matches

data = json.load(open("./data.json"))


def print_not_word_not_found(word):
    return f'{word} is not in our dictionary. Please check the spelling or chose another word, thank you'


def find_word(w):
    word = w.lower()
    meaning = data.get(word)
    if meaning:
        return meaning
    elif len(get_close_matches(word, data.keys(), n=1, cutoff=0.7)) > 0:
        closest_match = get_close_matches(word, data.keys(), n=1, cutoff=0.7)[0]
        yn = input(f"did you mean {closest_match}? [Y/n]")

        while True:
            yn = yn.lower()
            if yn == 'y':
                return data.get(closest_match)
            elif yn == 'n':
                return print_not_word_not_found(word)
            else:
                yn = input(f"did you mean {closest_match}? [Y/n]")
    else:
        return print_not_word_not_found(word)


if __name__ == '__main__':

    answer = input("Enter a word: ")
    output = find_word(answer)
    if type(output) is list:
        [print(definition) for definition in output]
    else:
        print(output)