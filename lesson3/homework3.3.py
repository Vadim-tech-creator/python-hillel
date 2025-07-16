lst = []

lst_2 = len(lst) // 2
if len(lst) % 2 != 0:
    lst_2 += 1
res = [lst[:lst_2], lst[lst_2:]]

print(res)