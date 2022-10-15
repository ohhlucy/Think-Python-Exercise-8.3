#Show an example of a string and empty slice with the word banana

fruit = 'banana'
fruit[:3]
'ban'
fruit = 'banana'
print: fruit [0:5:2]
'bnn'

#Generate a reversed string with a palindrome

def is_palindrome(word):
    return word == word[::-1]

print(is_palindrome('racecar'))
print(is_palindrome('refer'))
print(is_palindrome(''))
print(is_palindrome('a'))