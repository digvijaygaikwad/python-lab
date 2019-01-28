# Name:Digvijay Gaikwad
# Div.:P        Batch:P1
d={}
x=int(input("Enter no of students "))
for i in range(0,x,1):
 print('Profile student no',i+1)
 name=input('Enter name ')
 GRno=int(input('Enter Gr no '))
 Branch=input('Enter branch ')
 d[GRno]=(name,Branch)
print(d)
