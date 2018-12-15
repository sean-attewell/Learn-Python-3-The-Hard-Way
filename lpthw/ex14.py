from sys import argv

script, user_name, size = argv
# Now if we want to make the prompt something else, we just change it in
# this one spot and rerun the script.
# We've used f-string to make the prompt to type tell you what the script
# You're in is called and your username in brackets. Kind of like
# Powershell does.
prompt = f'{script} ({user_name})> '

print(f"Hi {size} {user_name}, I'm the {script} script.")
print("I'd like to ask you a few questions.")
print(f"Do you like me {user_name}?")
likes = input(prompt)

print(f"Where do you live {user_name}?")
lives = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)

print(f"""
Alright, so you said {likes} about liking me.
You live in {lives}. Not sure where that is.
And you have a {computer} computer. nice.
You're {size}.
""")

# Apparently nobody likes scripts that prompt you! So argv is more 
# common...
# So you want command line arguments to be the main way people interact
# with it rather than prompts

# If you want to convert an input to an integer with int()
# better to do it straight away, rather than within the f string braces
