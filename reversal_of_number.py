"""description: To find the reverse of a number."""
def reverse(value):
    """ To find the reverse of a number"""
    rev=0
    while(value>0):
        rev=(rev*10)+value%10
        value=value//10
    return rev
number=int(input("Enter number:"))
result=reverse(number)
print(f"the reverse of the {number} is {result}")
