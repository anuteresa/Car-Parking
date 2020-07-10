x=[]
print("1 means slot is occupied and 0 means slot is unoccupied")
n= int(input("Length of the parking slot"))
for i in range (0,n):
    k= (input("Enter the slot no"))
    x.append(k)

print(x)

count=0
for k in x:
    if k =="0":
        count+=1

percent= float(count)*(100/n)

print("vaccant=",percent, "%")