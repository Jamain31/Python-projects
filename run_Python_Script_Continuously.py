def func_1():
    print("Function Stuff")

def func_2():
    print("More Function Stuff")

while True:   #This makes it infinite unless you pick "0"!
    print("1. func_1()\n2. func_2()\n3. Exit")
    choice = int(input("Enter a choice (1/2/3): "))
    if choice == 3:
        break
    elif choice == 1:
        func_1()
    elif choice == 2:
        func_2()
    else:
        print("You pushed the wrong button...")
