'''Write a Python function that checks whether a passed in string is palindrome or not.

Note: A palindrome is word, phrase, or sequence that reads the same backward as forward, e.g., madam or nurses run.'''

def palindrome(s):
    reversed_word = s[::-1]
    if reversed_word == s:
        return True
    else:
        return False

result = palindrome('helleh')
print(result)

result1 = palindrome('hello')
print(result1)