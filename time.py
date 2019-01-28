# Name: Digvijay Gaikwad
# Div: P      Batch:P1
'''Write a Python program to convert seconds into hours,minutes,seconds.'''
x=int(input('Enter time in seconds '))
d=x//86400
r1=x%86400
h=r1//3600
r2=r1%3600
m=r2//60
r3=r2%60
s=r3
print('The total time is ',d,'days ',h,'hours ',m,'minutes ',s,'seconds') 
