# Three is a crowd part 1
names = ["Tom", "Jeff", "Kim", "Dave"]

def crowd_test(names):
    if(len(names) > 3):
        print("The room is crowded")

crowd_test(names)
names.pop()
crowd_test(names)

# Three is a crowd part 2 
def crowd_test2(names):
    if(len(names) > 3):
        print("The room is crowded")
    else:
        print("The room is not very crowded")
crowd_test2(names)

# six is a mob
names.append("Bob")
names.append("John")
names.append("Jane")

def crowd_test3(names):
    num_ppl = len(names)
    if(num_ppl > 5):
        print("The room is a mob")
    elif(num_ppl <= 5 and num_ppl >= 3):
        print("The room is crowded")
    elif(num_ppl > 0):
        print("The room is not crowded")
    else:
        print("The room is empty")

crowd_test3(names)