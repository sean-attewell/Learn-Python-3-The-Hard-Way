# String interpolation is a process substituting values of 
# variables into placeholders in a string

# Older Python 2 code uses these formatting characters to do what 
# f-strings do. Try them out as an alternative.

a = "%s there" % 'hi'
print(a)

b = 'We are learning %s %s' % ('Python', '3')
print(b)

c = "We are learning %(lang)s %(ver)s" % {'lang': 'Python', 'ver': '3'}
print(c)

print('\n')
# so here you can use a dictionary to name multiple



# %d Decimal integers (not floating point).
# Old
print('%d %d' % (1, 2))
print('%i %i' % (1, 2))
# New
print('{} {}'.format(1, 2))

print('\n')

# %o is for an octal number. "%o" % 1000 == '1750'

print('%o' % 1000)


print('\n')

# %u Unsigned decimal. "%u" % -1000 == '-1000'
print("%u" % -1000)

print('\n')

# %x Hexadecimal lowercase. "%x" % 1000 == '3e8'
# %X Hexadecimal uppercase. "%X" % 1000 == '3E8'
print("%x" % 1000)
print("%X" % 1000)

print('\n')

# %e Exponential notation, lowercase 'e'. "%e" % 1000 == '1.000000e+03'
# %E Exponential notation, uppercase 'E'. "%E" % 1000 == '1.000000E+03'

print("%e" % 1000)
print("%E" % 1000)

print('\n')

# %f Floating point real number. "%f" % 10.34 == '10.340000'
# %F Same as %f. "%F" % 10.34 == '10.340000'
print("%f" % 10.34)
print("%F" % 10.34)


print('\n')
# %g Either %f or %e, whichever is shorter. "%g" % 10.34 == '10.34'
# %G Same as %g but uppercase. "%G" % 10.34 == '10.34'
# I guess upper case for the E if it goes for that one

print("%g" % 10.34)
print("%G" % 10.34)

print('\n')

# %c Character format. "%c" % 34 == '"'
print("%c" % 34)

print('\n')
# %% A percent sign. "%g%%" % 10.34 == '10.34%'

print("%g%%" % 10.34)

print('\n')

# Repr format (debugging format). - representation
print("%r" % int)
