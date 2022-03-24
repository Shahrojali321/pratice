a=int(input('enter the 1st nymber:'))
b=int(input('enter the 2nd number:'))
c=int(input('enter the 3rd number:'))
largest=0
if a>b and a>c:
    largest=a
if b>a and b>c:
    largest=b
if c>a and c>b:
    largest=c
print(largest)
