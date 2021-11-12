def get_bmi(weight, height):
    return weight / (height ** 2)

def get_bmi_grade(bmi):
    if bmi < 18.5:
        return "under"
    elif bmi < 25.0:
        return "normal"
    elif bmi < 30.0:
        return "over"
    else:
        return "obese"

if __name__ == '__main__':
    num_people = int(input("input data:\n"))
    res_lst = []
    while num_people > 0:
        args = input()
        [weight, height] = args.split(" ")
        bmi = get_bmi(float(weight), float(height))
        grade = get_bmi_grade(bmi)
        res_lst.append(grade)
        num_people -= 1
    
    print("answer:")
    for res in res_lst:
        print(res, end=" ")
