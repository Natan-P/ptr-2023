from itertools import accumulate
import sys

file = sys.stdin.read().split("\n")
d, w = map(int, file[0:2])
cols = [[file[y+2][x]
          for y in range(d)]
         for x in range(w)]
# accumulate je uporabljen namesto reduce ker je lepo videti cisto vse korake ko debuggas kodo - razen tega je reduce boljsa izbira tu
food = list(accumulate(
        cols[1:],
        initial=list(map(lambda i: 0 if i == 'B' else -1, cols[0])),
        func=lambda acc, nxt: 
        list(map(
            lambda i: (
                max(acc[max(i-1, 0)], acc[i], acc[min(d-1, i+1)])+(1 if nxt[i]=='H' else 0)
                # ce do vseh pred hrano niti mogu ni pridt, poj nej niti ne razmisla da bi jo pojedu 
                if not all(map(lambda i: i == -1, (acc[max(i-1, 0)], acc[i], acc[min(d-1, i+1)])))
                else -1
            ),
            range(d)
        )) 
))
print(max(food[-1]))
