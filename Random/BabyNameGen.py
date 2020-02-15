import string, random

# input
letter1_input = input('Choose a letter: "v" for vowels, "c" for consonants and "l" for any other letter: ')
letter2_input = input('Choose a letter: "v" for vowels, "c" for consonants and "l" for any other letter: ')
letter3_input = input('Choose a letter: "v" for vowels, "c" for consonants and "l" for any other letter: ')
letter4_input = input('Choose a letter: "v" for vowels, "c" for consonants and "l" for any other letter: ')
letter5_input = input('Choose a letter: "v" for vowels, "c" for consonants and "l" for any other letter: ')

vowels = 'aeiou'
consonants = 'bcdfghjklmnpqrstvwxyz'
letters = string.ascii_lowercase

def generator():
    if letter1_input == "v":
        letter1 = random.choice(vowels)
    elif letter1_input == "c":
        letter1 = random.choice(consonants)
    elif letter1_input == "l":
        letter1 = random.choice(letters)
    else:
        letter1 = letter1_input

    if letter2_input == "v":
        letter2 = random.choice(vowels)
    elif letter2_input == "c":
        letter2 = random.choice(consonants)
    elif letter2_input == "l":
        letter2 = random.choice(letters)
    else:
        letter2 = letter2_input

    if letter3_input == "v":
        letter3 = random.choice(vowels)
    elif letter3_input == "c":
        letter3 = random.choice(consonants)
    elif letter3_input == "l":
        letter3 = random.choice(letters)
    else:
        letter3 = letter3_input

    if letter4_input == "v":
        letter4 = random.choice(vowels)
    elif letter4_input == "c":
        letter4 = random.choice(consonants)
    elif letter4_input == "l":
        letter4 = random.choice(letters)
    else:
        letter4 = letter4_input

    if letter5_input == "v":
        letter5 = random.choice(vowels)
    elif letter5_input == "c":
        letter5 = random.choice(consonants)
    elif letter5_input == "l":
        letter5 = random.choice(letters)
    else:
        letter5 = letter5_input
    name = letter1.upper() + letter2 + letter3 + letter4 + letter5
    return name

print(generator(), '\n')

print("Other names for your baby: ")
for i in range(10):
    print(generator())