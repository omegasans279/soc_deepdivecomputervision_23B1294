def f(arr, n):
    if n == 1: return arr[0]
    return max(arr[n - 1], f(arr, n - 1))

myList = [2, 1, 4, 3]
print(f(myList, len(myList)))
