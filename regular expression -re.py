# Searching for Patterns in Text

import re

# List of patterns to search for
patterns = ['term1', 'term2']

# Text to parse
text = 'This is a string with term1, but it does not have the other term.'

for pattern in patterns:
    print('Searching for "%s" in:\n "%s"\n' % (pattern, text))

    # Check for match
    if re.search(pattern, text):
        print('Match was found. \n')
    else:
        print('No Match was found.\n')

# Now we have seen that re.search() will take the pattern, scan the text, and then return a Match object. If no pattern is found, None is returned.

# List of patterns to search for
pattern = 'term1'

# Text to parse
text = 'This is a string with term1, but it does not have the other term.'

match = re.search(pattern,text)

print(type(match))

# This Match object returned by the search() method is more than just a Boolean or None,
# it contains information about the match, including the original input string, the regular expression that
# was used, and the location of the match. Let's see the methods we can use on the match object:

# Show start of match
print(match.start())

# Show end
print(match.end())

print('*'*18)
##Split with regular expressions

# Term to split on
split_term = '@'

phrase = 'What is the domain name of someone with the email: hello@gmail.com'

# Split the phrase
print(re.split(split_term,phrase))

print('*'*18)
##Finding all instances of a pattern


# Returns a list of all matches
print(re.findall('match','test phrase match is in middle'))

print('*'*18)
##re Pattern Syntax

def multi_re_find(patterns,phrase):
    '''
    Takes in a list of regex patterns
    Prints a list of all matches
    '''
    for pattern in patterns:
        print('Searching the phrase using the re check: %r' %(pattern))
        print(re.findall(pattern,phrase))
        print('\n')



print('*'*18)
##repition syntax


test_phrase = 'sdsd..sssddd...sdddsddd...dsds...dsssss...sdddd'

test_patterns = [ 'sd*',     # s followed by zero or more d's
                'sd+',          # s followed by one or more d's
                'sd?',          # s followed by zero or one d's
                'sd{3}',        # s followed by three d's
                'sd{2,3}',      # s followed by two to three d's
                ]

multi_re_find(test_patterns,test_phrase)