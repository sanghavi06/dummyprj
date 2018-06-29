def Add(x,y):
  return x+y
def Subtract(x,y):
  return x-y
def Multiply(x,y):
  return x*y
def Divide(x,y):
  return x/y

print("Select operation")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("5.Exit")
choice = input("enter choice(1/2/3/4):")
num1 = int(input("enter first number:"))
num2 = int(input("enter second number"))
if choice == '1':
   print(num1,"+",num2,"=",Add(num1,num2))
elif choice == '2':
   print(num1,"-",num2,"=",Subtract(num1,num2))
elif choice == '3':
   print(num1,"*",num2,"=",Multiply(num1,num2))
elif choice == '4':
   print(num1,"/",num2,"=",Divide(num1,num2))
else:
	print("Invalid input")