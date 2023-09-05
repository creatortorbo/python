list=[]
num = int(input("Enter no. the list:"))
for i in range(1,num+1):
    element = int(input("Enter Element :"))
    list.append(element)
print("laragest element",max(list),min(list))