# Name:Digvijay Gaikwad
# Div.:P        Batch:P1
'''write a python program to find whether a 3 digit value is palindrome or not'''
x=int(input('enter a value '))
a=x//100
r1=x%100
b=r1//10
r2=r1%10
z=(r2*100)+(b*10)+(a)
if x==z:
	print x ,'is a palindrome'
else:
	print x ,'is not a palindrome'
