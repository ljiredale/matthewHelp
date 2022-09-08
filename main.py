classes = [
        "Yoga 1", "Yoga 2", "Children's Yoga", "Prenatal Yoga", "Senior Yoga"
    ]
classcnt = [0, 0, 0, 0, 0]

def printClasses():
    print("\nEnter -1 to finish.")
    for i in range(len(classes)):
        print(str(i + 1) + ". " + classes[i])

def main():
    printClasses()
    inputVal = int(input("Select a class:"))
    if inputVal == -1:
        finished()
    elif inputVal == 0 or inputVal <= -2 or inputVal > 5:
        print("Input a valid number.")
        main()
    else:
        classcnt[inputVal-1] = classcnt[inputVal-1] + 1
        main()
def finished():
    for i in range(len(classes)):
        print("\n" + str(i + 1) + ". " + classes[i] + ": " + str(classcnt[i]))

main()