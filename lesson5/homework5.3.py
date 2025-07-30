import string

s = input()
hashtag = '#'
new_word = True

for c in s:
    if c in string.punctuation or c ==' ':
        new_word = True
    else:
        if new_word:
            hashtag += c.upper()
            new_word = False
        else:
            hashtag += c.lower()
print(hashtag[:140])