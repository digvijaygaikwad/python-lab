#Name:Digvijay Gaikwad
#Div.:P      Batch:P1
'''Write a program to find user entered sequence as a palindrome'''
x=list(input('enter sequence '))
y=x[::-1]
if x==y:
	print('Palindrome is ',x)
else:
	print('not a palindrome')
