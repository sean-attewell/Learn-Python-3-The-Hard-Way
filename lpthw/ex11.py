# Note that you print before you input.
print("How old are you?", end = ' ')
age = input()
print("How tall are you?", end = ' ')
height = input()
print("How much do you weigh?", end = ' ')
weight = input()

print(f"So, you're {age} old, {height} tall and {weight} heavy.")

# Online showed putting strings in the input function, which do print somehow
# Wonder why they + instead of , here.
name = input("What's your name? ")
print("Nice to meet you " + name + "!")
age2 = input("Your age? ")
print("So, you are already " + str(age2) + " years old, " + name + "!")

# Happy with this
print("What times 2 is 6?", end = ' ')
answer = int(input())
print(f"if I use {answer} we get:", 2 * answer)

# If the user puts in something that's not a number it will have a fit.
# print(">>>> age", repr(age)) could tell you if it's a string or int.
# because it's in quotes that means it's a string
print(">>>> age", repr(age))