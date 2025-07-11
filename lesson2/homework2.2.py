number = int(input("Enter your number:"))
a = number % 10
b = (number // 10) % 10
c = (number // 100) % 10
d = (number // 1000) % 10
e = number // 10000
reverse = a * 10000 + b * 1000 + c * 100 + d * 10 + e
print(reverse)