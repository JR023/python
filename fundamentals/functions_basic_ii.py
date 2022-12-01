#1
def countdown(num):
    newArr = []
    for i in range(num,-1, -1):
        newArr.append(i)

    return newArr

print(countdown(5))

#2
def print_and_return(arr):
    if len(arr) != 2:
        return False
    print(arr[0])

    return arr[1]

print(print_and_return([1,2]))

#3
def first_plus_length(arr):
    return arr[0] + len(arr)

print(first_plus_length([1,2,3,4,5]))

#4
def values_greater_than_second(arr):
    if len(arr) < 2:
        return False

    newArr = []
    count = 0
    for num in arr:
        if num > arr[1]:
            newArr.append(num)
            count += 1
    print(count)

    return newArr

print(values_greater_than_second([5,2,3,2,1,4]))
print(values_greater_than_second([3]))

#5
def length_and_value(size, value):
    newArr = []
    for _ in range(size):
        newArr.append(value)
    return newArr

print(length_and_value(4,7))
print(length_and_value(6,2))