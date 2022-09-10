s = input('Please, enter the first phrase: ')
t = input('Please, enter the second phrase: ')

anagram = False
if s.lower() == t[::-1].lower():
    anagram = True

print ('The phrases are anagramm:' , anagram)
