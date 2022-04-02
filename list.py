"""defination: to find the square of number in the values."""
def sqr(arr):
    """to find the square of number in the values"""

    for i in range(len(arr)):
        arr[i]=arr[i]**2

    return arr

input=list(map(int,input("Enter the values with spaces ").split()))

print("result:",sqr(input))