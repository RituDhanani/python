
for i in range(4):
    for j in range(5):
        if (i==0 and (j==0 or j==1 or j==3 or j==4)) or (i==1 and (j==0 or j==4)):
                print("*",end=" ")
        elif(i==3 and (j==0 or j==4)):
                print("*",end=" ")
        else:
                print("_",end=" ")

    print()

