bytes = b'Aragon\xc3\xa9s'
words = bytes.decode('utf-8')
print(words)

# OK this works!
# b'' must tell python it's a byte we're assigning to the variable
# We then decode the bytes into a cooked_string
# Still not sure how to import a .txt file as anything other than a string

# Note that there is only one letter in hex because it has an accent
