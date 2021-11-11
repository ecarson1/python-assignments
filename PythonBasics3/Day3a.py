import random
# Question 1
def div_5_7():
    lst = []
    for i in range(1500, 2701):
        if (i % 5 == 0) and (i % 7 == 0):
            lst.append(i)
    return lst
# for i in div_5_7():
   #print(i, end=",")      

# Question 2
def f_to_c(fah):
    cel = round(5/9 * (fah-32))
    print(str(fah) + "°F is " + str(cel) + " in Celsius")

def c_to_f(cel):
    fah = round(cel * 9/5 + 32)
    print(str(cel) + "°C is " + str(fah) + " in Fahrenheit")

#c_to_f(60)
#f_to_c(45)

# Question 3
def guess_num():
    num = random.randint(0, 9)
    guess = -1
    while(guess != num):
        guess = int(input("Guess a number: "))

    print("Well guessed")

#guess_num()

# Question 4
def pattern():
    for i in [1,2,3,4,3,2,1]:
        pat = ""
        for j in range(0, i):
            pat = pat + "*"
            
        print(pat)

#pattern()

# Question 5
def rev_word(word):
    return word[::-1]

#print(rev_word("example word"))

# Question 6
def even_and_odd(nums):
    o_ct = 0
    e_ct = 0
    for i in nums:
        if i % 2 == 0:
            e_ct += 1
        else:
            o_ct += 1

    print("Number of even numbers: " + str(e_ct))
    print("Number of odd numbers: " + str(o_ct))

#nums = (1, 2, 3, 4, 5, 6, 7, 8, 9)
#even_and_odd(nums)

# Question 7
def get_types(arr):
    for i in arr:
        print(str(i) + ", type: " + str(type(i)))

# datalist = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12], {"class":'V', "section":'A'}]
# get_types(datalist)

# Question 8
def print_nums():
    for i in range(0,7):
        if i == 3 or i == 6:
            continue
        print(i, end=" ")

#print_nums()