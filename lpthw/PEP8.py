# https://www.python.org/dev/peps/pep-0008/

# hanging indent

# Aligned with opening delimiter.
foo = long_function_name(var_one, var_two,
                         var_three, var_four)

# More indentation included to distinguish this from the rest.
def long_function_name(
        var_one, var_two, var_three,
        var_four):
    print(var_one)

# Hanging indents should add a level.
foo = long_function_name(
    var_one, var_two,
    var_three, var_four)


# No:

# Arguments on first line forbidden when not using vertical alignment.
foo = long_function_name(var_one, var_two,
    var_three, var_four)

# Further indentation required as indentation is not distinguishable.
def long_function_name(
    var_one, var_two, var_three,
    var_four):
    print(var_one)


# This PEP takes no explicit position on how (or whether) to further visually
# distinguish such conditional lines from the nested suite inside the if-statement. 
# Acceptable options in this situation include, but are not limited to:

# No extra indentation.
if (this_is_one_thing and
    that_is_another_thing):
    do_something()

# Add a comment, which will provide some distinction in editors
# supporting syntax highlighting.
if (this_is_one_thing and
    that_is_another_thing):
    # Since both conditions are true, we can frobnicate.
    do_something()

# Add some extra indentation on the conditional continuation line.
if (this_is_one_thing
        and that_is_another_thing):
    do_something()


# The closing brace/bracket/parenthesis on multiline constructs may either line up 
# under the first non-whitespace character of the last line of list, as in:

my_list = [
    1, 2, 3,
    4, 5, 6,
    ]
result = some_function_that_takes_arguments(
    'a', 'b', 'c',
    'd', 'e', 'f',
    )
# or it may be lined up under the first character of the line that starts the
# multiline construct, as in:

my_list = [
    1, 2, 3,
    4, 5, 6,
]
result = some_function_that_takes_arguments(
    'a', 'b', 'c',
    'd', 'e', 'f',
)


# Spaces are the preferred indentation method, not tabs.


# Limit all lines to a maximum of 79 characters.

# For flowing long blocks of text with fewer structural restrictions (docstrings or 
# comments), the line length should be limited to 72 characters.

# Limiting the required editor window width makes it possible to have several files
# open side-by-side, and works well when using code review tools that present the two
# versions in adjacent columns.

# For code maintained exclusively or primarily by a team that can reach agreement on
# this issue, it is okay to increase the nominal line length from 80 to 100 characters
# (effectively increasing the maximum length to 99 characters), provided that comments
# and docstrings are still wrapped at 72 characters.

# In Python code, if you end the line with a backslash, Python will continue
# the line of code into the next. So:

print 23 + \
x

is the same as:

print 23 + x

# The preferred way of wrapping long lines is by using Python's implied line
# continuation inside parentheses, brackets and braces. Long lines can be broken
# over multiple lines by wrapping expressions in parentheses. These should be used
# in preference to using a backslash for line continuation.

# Backslashes may still be appropriate at times. For example, long, multiple 
# with-statements cannot use implicit continuation, so backslashes are acceptable:



with open('/path/to/some/file/you/want/to/read') as file_1, \
     open('/path/to/some/file/being/written', 'w') as file_2:
    file_2.write(file_1.read())



# Yes: easy to match operators with operands
income = (gross_wages
          + taxable_interest
          + (dividends - qualified_dividends)
          - ira_deduction
          - student_loan_interest)


# Surround top-level function and class definitions with two blank lines.
# Method definitions inside a class are surrounded by a single blank line.

# Imports should usually be on separate lines:

# Yes:
import os
import sys

# No:
import sys, os

# It's okay to say this though:

from subprocess import Popen, PIPE


# Imports should be grouped in the following order:

# Standard library imports.
# Related third party imports.
# Local application/library specific imports.

# You should put a blank line between each group of imports.


# Module level "dunders" (i.e. names with two leading and two trailing underscores)
# such as __all__, __author__, __version__, etc. should be placed after the module
# docstring but before any import statements except from __future__ imports. 
# Python mandates that future-imports must appear in the module before any other code
# except docstrings:

"""This is the example module.

This module does stuff.
"""

from __future__ import barry_as_FLUFL

__all__ = ['a', 'b', 'c']
__version__ = '0.1'
__author__ = 'Cardinal Biggles'

import os
import sys


# String Quotes

# In Python, single-quoted strings and double-quoted strings are the same. This
# PEP does not make a recommendation for this. Pick a rule and stick to it. When a
# string contains single or double quote characters, however, use the other one to
# avoid backslashes in the string. It improves readability.

# For triple-quoted strings, always use double quote characters to be consistent with
# the docstring convention in PEP 257.



# Whitespace in Expressions and Statements

# Yes: 
spam(ham[1], {eggs: 2})

# No:  
spam( ham[ 1 ], { eggs: 2 } )

