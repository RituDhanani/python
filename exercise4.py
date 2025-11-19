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

