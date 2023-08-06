from functools import reduce
from math import floor

s = 10000
k1, k2 = 5, 9

possible = reduce(lambda acc, n: acc + (1 if ((s-(n*k1))/k2).is_integer() else 0), range(floor(s/k1)+1), 0)

print(possible)
