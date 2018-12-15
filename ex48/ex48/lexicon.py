# stuff = input('> ')
# words = stuff.split()

# A tuple is nothing more than a list that you can't modify.

# first_word = ('verb', 'go')
# second_word = ('direction', 'north')
# third_word = ('direction', 'west')
# sentence = [first_word, second_word, third_word]

# You want to take raw input from the user, carve it 
# into words with split, analyze those words to identify their type,
# and finally, make a sentence out of them

# def convert_number(s):
#     try:
#         return int(s)
#     except ValueError:
#         return None

lex = {
    'north' : 'direction',
    'south' : 'direction',
    'east' : 'direction',
    'west' : 'direction',
    'go' : 'verb',
    'kill' : 'verb',
    'eat' : 'verb',
    'the' : 'stop',
    'in' : 'stop',
    'of' : 'stop',
    'bear' : 'noun',
    'princess' : 'noun'
}



def scan(speech):

    words = speech.split()
    translated = []

    try:
        for word in words:
            number = int(word)
            translated.append(('number', number))

        return translated    

    except ValueError:
        for word in words:
            word_type = lex.get(word.lower())

            if word_type == None:
                translated.append(('error', word)) # Keep case on errors as they are
            
            else:
                translated.append((word_type, word.lower()))

        return translated


# print("Welcome to the game. What's occuring?")

# speech = input("> ")

# print(scan(speech))


