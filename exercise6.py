string="QRQSRQRSQRQRSQRQS"
substring="QRQS"

count=0
start=0
while True:
    start=string.find(substring,start)
    if start==-1:
        break
    count+=1
    start+=1
print("The count of overlapping occurrences of substring is =",count)