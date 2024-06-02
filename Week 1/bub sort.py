arr = [4, 3, 2, 1]
for i in range(3):
    for j in range(i+1, 4):
        if arr[i] > arr[j]:
            arr[i], arr[j] = arr[j], arr[i]
print(arr)
