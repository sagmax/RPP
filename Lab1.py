import random
import sys

try:
    size = int(input())
except ValueError:
    print("Ошибка ввода! Введите число")
    sys.exit()
ar = []
for i in range(size):
    ar.append(random.randint(0,10))
print(ar)

def found_id_max(ar):  # функция для нахождения id max числа в списке
    m = ar[0]
    for i in range(1, len(ar)):
        if m < ar[i]:
            m = ar[i]
            id = i
    return id

def found_id_min(ar):   # функция для нахождения id min числа в списке
    m = ar[0]
    for i in range(1, len(ar)):
        if m >= ar[i]:
            m = ar[i]
            id = i
    return id

def change_mas(ar, id1, id2):   # функция для удаления необходимых элементов по условию
    k = 0                       # переменная для подсчета кол-ва удалений элементов
    for i in range(len(ar)):
        if ((i - k) > (id1 - k) and (i - k) < (id2 - k)):
            if ar[i - k] % 3 == 0:
                ar.pop(i - k)
                k = k + 1
    return ar

print(found_id_max(ar))
print(found_id_min(ar))
print(change_mas(ar, found_id_max(ar), found_id_min(ar)))
