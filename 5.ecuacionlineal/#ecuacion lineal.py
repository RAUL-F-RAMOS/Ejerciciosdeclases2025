#ecuacion lineal
import os
os.system('cls' if os.name=='nt' else 'clear')

print("ecuacion lineal")
print("aX+b=0> X=-b/a")

a=float(input("a:"))
b=float(input("b:"))

x=-b/a


x=round(x,0)
print("X=",x)