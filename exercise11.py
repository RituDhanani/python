def correct_Arithmetic(arr):
  
    d1 = arr[1] - arr[0]
    d2 = arr[2] - arr[1]
    d = d1 if d1 == d2 else arr[3] - arr[2]


    for i in range(len(arr)):
        correct_value = arr[0] + i * d
        if arr[i] != correct_value:
            arr[i] = correct_value
            break
    return arr



def correct_Geometric(arr):
   
    r1 = arr[1] / arr[0]
    r2 = arr[2] / arr[1]
    r = r1 if r1 == r2 else arr[3] / arr[2]


    for i in range(len(arr)):
        correct_value = int(arr[0] * (r ** i))
        if arr[i] != correct_value:
            arr[i] = correct_value
            break
    return arr

ap = [2, 5, 8, 11, 15, 17]
gp = [3, 6, 12, 24, 22, 96]

correct_ap = correct_Arithmetic(ap)
correct_gp = correct_Geometric(gp)

print("Correct Arithmetic sequence is  =", correct_ap)
print("Correct Geometric sequence is =", correct_gp)    