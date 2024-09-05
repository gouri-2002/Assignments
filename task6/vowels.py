

words=["hello","hai","python","apple","eagle"]

#wors starting with vowels

vowels="a","e","i","o","u"

for i in range(0,len(words)):

    if words[i].startswith(vowels):
        print(words[i])