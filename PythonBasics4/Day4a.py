# Question 1
def func():
    print('Hello World')

# func()

# Question 2
def func1(name):
    print(f'My name is {name}')

# func1('Ethan')

# Question 3
def func3(x, y, z):
    if z:
        return x
    else:
        return y

# print(func3("Hello", "Goodbye", False))

# Qusetion 4
def func4(x, y):
    return x * y

# print(func4(5, 10))

# Question 5
def is_even(num):
    return num % 2 == 0

# print(is_even(1))

# Question 6
def greater_than(x, y):
    return x > y

# print(greater_than(2, 1))
# print(greater_than(1, 1))

# Question 7
def sum(*nums):
    total = 0
    for num in nums:
        total += num
    return total

# print(sum(1, 2, 3, 4, 5))

# Question 8
def get_even(*nums):
    lst = []
    for num in nums:
        if num % 2 == 0:
            lst.append(num)
    return lst

# print(get_even(1,2,3,4,5,6))

# Question 9 (assumes first index is even since its 0)
def alternate(word):
    chars = []
    for i in range(len(word)):
        if i % 2 == 0:
            chars.append(word[i].upper())
        else:
            chars.append(word[i].lower())
    return ''.join(chars)

# print(alternate("example"))

# Question 10
def func10(x, y):
    if (x % 2 == 0) and (y % 2 == 0):
        return min(x, y)
    else:
        return max(x, y)

# print(func10(2, 4))
# print(func10(1, 4))

# Question 11
def same_first(word1, word2):
    return word1[0] == word2[0]

# print(same_first("test1", "test2"))
# print(same_first("true", "false")) 

# Question 13 (since we ignored 12)
def func13(word):
    chars = []
    for i in range(len(word)):
        if i == 0 or i == 3:
            chars.append(word[i].upper())
        else:
            chars.append(word[i])
    return "".join(chars)

# print(func13("test"))