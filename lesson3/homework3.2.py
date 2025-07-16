lst = [1, 2, 3, 4]
if len(lst) > 1:
    lst.insert(0, lst.pop())
print(lst)