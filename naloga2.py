from math import floor

possible = 0
s = 10000
k1, k2 = 5, 9
for i in range(floor(s/k1)+1):
    if ((s-(i*k1))/k2).is_integer():
        possible += 1
print(possible)
