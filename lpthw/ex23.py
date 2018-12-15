# .decode() raw bytes into strings (such as UTF-8)
# .encode() strings into raw bytes
# Dee Bess

# Raw bytes have no convention to them. They are just sequences of bytes
# with no meaning other than numbers, so you must tell Python to 
# "decode this into a utf string".

import sys
script, input_encoding, error = sys.argv

def main(language_file, encoding, errors):
    line = language_file.readline()

    if line:
        print_line(line, encoding, errors)
        return main(language_file, encoding, errors)

# The readline function will return an empty string when it reaches the
# end of the file and if line simply tests for this empty string. As 
# long as readline gives us something, this will be true, and the code
# under (indented) will run. When this is false, Python 
# will skip the indented lines.

# I then call a separate function to do the actual printing of this line. 
# This simplifies my code and makes it easier for me to understand it.
# Once I know what print_line does I can attach my memory to the name 
# print_line and forget about the details.

# I am then calling main again inside main!
# calling this function at the end of itself would...jump back to the top
# and run it again. That would make it loop.
# The if-statement keeps this function from looping forever.
        
def print_line(line, encoding, errors):
    next_lang = line.strip() # This is a simple stripping of the trailing \n on the line string
    raw_bytes = next_lang.encode(encoding, errors=errors) # look at the trail for passing in the encoding you want
    cooked_string = raw_bytes.decode(encoding, errors=errors)
    # Errors the encode/decode parameter is set to the whatever 'errors' the argument used in the function is

    print(raw_bytes, "<===>", cooked_string)

# cooked string should be the same as next_lang

# Python knows its internal convention, but it has no idea what 
# convention you need. In that case, you must use .encode() to get
# the bytes you need.

languages = open("languages.txt", encoding="utf-8")
# Force the encoding here to be utf-8. Have to do that because
# Powershell defaults to a different encoding

main(languages, input_encoding, error)
# Runs the main function and starts the loop


# The ex23.py script is taking bytes written inside the b'' (byte string) 
# and converting them to the UTF-8 (or other) encoding you specified.
# On the left is the numbers for each byte of the utf-8 (shown in
# hexadecimal), and the right has the character output as actual utf-8. 
# The way to think of this is the left side of <===> is the Python 
# numerical bytes, or the "raw" bytes Python uses to store the string. 
# You specify this with b'' to tell Python this is "bytes". These raw 
# bytes are then displayed "cooked" on the right so you can see the real
# characters in your terminal.

# The method strip() returns a copy of the string in which all chars have 
# been stripped from the beginning and the end of the string 
# (default whitespace characters)
# str = "0000000this is string example....wow!!!0000000";
# print str.strip( '0' )
# > this is string example....wow!!!

# The method encode() returns an encoded version of the string
# Default encoding is the current default string encoding
# errors − This may be given to set a different error handling scheme. 
# The default for errors is 'strict', meaning that encoding errors raise 
# a UnicodeError

# str = "this is string example....wow!!!";
# print "Encoded String: " + str.encode('base64','strict')
# > Encoded String: dGhpcyBpcyBzdHJpbmcgZXhhbXBsZS4uLi53b3chISE=


# In mathematics and computing, hexadecimal (also base 16, or hex) is a 
# positional numeral system with a radix, or base, of 16. It uses sixteen 
# distinct symbols, most often the symbols 0–9 to represent values zero 
# to nine, and A–F (or alternatively a–f) to represent values ten to 
# fifteen

# Hexadecimal numerals are widely used by computer system designers and 
# programmers, as they provide a more human-friendly representation of 
# binary-coded values. Each hexadecimal digit represents four binary 
# digits, also known as a nibble, which is half a byte. For example, a 
# single byte can have values ranging from 0000 0000 to 1111 1111 in 
# binary form, which can be more conveniently represented as 00 to FF in 
# hexadecimal

# Why does the output show some languages (ASCII looking ones) as letters
# on the raw side and not the hex?

# Give it a made up encoding:
# LookupError: unknown encoding: uzzt

# When you want to figure out what's going on you can shrink down the
# size of your test case

# The enter and exit printing guides you to not just what's there
# (by printing the variabels in repr()), but also allows you to follow
# where the program is jumping to. e.g. putting in "Call main",
# "There is a line", "Print line", "call main again", and eventually
# "exit main"

# If you take out the if so it loops forever, you get:
# "RecursionError: maximm recursion depth exceeded"
# Calling the function itself is called recursion
# Eventually you run out of memory calling the variables