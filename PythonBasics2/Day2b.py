# Question 1
stuff = [1, "word", 1.2]
# print(stuff)

# Question 2
nested = [1,1,[1,2]]
# print(nested[2][1])

# Question 3
lst = ['a', 'b', 'c']
# print(lst[1:])

# Question 4
weekdays = {"Monday": 1, "Tuesday": 2, "Wednesday": 3, "Thursday": 4, "Friday": 5}
# print(weekdays)

# Question 5
D = {'k1':[1,2,3]}
# print(D['k1'][1])

#Question 6
lst = [1,[2,3]]
tpl = tuple(lst)
# print(tpl)

# Question 7
dist = set("Mississippi")
# print(dist)

# Question 8
dist.add('X')
# print(dist)

# Question 9
num_set = set([1,1,2,3])
# print(num_set)

# Second set of questions that reuse same numbers as above
# Question 1 
def div_7_not_5():
    for i in range(2000, 3201):
        if((i % 7 == 0) and (i % 5 != 0)):
            print(i, end=",")

# div_7_not_5()

# Question 2
def fact(i):
    if i < 2:
        return 1
    return i * fact(i - 1)

# val = int(input("Enter num to take factorial of: "))
# print(fact(val))

# Question 3
def sqr_dict(n):
    d = dict()
    for i in range(1, n+1):
        d[i] = i * i
    print(d)

#val = int(input("Enter an integer: "))
#sqr_dict(val)

# Question 4
def lst_and_tpl(num_str):
    lst = num_str.split(",")
    print(lst)
    tpl = tuple(lst)
    print(tpl)

#num_str = input("Enter comma seperated string of numbers: ")
#lst_and_tpl(num_str)

# Question 5
class NewString(object):
    def __init__(self):
        self.val = ""

    def get_string(self):
        self.val = input("Enter string: ")

    def print_string(self):
        print(self.val)

#str_obj = NewString()
#str_obj.get_string()
#str_obj.print_string()
