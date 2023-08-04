import sys
file = sys.stdin.read().split("\n")
n = int(file[0])
yum = 0
path = file[2]
last4 = '////'
f = 0
for i in range(int(file[1])):
    if path[i] == '|':
        if last4[1:] != "|||" or last4 == "||||": # ce so ze 4 zaporedne stvari trava, vemo da prejsnje ni pojedla -> eno je ze preskocila, tako da lahko spet zacne
            yum += 1
    elif path[i] == 'R':
        yum += 1
    elif path[i] == 'M':
        if last4[-1] != 'R':
            yum += 1
    if yum == n:
        f = i+1
        break
    last4 = last4[1:] + path[i]

print(f)

