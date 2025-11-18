numbers=[2,4,5,2,12,44,5,1,2,3]
print("1.Length of list\n2.Display first 3 numbers\n3.Display sum of odd numbers\n4.Number of duplicate numbers\n5.Display list without duplicate numbers")
print("\n")

n=int(input("choose any option "))

if n==1:
    print("length of list is ",len(numbers))
 
elif n==2:
    print("First three number is ",numbers[:3])

elif n==3:
    add = sum(num for num in numbers)
    if n%2!=0:
     print("sum of odd number is ",add)

elif n==4:
   duplicates= sum(numbers.count(n)>1 for n in set(numbers))
  
print("number of duplicate in numbers ",duplicates)

elif n==5:
    print("list without duplicate numberes is ",set(numbers))


   
   
   
   
    

