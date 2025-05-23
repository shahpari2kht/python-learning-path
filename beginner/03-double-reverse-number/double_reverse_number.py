xyz=int(input())
t= str(xyz%10)
a= xyz//10
o= str(a%10)
p= str(xyz//100)
top=int(t+o+p)
print(top*2)
