print("enter x");
dec = input("enter number in decimal format:");
if dec =='x':
    exit();
else:
    decimal = int(dec);
    print(decimal,"in binary=",bin(decimal));