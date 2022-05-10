X = Y = 1
NewCom = [[X,",", Y]]

while 1 > 0:
    com = input()
    if com == "":
        break

    C, n = (com.split(","))
    n = int(n)

    for i in range(0, n):
        if C == 'R':
            X += 1
        if C == 'L':
            X -= 1
        if C == 'D':
            Y += 1
        if C == 'U':
            Y -= 1
        NewCom.append([X,",", Y])

for i in range(0, len(NewCom)):
    for i2 in range(0, len(NewCom[i])):
        print(NewCom[i][i2], end='')
    print()