# Yes: 
foo = (0,)

# No:  
bar = (0, )

# Yes: 
spam(1)

# No:  
spam (1)

# Yes: 
dct['key'] = lst[index]

# No:  
dct ['key'] = lst [index]


# Yes:

x = 1
y = 2
long_variable = 3

# No:

x             = 1
y             = 2
long_variable = 3


# Avoid trailing whitespace anywhere. Because it's usually invisible, it can 
# be confusing: e.g. a backslash followed by a space and a newline does not count
# as a line continuation marker.

# Always surround these binary operators with a single space on either side: 
# assignment (=), augmented assignment (+=, -= etc.), comparisons (==, <, >, !=, <>,
# <=, >=, in, not in, is, is not), Booleans (and, or, not).


# If operators with different priorities are used, consider adding whitespace around
# the operators with the lowest priority(ies). Use your own judgment; however, never
# use more than one space, and always have the same amount of whitespace on both sides
# of a binary operator.

# Yes:

i = i + 1
submitted += 1
x = x*2 - 1
hypot2 = x*x + y*y
c = (a+b) * (a-b)

# No:

i=i+1
submitted +=1
x = x * 2 - 1
hypot2 = x * x + y * y
c = (a + b) * (a - b)


# Don't use spaces around the = sign when used to indicate a keyword argument or a 
# default parameter value.

# Yes:

def complex(real, imag=0.0):
    return magic(r=real, i=imag)


# Function annotations should use the normal rules for colons and always have
# spaces around the -> arrow if present

# Yes 

def munge(input: AnyStr): ...

def munge() -> AnyStr: ...

# When combining an argument annotation with a default value, use spaces around 
# the = sign (but only for those arguments that have both an annotation and a default).

# Yes

def munge(sep: AnyStr = None): ...
def munge(input: AnyStr, sep: AnyStr = None, limit=1000): ...


# Compound statements (multiple statements on the same line) are generally discouraged.

# Yes:

if foo == 'blah':
    do_blah_thing()
do_one()
do_two()
do_three()

# Rather not:

if foo == 'blah': do_blah_thing()
do_one(); do_two(); do_three()


# Trailing commas are usually optional, except they are mandatory when making a 
# tuple of one element.

# For clarity, it is recommended to surround the latter in (technically redundant)
# parentheses.

# Yes:

FILES = ('setup.cfg',)

# OK, but confusing:

FILES = 'setup.cfg',


# When trailing commas are redundant, they are often helpful when a version control
# system is used, when a list of values, arguments or imported items is expected to be
# extended over time. The pattern is to put each value (etc.) on a line by itself,
# always adding a trailing comma, and add the close parenthesis/bracket/brace on the
# next line. However it does not make sense to have a trailing comma on the same
# line as the closing delimiter (except in the above case of singleton tuples).

# Yes:

FILES = [
    'setup.cfg',
    'tox.ini',
    ]
initialize(FILES,
           error=True,
           )

# No:

FILES = ['setup.cfg', 'tox.ini',]
initialize(FILES, error=True,)


### Comments ###

# You should use two spaces after a sentence-ending period in multi-sentence 
# comments, except after the final sentence.

# Comments should be complete sentences.  The first word should be capitalized, 
# unless it is an identifier that begins with a lower case letter (never alter the
# case of identifiers!).

# Python coders from non-English speaking countries: please write your comments 
# in English, unless you are 120% sure that the code will never be read by people 
# who don't speak your language.

### Block comments ###

# Block comments generally apply to some (or all) code that follows them, and are 
# indented to the same level as that code. Each line of a block comment starts 
# with a # and a single space (unless it is indented text inside the comment).

# Paragraphs inside a block comment are separated by a line containing a single #.

### Inline Comments ###

# Use inline comments sparingly.

# An inline comment is a comment on the same line as a statement.  Inline comments 
# should be separated by at least two spaces from the statement. They should start
# with a # and a single space.

# Inline comments are unnecessary and in fact distracting if they state the obvious. 

# Don't do this:

x = x + 1                 # Increment x

# But sometimes, this is useful:

x = x + 1                 # Compensate for border


### Docstrings ###

# PEP 257 describes good docstring conventions. Note that most importantly, the """
# that ends a multiline docstring should be on a line by itself:

"""Return a foobang

Optional plotz says to frobnicate the bizbaz first.
"""

# For one liner docstrings, please keep the closing """ on the same line.


# Naming Conventions #

# Names that are visible to the user as public parts of the API should follow 
# conventions that reflect usage rather than implementation.

# The following naming styles are commonly distinguished:

# b (single lowercase letter)

# B (single uppercase letter)

# lowercase

# lower_case_with_underscores

# UPPERCASE

# UPPER_CASE_WITH_UNDERSCORES

# CapitalizedWords (or CapWords, or CamelCase -- so named because of the bumpy look of
# its letters [4]). This is also sometimes known as StudlyCaps.

