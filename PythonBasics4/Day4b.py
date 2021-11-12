# Function 1
def func1(orders):
    get_tpl = lambda lst: (lst[0], lst[2] * lst[3] if (lst[2] * lst [3]) >= 100 else (lst[2] * lst[3]) + 10)
    return list(map(get_tpl, orders))

lst1 = [[34587, 'title1', 4, 40.95], [98762, 'title2', 5, 56.80], [77226, 'title3', 3, 32.95], [88112, 'title4', 3, 24.99]]
lst2 = func1(lst1)
for tpl in lst2:
    print(tpl)

def func2(orders):
    get_tpl = lambda lst: (lst[0], lst[1][1] * lst[1][2] if (lst[1][1] * lst[1][2]) >= 100 else (lst[1][1] * lst[1][2]) + 10)
    return list(map(get_tpl, orders))

lst3 = [[34587, ('title1', 4, 40.95)], [98762, ('title2', 5, 56.80)], [77226, ('title3', 3, 32.95)], [88112, ('title4', 3, 24.99)]]
lst4 = func2(lst3)
for tpl in lst4:
    print(tpl)