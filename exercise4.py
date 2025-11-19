def fib(n, number={}):
    if n in number: 
        return number[n]
    if n <= 2:
        return 1
    number[n] = fib(n-1, number) + fib(n-2, number)
    return number[n]


print("Fibonacci 8  =", fib(8))   
print("Fibonacci 60 =", fib(60))   
print("Fibonacci 90 =", fib(90))  


number=[22,44,5,67,1,1,2,4,5]
def sum(number):
    if len(number)==0:
        return 0
    else:
        return number[0]+sum(number[1:])
print("Sum of given list number is  =",sum(number))

    