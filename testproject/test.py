# List and examples of the default VSCode "editor.tokenColorCustomizations" colors (in dark mode at least).
# This example is in Python but the same colors apply to any language.
# Save as a Python (.py) file in VSCode with Dark+ (default dark) color theme to view properly.


print()
# #. Key: textMateRules scope
# 1. comments: 'comment'
# 2. strings: 'string'
# 3. keywords: 'keyword'
# 4. numbers: 'constant.numeric'
# 5. types: 'entity.name.type'
# 6. functions: 'entity.name.function'
# 7. variables: 'variable'
# 8. n/a: 'constant.language' (does not autocomplete for some reason)

# See also:
# https://macromates.com/manual/en/language_grammars#naming-conventions
# https://stackoverflow.com/a/45637405
# https://cdn.discordapp.com/attachments/470168395770363905/887061550454693938/unknown.png
# https://github.com/microsoft/vscode/blob/main/extensions/theme-defaults/themes/dark_vs.json


# 1. Comments (comments: 'comment'), inline or block, are green - #6A9955

# this is a comment


# 2. Strings (strings: 'string') are rusty orange/red - #CE9178

'this is a string'
"""this is a string"""
'''this is a string'''
f'this is a string'
r'this is a string'


# 3. Keywords (keywords: 'keyword') are purple - #C586C0

# while and pass are keywords (https://www.programiz.com/python-programming/keyword-list)
while 0:
    pass


# 4. Numbers (numbers: 'constant.numeric'), int or float, are faded light green - #B5CEA8

1234567890
3.14
12e-9
-17
1.8j


# 5. Types (types: 'entity.name.type') are turquoise - #4EC9B0

int
str
float


class my_custom_type:
    pass


# These feel like functions (https://docs.python.org/3/library/functions.html) but are actually types:
zip
map
super

# 6. Functions (functions: 'entity.name.function') are light yellow/wheat - #DCDCAA


print()

id
abs
bin
input
def this_is_a_function(): pass

# 7. Variables (variables: 'variable') are light blue - #9CDCFE


this_is_a_variable = 0

# 8. Constants (n/a: 'constant.language') are blue - #569CD6

None
True
False


class _:
    def _(): pass

# There may be other common colors this list is missing.
