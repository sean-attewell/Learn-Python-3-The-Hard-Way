import random
from urllib.request import urlopen
import sys

WORD_URL = "http://learncodethehardway.org/words.txt"
WORDS = []

PHRASES = {
    "class %%%(%%%):":
      "Make a class named %%% that is-a %%%.",
    "class %%%(object):\n\tdef __init__(self, ***)" :
      "class %%% has-a __init__ that takes self and *** params.",
    "class %%%(object):\n\tdef ***(self, @@@)":
      "class %%% has-a function *** that takes self and @@@ params.",
    "*** = %%%()":
      "Set *** to an instance of class %%%.",
    "***.***(@@@)":
      "From *** get the *** function, call it with params self, @@@.",
    "***.*** = '***'":
      "From *** get the *** attribute and set it to '***'."
}

# do they want to drill phrases first
if len(sys.argv) == 2 and sys.argv[1] == "english":
    PHRASE_FIRST = True
else:
    PHRASE_FIRST = False

# load up the words from the website
for word in urlopen(WORD_URL).readlines():
    WORDS.append(str(word.strip(), encoding="utf-8"))
 

def convert(snippet, phrase): # Snippet is key (code), phrase is answer
    class_names = [w.capitalize() for w in 
                   random.sample(WORDS, snippet.count("%%%"))]
    other_names = random.sample(WORDS, snippet.count("***"))
    results = []
    param_names = []

    for i in range(0, snippet.count("@@@")):
        param_count = random.randint(1,3)
        param_names.append(', '.join(
            random.sample(WORDS, param_count)))
            # Appends list to list

    for sentence in snippet, phrase:
        # this is how you duplicate a list or string
        # So result is getting both the question and answer
        result = sentence[:]

        # The below is updating both question and answer to have same word
        # for loop cycling through all blanks, so only need to replace one at a time

        # fake class names
        for word in class_names:
            result = result.replace("%%%", word, 1)
        
        # fake other names
        for word in other_names:
            result = result.replace("***", word, 1)
        
        # fake parameter lists
        for word in param_names:
            result = result.replace("@@@", word, 1)
            
        results.append(result)

        DEBUG = 0
        if DEBUG:
            print("snippet: " , snippet)
            print("phrase: ", phrase)
            print("class names: ", class_names)
            print("other names: " , other_names)
            print("param names: ", param_names)

    return results


# Keep going until they hit CTRL-D
try:
    while True:
        snippets = list(PHRASES.keys()) # .keys() returns a list of all the available keys in the dictionary
        random.shuffle(snippets)
    
        for snippet in snippets:
            phrase = PHRASES[snippet] # Use the key to access the answer and call it phrase
            question, answer = convert(snippet, phrase)
            # Running convert to randomise names in each snippet and phrase
            # assign the results outputs to question and answer


        if PHRASE_FIRST:
            question, answer = answer, question
            # This is a quick and easy way to swap two things
            # so assigning answer to question and question to answer

        print(question)

        input("> ")
        print(f"ANSWER:   {answer}\n\n")
        
    

except EOFError:
    print("\nBye")



# The whole thing didn't work because stuff in the while loop wasn't 
# indented

# Run file on its own or with the argument english

# Part of learning to read code well is to stop placing so much meaning
# on the names used for variables and classes. Too often people will
# read a word like ”Cork” and suddenly get derailed because that word
# will confuse them about the meaning. In the above example, "Cork" is
# just an arbitrary name chosen for a class. Don’t place any other 
# meaning on it, and instead treat it like the patterns I’ve given you.

