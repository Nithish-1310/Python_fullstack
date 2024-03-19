
# Write a Python Program to Find the Factorial of a Number

num = int(input("Enter the number: "))

factorial = 1

if num < 0 :
    print("Factorial does not exist in negative number!")
elif num == 0:
    print(f"Factorial of {num} is : 1")
    
else:
    for i in range(1,num+1):
        factorial = factorial * i
    print(f"Factorial of {num} is : {factorial}")
