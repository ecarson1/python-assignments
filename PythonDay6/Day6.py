#Question 1
import numpy as np

if __name__ == '__main__':
    #Question 2
    zeroes = np.zeros(10)
    print(zeroes)

    #Question 3
    ones = np.ones(10)
    print(ones)

    #Question 4
    ones[:] = 5
    print(ones)

    #Question 5
    arr = np.arange(10, 51)
    print(arr)

    #Question 6
    arr2 = np.arange(10, 51, 2)
    print(arr2)

    #Question 7
    mat = np.arange(0, 9).reshape(3,3)
    print(mat)

    #Question 8
    i_matrix = np.eye(3,3)
    print(i_matrix)

    #Question 9
    random_num = np.random.rand()
    print(random_num)