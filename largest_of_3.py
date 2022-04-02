"""defination:To find the largest number."""
def largest(value1,value2,value3):
    """To find the largest number."""
    lar=0
    if value1>value2 and value1>value3:
        lar=value1
    if value2>value1 and value2>value3:
        lar=value2
    if value3>value1 and value3>value2:
        lar=value3
    return lar
v1=int(input('enter the 1st nymber:'))
v2=int(input('enter the 2nd number:'))
v3=int(input('enter the 3rd number:'))
result=largest(v1,v2,v3)
print(f"The largest number is: {result} ")