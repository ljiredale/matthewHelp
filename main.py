def orderReq():
    for i in range(1):
        orderNum = int(input("Please input your order number: "))
        customerName = input("Please input your name: ")
        woodType = int(input("Enter wood type 1 for oak wood 2 for pine wood: "))
        numberOfCharacters = int(input("Please input number of characters: "))
        colWhite = int(input("Enter number of white colored characters: "))
        colBlack = int(input("Enter number of black colored characters: "))
        colGold = int(input("Enter number of gold colored characters: "))
    runCalc(orderNum, customerName, woodType, colWhite, colBlack, colGold)

def runCalc(oNum, cName, wType, cWhite, cBlack, cGold):
    charge = 30
    if wType == 1:
        charge += 15
    if cWhite + cBlack + cGold > 6:
        charge += (((cWhite + cBlack + cGold)-6)*3)
    if cGold > 0:
        charge += 12
    if cGold > 10 and wType == 2:
        print("Pine wood with more than 10 gold characters")
        print("Order number is " + str(oNum))
        print("Customer's name is " + cName)
        print("Number of characters is " + str((cWhite + cGold + cBlack)))    
        print(charge)
    if cWhite == 5 and wType == 1:
        print("Oak wood with more than 5 white characters")
        print("Order number is " + str(oNum))
        print("Customer's name is " + cName)
        print("Number of characters is " + str((cWhite + cGold + cBlack)))    
        print("Charge is " + str(charge))




orderReq()