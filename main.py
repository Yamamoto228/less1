def my_factorial(n):
    temp = 1
    for i in range(1, n+1):
        temp = temp * i
    return temp


print(my_factorial(10))


def fib(n):
    a = 0
    b = 1
    if n == 0:
        return 0
    for i in range(1, n-1):
        b = a+b
        a = b-a
    return b


print(fib(7))


def my_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            print(arr)
            if arr[i]<arr[j]:
                arr[i],arr[j]=arr[j],arr[i]
    return arr


a = [-4, 6, 3, 5, 1, -5]
print(my_sort(a))
