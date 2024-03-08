word= input('Enter a string: ')
letter = [*word]
print(letter)

delstr= input('Enter a word to delete: ')
print(type(delstr))
for index in letter:
    if index == delstr:
        letter.remove(delstr)
print(letter)
