employees = []
count = 0


def export_emp(employees):
    fopen = open("employeedata.txt", "a")
    for employee in employees:
        for i in employee:
            fopen.write(i+" ")
        fopen.write("\n")
    fopen.close()



def import_emp():
    fname = input("Filename: ")
    temp = []
    fopen = open(fname,"r")
    for line in fopen:
        line = line.strip()
        if len(line) !=0:
            line = line.split()
            temp.append(line)
    fopen.close()
    return temp



def Add_Employee():
    global count
    Employee = []
    count += 1
    print('Enter name of employee:',end='')
    Employee.append(input())
    print('Enter employee SSN:',end='')
    Employee.append(input())
    print('Enter employee phone number:',end='')
    Employee.append(input())
    print('Enter employee email:',end='')
    Employee.append(input())
    print('Enter employee salary: $',end='')
    Employee.append(input())
    employees.append(Employee)


def view_all_Employees(employees):
    for i in employees:
        print('---------------------------- '+i[0]+' -------------------------------')
        print('SSN:', i[1])
        print('Phone:', i[2])
        print('Email:', i[3])
        print('Salary', i[4])
        print('----------------------------------------------------------------------')


def search_Employee(ssn):
    findIndex = 0
    for i in employees:
        if(i[1]==ssn):
            return findIndex
        findIndex+=1
    return-1


def main():
    global count
    global employees


    while(True):
        print("----------------------------- Employee Management System -----------------------------------\n")
        print('Enter -1 to exit')
        print('\nThere are ( ',count,' ) employees in the system.\n')
        print('--------------------------------------------------------------------------------------------\n')
        print('1. Add New Employee\n')
        print('2. View All Employees\n')
        print('3. Search Employee by SSN\n')
        print('4. Add Employee Information\n')
        print('5. Export Employee Information into a text file\n')
        print('6. Import Employee Information from a text file\n')
        print('--------------------------------------------------------------------------------------------\n')
        print('Please Enter Your Option Number: ', end="")


        a =int(input())
        if(a==-1):
            print("\nBye!")
            break


        elif(a==1):
            Add_Employee()
            print()


        elif(a==2):
            view_all_Employees(employees)
            print()


        elif(a==3):
            ssn=input("Enter the SSN to find employee: ")
            empIndex=search_Employee(ssn)
            if(empIndex>=0):
                print("------------------------------ "+employees[empIndex][0]+" ----------------------------")
                print('SSN:',employees[empIndex][1])
                print('Phone:',employees[empIndex][2])
                print('Email:',employees[empIndex][3])
                print('Salary:',employees[empIndex][4])
                print("------------------------------------------------------------------------------------\n")
            else:
                print("Employee with "+ssn+" is not found.\n")


        elif(a==4):
            ssn=input("Enter the SSN to Update Employee: ")
            empIndex=search_Employee(ssn)
            if(empIndex>=0):
                employees[empIndex][0]=input("Enter Update Name: ")
                employees[empIndex][2]=input("Enter Update Phone Number: ")
                employees[empIndex][3]=input("Enter Update Email: ")
                employees[empIndex][4]=input("Enter Update Salary: $")
                print("Employee Information Has Been Updated Successfully.\n")
            else:
                print("Employee with "+ssn+" is not found.\n")


        elif(a==5):
            export_emp(employees)
            print("Data Successfully Exported\n")


        elif(a==6):
            employees.extend(import_emp())
            count = len(employees)
            print("Data Successfully Loaded\n")


        else:
            print('Invalid Output')



main()
