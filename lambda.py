def myfunction(n):
    return lambda a:a+n

number1=myfunction(10)
number2=myfunction(11)

print(number1(5))
print(number2(2))

myfunction()
