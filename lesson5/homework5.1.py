import string
import keyword

s = input()

first_char_is_digit = False
for c in s:
    first_char_is_digit = c.isdigit()
    break

allowed_chars = string.ascii_lowercase + string.digits + "_"

all_allowed = True
for ch in s:
    if ch not in allowed_chars:
        all_allowed = False
        break

print(s and not first_char_is_digit and all_allowed and s not in keyword.kwlist)
