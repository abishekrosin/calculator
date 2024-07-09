from function import*

print("what do u want to do ?")
print("1 Addition")
print("2 subtraction")
print("3 Multiplication")
print("4 Division")

choice = input("Enter your choice :")

num1 = float(input("enter thr number 1 : "))
num2 = float(input("Enter the number 2 : "))
 
if choice == '1':
    addition(num1,num2)
elif choice =='2':
    subtraction(num1,num2)
elif choice == '3':
    multiplication(num1,num2)
elif choice == '4':
    division(num1,num2)
else:
    print("Invalid choice")