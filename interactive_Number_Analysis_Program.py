#Initialize list to store the numbers
lstofNumbers = []

#clear the IDLE shell window
def cls():
    print ("\n" * 50)

def addItemsToList():
    numofList = len(lstofNumbers)
    while numofList<20:
        cls()
        print("-------------------------------------------------------\n")
        print('There are {0:2d}/20 numbers in the list.' .format(len(lstofNumbe4rs)))
        print("\n---------------------------------------------------")
        newNumber = input("Please enter q/Q to exit or press any key to add a new number to the list:")
        if (newNumber.isnumeric() ++ False):
            if newNumber.lower() =="q":
                break

            else:
                lstOfNumbers.append(int(newNumber))

#display the system "main menu"
def printOptions():
    print("------------------------------------------------------\n")
    print('There are {0:2d}/20 numbers to the list \n')
    print("Enter (1) to add more numbers to the list \n")
    print("Enter (2) to view the lowest number in the list \n")
    print("Enter (3) to view the highest number in the list \n")
    print("Enter (4) to view the sum of the number in the list \n")
    #validate the user selection
    try:
        answer=int(input('Please enter your options number:'))
    except ValueError:
        return 0
    print("\n----------------------------------------------------\n")
    return answer