# Note: When using acronyms in CapWords, capitalize all the letters of the acronym. 
# Thus HTTPServerError is better than HttpServerError.

# mixedCase (differs from CapitalizedWords by initial lowercase character!)

# Capitalized_Words_With_Underscores (ugly!)


# _single_leading_underscore: weak "internal use" indicator. E.g. from M import * 
# does not import objects whose name starts with an underscore

# single_trailing_underscore_: used by convention to avoid conflicts with Python 
# keyword, e.g.

Tkinter.Toplevel(master, class_='ClassName')

# __double_leading_underscore: when naming a class attribute, invokes name mangling 
# (inside class FooBar, __boo becomes _FooBar__boo; see below).

# __double_leading_and_trailing_underscore__: "magic" objects or attributes that live
# in user-controlled namespaces. E.g. __init__, __import__ or __file__. 
# Never invent such names; only use them as documented.


### Prescriptive: Naming Conventions ###

# Never use the characters 'l' (lowercase letter el), 'O' (uppercase letter oh), or 
# 'I' (uppercase letter eye) as single character variable names.
# In some fonts, these characters are indistinguishable from the numerals one and zero.
# When tempted to use 'l', use 'L' instead.

# Modules should have short, all-lowercase names. Underscores can be used in the module
# name if it improves readability. Python packages should also have short,
# all-lowercase names, although the use of underscores is discouraged

# Class names should normally use the CapWords convention.
# The naming convention for functions may be used instead in cases where the interface
# is documented and used primarily as a callable.

# Note that there is a separate convention for builtin names: most builtin names are 
# single words (or two words run together), with the CapWords convention used only 
# for exception names and builtin constants.

# Names of type variables introduced in PEP 484 should normally use CapWords pr
# eferring short names: T, AnyStr, Num. It is recommended to add suffixes _co or
# _contra to the variables used to declare covariant or contravariant behavior 
# correspondingly:

from typing import TypeVar

VT_co = TypeVar('VT_co', covariant=True)
KT_contra = TypeVar('KT_contra', contravariant=True)

# Because exceptions should be classes, the class naming convention applies here. 
# However, you should use the suffix "Error" on your exception names (if the 
# exception actually is an error).



# Function and Variable Names #

# Function names should be lowercase, with words separated by underscores as necessary
# to improve readability.

# Variable names follow the same convention as function names.

# mixedCase is allowed only in contexts where that's already the prevailing style 
# (e.g. threading.py), to retain backwards compatibility.


# Function and Method Arguments #

# Always use self for the first argument to instance methods.

# Always use cls for the first argument to class methods.

# If a function argument's name clashes with a reserved keyword, it is generally 
# better to append a single trailing underscore rather than use an abbreviation or
# spelling corruption.

# Comparisons to singletons like None should always be done with is or is not, 
# never the equality operators.

# Also, beware of writing if x when you really mean if x is not None -- e.g. when 
# testing whether a variable or argument that defaults to None was set to some 
# other value. The other value might have a type (such as a container) that could 
# be false in a boolean context!

# Use is not operator rather than not ... is. While both expressions are 
# functionally identical, the former is more readable and preferred.

#Yes:

if foo is not None:

# Always use a def statement instead of an assignment statement that 
# binds a lambda expression directly to an identifier.

# Yes:

def f(x): return 2*x

# No:

f = lambda x: 2*x

# When a resource is local to a particular section of code, use a with
# statement to ensure it is cleaned up promptly and reliably after use. 
# A try/finally statement is also acceptable.

# Be consistent in return statements. Either all return statements in a 
# function should return an expression, or none of them should. If any return
# statement returns an expression, any return statements where no value is
# returned should explicitly state this as return None, and an explicit return
# statement should be present at the end of the function (if reachable).

# Yes:

def foo(x):
    if x >= 0:
        return math.sqrt(x)
    else:
        return None

def bar(x):
    if x < 0:
        return None
    return math.sqrt(x)


# No:

def foo(x):
    if x >= 0:
        return math.sqrt(x)

def bar(x):
    if x < 0:
        return
    return math.sqrt(x)


# Use ''.startswith() and ''.endswith() instead of string slicing to check
# for prefixes or suffixes.

# Yes: 
if foo.startswith('bar'):

# No:
if foo[:3] == 'bar':


# Object type comparisons should always use isinstance() instead of comparing 
# types directly.

# Yes: 
if isinstance(obj, int):

# No:
if type(obj) is type(1):


# For sequences, (strings, lists, tuples), use the fact that 
# empty sequences are false.

# Yes:
if not seq:
if seq:

# No:
if len(seq):
if not len(seq):


# Don't compare boolean values to True or False using ==.

# Yes:   
if greeting:

# No:
if greeting == True:

# Worse:
if greeting is True:
