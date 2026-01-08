def factorial(n):
    if n==1:
        return n
    else:
        f= n*factorial(n-1)
        return f
num=int(input("Enter a number"))
print("Factorial of", num, "is:", factorial(num))
