

arr = [9, 2, 1, 4, 6]

if(len(arr) % 2 == 0):
    print("ERROR")
else:
    arr.sort()
    print(arr)
    x = int((len(arr) / 2))
    print(arr[x])
