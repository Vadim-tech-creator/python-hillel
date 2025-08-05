seconds = int(input())
days,rest = divmod(seconds, 86400)
hours,rest = divmod(rest, 3600)
minutes,secs = divmod(rest, 60)

if days % 10 == 1 and days % 100 != 11:
    day_word = "день"
elif days % 10 in [2, 3, 4] and not (11 <= days % 100 <= 14):
    day_word = "дні"
else:
    day_word = "днів"

print(f"{days} {day_word}, {hours:02}:{minutes:02}:{secs:02}")