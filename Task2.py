import numpy as np

ar = np.random.randint(-100, 100, 15)
m = ar[0]
for i in range(1, len(ar)):
    if ar[i] < m:
        m = ar[i]

print(ar)
print(m)
