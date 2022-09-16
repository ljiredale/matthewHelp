'''10 Executive Training School offers typing classes. Each final exam evaluates a
student’s typing speed and the number of typing errors made. Develop the logic
for a program that produces a summary table of each examination’s results.
Each row represents the number of students whose typing speed falls within
the following ranges of words per minute: 0–19, 20–39, 40–69, and 70 or more.
Each column represents the number of students who made different numbers of
typing errors—0 through 6 or more.'''

sL = []
aL = []


def runMain():
    check = int(input("Enter -1 if you want to quit, or 0 to continue: "))
    if check == -1:
        finish()
    if check == 0:
        speed = int(input("Enter typing speed: "))
        acc = int(input("Enter errors made: "))
        sL.append(speed)
        aL.append(acc)
        runMain()
    else:
        runMain()
def finish():
    table = ([[0],[0],[0],[0],[0],[0],[0]],
            [[0],[0],[0],[0],[0],[0],[0]],
            [[0],[0],[0],[0],[0],[0],[0]],
            [[0],[0],[0],[0],[0],[0],[0]])
    for i in range(len(sL)):
        if sL[i] >= 0 and sL[i] <= 19:
            if aL[i] == 0:
                table[0][0][0] = int(table[0][0][0]) + 1
            if aL[i] == 1:
                table[0][1][0] = int(table[0][1][0]) + 1
            if aL[i] == 2:
                table[0][2][0] = int(table[0][2][0]) + 1
            if aL[i] == 3:
                table[0][3][0] = int(table[0][3][0]) + 1
            if aL[i] == 4:
                table[0][4][0] = int(table[0][4][0]) + 1
            if aL[i] == 5:
                table[0][5][0] = int(table[0][5][0]) + 1
            if aL[i] >= 6:
                table[0][6][0] = int(table[0][6][0]) + 1
        if sL[i] >= 20 and sL[i] <= 39:
            if aL[i] == 0:
                table[1][0][0] = int(table[1][0][0]) + 1
            if aL[i] == 1:
                table[1][1][0] = int(table[1][1][0]) + 1
            if aL[i] == 2:
                table[1][2][0] = int(table[1][2][0]) + 1
            if aL[i] == 3:
                table[1][3][0] = int(table[1][3][0]) + 1
            if aL[i] == 4:
                table[1][4][0] = int(table[1][4][0]) + 1
            if aL[i] == 5:
                table[1][5][0] = int(table[1][5][0]) + 1
            if aL[i] >= 6:
                table[1][6][0] = int(table[1][6][0]) + 1
        if sL[i] >= 40 and sL[i] <= 69:
            if aL[i] == 0:
                table[2][0][0] = int(table[2][0][0]) + 1
            if aL[i] == 1:
                table[2][1][0] = int(table[2][1][0]) + 1
            if aL[i] == 2:
                table[2][2][0] = int(table[2][2][0]) + 1
            if aL[i] == 3:
                table[2][3][0] = int(table[2][3][0]) + 1
            if aL[i] == 4:
                table[2][4][0] = int(table[2][4][0]) + 1
            if aL[i] == 5:
                table[2][5][0] = int(table[2][5][0]) + 1
            if aL[i] >= 6:
                table[2][6][0] = int(table[2][6][0]) + 1
        if sL[i] >= 70:
            if aL[i] == 0:
                table[3][0][0] = int(table[3][0][0]) + 1
            if aL[i] == 1:
                table[3][1][0] = int(table[3][1][0]) + 1
            if aL[i] == 2:
                table[3][2][0] = int(table[3][2][0]) + 1
            if aL[i] == 3:
                table[3][3][0] = int(table[3][3][0]) + 1
            if aL[i] == 4:
                table[3][4][0] = int(table[3][4][0]) + 1
            if aL[i] == 5:
                table[3][5][0] = int(table[3][5][0]) + 1
            if aL[i] >= 6:
                table[3][6][0] = int(table[3][6][0]) + 1
    '''
    table = ([[0],[0],[0],[0],[0],[0],[0]],
            [[0],[0],[0],[0],[0],[0],[0]],
            [[0],[0],[0],[0],[0],[0],[0]],
            [[0],[0],[0],[0],[0],[0],[0]])'''
    for i in range(len(table)):
        print(table[i])


        
            


runMain()

