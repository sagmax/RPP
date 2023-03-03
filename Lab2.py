import numpy as np

def input_rand_mas(size):

    return np.random.randint(0, 10, size)

def delete_str(ar, n):

    return np.delete(ar, n, axis=0)

N = input()
M = input()
k = (int(N), int(M))  #кортеж кол-ва строк и столбцов, необходимый передать для создания двум. массива
ar1 = input_rand_mas(k)
print(ar1)
num = input()
ar2 = delete_str(ar1, int(num))
print(ar2)
with open("lab2.txt", "w") as f:
    f.write(
        str(ar1) + "\n\n" + str(ar2))

