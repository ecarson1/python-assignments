# Question 1
s = "Hello World"[-3]
# print(s)

# Question 2
# using slice to get ink from thinker
s = "thinker"[2:-2]
# print(s)

# output of s[1]
s = "hello"
# print(s[1])

# Question 3
s = "Sammy"
# print(s[2:])

# Question 4
s = set("Mississippi")
# print(s)

# Question 5

# helper to determine if char is a letter
def is_chr(letter):
    val = ord(letter)
    return (val >= 65 and val <= 90) or (val >= 97 and val <= 122)

# helper to determine if word is a palindrome
def palin_helper(word):
    start = 0
    end = len(word)-1
    while(start <= end):
        # if char is not a letter than skip it until both ptrs point to letters
        if(not is_chr(word[start])):
            start += 1
        elif(not is_chr(word[end])):
            end -= 1
        elif(word[start] != word[end]):
            return False
        else:
            start += 1
            end -= 1

    return True

def is_palindrome():
    num = input("input data\n")
    i = 0
    result = []
    while(i < int(num)):
        pal = input()
        pal = pal.lower()
        if palin_helper(pal):
            result.append('Y')
        else:
            result.append('N')

        i += 1
    
    for s in result:
        print(s)

is_palindrome()