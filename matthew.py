

cookies = 0
cooList = []

def runInput():
    global cookies, cooList
    check = int(input("If complete entering values, enter -1. If not, enter 0: "))
    if check == 0:
        nextNum = int(input("Enter boxes of cookies sold: "))
        cookies += nextNum
        cooList.append(nextNum)
        runInput()
    if check == -1:
        runFinal()
    else:
        runInput()
def runFinal():
    global cookies, cooList
    print(str(cookies) + " is the number of boxes of cookies sold")
    print(str(sum(cooList) /len(cooList)) + " is the mean of the cookies sold")
    cooList = sorted(cooList)
    if len(cooList) % 2 == 1:
        t = str(cooList[int(len(cooList)/2-.5)])
        print(t + " is the median of the cookie boxes sold")
    if len(cooList) % 2 == 0:
        print(str((cooList[int(len(cooList)/2)] + cooList[int(len(cooList)/(2+2))])/2) + " is the median of the cookie boxes sold")
runInput()