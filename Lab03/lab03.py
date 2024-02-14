def empEntries():
    empDict = {}
    while True:
        empName = input("Enter name: ")
        if empName.lower() == "No".lower():
            break
        empSalary = float(input("Enter Salary: "))
        empDict[empName] = empSalary
    print(empDict)

#empEntries()

def createList():
    myList = []
    for i in range(10):
        myList.append(int(input("Enter a number: ")))
    return f"List: {myList},\nLargest number on the list: {getMaxNum(myList)}"

#createList()

def getMaxNum(list):
  
    max = list[0]
    for i in range(len(list)):
        print(i)
        if list[i] > max:
            max = list[i]
    return max        


def celsToFarh():
    celsius = float(input("Enter the celsius temp: "))
    return f"The fahrenhiet temp = {9/5 * celsius + 32}"


print(celsToFarh())


def multiplicationTable():
    count = 1
    x = int(input("Enter a number: "))
    while count <= 10:
        print(f"{x}*{count}={x*count}")
        count+=1

#multiplicationTable()

def repeaters(f):
    def wrapper():
        x = int(input("Enter a nubmer of reptitions "))
        for i in range(x):
            f()
    return wrapper

@repeaters
def hello():
    print("Hello")

hello()
