from functools import reduce
from math import trunc
import sys
file = sys.stdin.read().split("\n")

path, signs = map(int, file[0].split(" ")[0:3:2])
lim: list[tuple[int, int]]
lim = []
lim.append((0, int(file[0].split(" ")[1])))
# a se vidi da sem se lani naucil haskell?
lim = reduce(lambda acc, s: acc + [tuple(map(int, s.split(" ")[0:2]))], file[1:signs+1], [(int(0), int(file[0].split(" ")[1]))])
limTo: list[tuple[int, int, int]]
limTo = reduce(lambda acc, s: acc[:-1] + [(*acc[-1][:-1], s[0])] + [(*s, path)], lim[1:], [(*lim[0], path)])

hours = reduce(lambda acc, s: acc+max(0, min(s[2], path)-s[0])/s[1], limTo, 0)
hoursTruncated = trunc(hours * 100)/100
print(hoursTruncated)
