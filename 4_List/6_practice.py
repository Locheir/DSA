# List practice Question : 

myList = list()

while(True):
    inp = input("Enter a Number :")
    if inp == "done":
        break
    value = float(inp)
    myList.append(value)

average = sum(myList)/len(myList)

print("Average :",average)