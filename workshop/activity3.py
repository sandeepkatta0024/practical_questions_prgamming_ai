#dDemonstrate Python's dynamic typing: Assign 10 to a variable, 
# print its type, reassign "hello" to the same variable, and print the new type.
a=10
print(type(a))
a="hello"
print(type(a))

#Read two numbers as input, convert to float, compute their average, 
# and print it formatted to 2 decimal places with an f-string.

a=int(input("enter the first number "))
b=int(input("enter the second number "))

a=float(a)
b=float(b)

print(a)
print(b)

avg=(a+b)/2
print(f"The average of the numbers are {avg:.2f}")
