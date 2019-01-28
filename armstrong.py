# Name: Digvijay Gaikwad
# Div: P         Batch:P1
'''Write a python program to find whether the user entered number is an armstrong number'''
x=int(input('enter a 3 digit value'))
a=x//100
r1=x%100
b=r1//10
r2=r1%10
c=r2
z=a**3+b**3+c**3
if x==z:
	print('Armstrong number')
else:
	print('Not an Armstrong number')
