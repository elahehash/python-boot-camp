print("welcome to the tip calculator!")
a=input("what was the total bill? $")
b=input("how much bill you want to pay? 10 12 or 15")
c=input("how many people too split the bill?")
p=int(b)/100
z=((float(a)*float(p)+float(a))/float(c))
print("Each person should pay: $",round(z,2))

