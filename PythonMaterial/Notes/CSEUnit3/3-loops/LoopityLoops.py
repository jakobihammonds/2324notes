mylist = []
for i in range(int(input("How many numbers do you want"))):
    mylist.append(int(input("Number Please: ")))

def Instructions():
    print("Sum of list")
    print(sum(mylist))
    print("Smallest number of list")
    print(min(mylist))
    print("Largest number of list")
    print(max(mylist))
    print("middle number of list")
    print(sum(mylist)/len(mylist))

Instructions()

#print evens between 1 and 100
#for i in range(1,100,2):
#       print(i)
#for i in range(1000,0,50):
 #       print(i)
