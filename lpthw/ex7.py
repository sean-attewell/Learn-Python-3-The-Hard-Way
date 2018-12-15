print("Mary had a little lamb.")
print("Its fleece as white as {}.".format('snow'))
print("And everywhere that Mary went.")
print("." * 10) # What'd that do?

end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

#Watch that comma at the end. Try removing it to see what happens.
print(end1 + end2 + end3 + end4 + end5 + end6, end = ' ')
print(end7 + end8 + end9 + end10 + end11 + end12)

# If you remove the end argument, then cheese and burger appear on
# two different lines

# You're telling python - when you end the print statement, instead of 
# ending it with a new line, end it with a space. 
# You can put any string there instead of the auto new line!
