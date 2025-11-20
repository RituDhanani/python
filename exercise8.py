numbers=[2,5,6,1,3,4,7,8,9,10]

for i in range(len(numbers)):
    for j in range(0, len(numbers)-i-1):
        if numbers[j]>numbers[j+1]:
            numbers[j],numbers[j+1]=numbers[j+1],numbers[j]
       
       
print(numbers)


