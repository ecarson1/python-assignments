# Question 1 Solution
sum = 50 + 50
diff = 100 - 10
print(sum)
print(diff)

# Question 2 Solution
# I was confused as to what this question was asking
print(30,6^6,6**6,6+6+6+6+6+6)

# Question 3 Solution
print("Hello World")
print("Hello World: 10")

# Question 4 Solution
def get_m(p, r, l):
    comp = pow((1 + r/(12 * 100)), l)
    return round((p * comp * (r/1200))/(comp-1))

print(get_m(800000, 6, 103))
