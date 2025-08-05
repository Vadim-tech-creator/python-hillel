import string

s = input("Enter your text: ")
hashtag = '#'
new_word = True
for c in s:
    if c == ' ':
        new_word = True
    elif c in string.punctuation:
        continue
    else:
        if new_word:
            hashtag += c.upper()
            new_word = False
        else:
            hashtag += c.lower()

print(hashtag[:140])