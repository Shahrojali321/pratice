"""description: To find the area of rectangle"""
def area(value1,value2):
    """To find the area of rectangle"""
    val=value1*value2
    return val
length=int(input("enter the length of rectangle:"))
breadth=int(input("enter the breadth of rectangle:"))
result=area(length,breadth)
print("Area of rectangle:",result)
