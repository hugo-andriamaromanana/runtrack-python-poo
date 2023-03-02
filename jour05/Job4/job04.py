def my_len(arr):
    if arr == []:
        return 0
    else:
        return 1 + my_len(arr[1:])

def my_max(arr):
    if my_len(arr) == 1:
        return arr[0]
    else:
        return max(arr[0], my_max(arr[1:]))

print(my_max([1, 2, 3, 4, 5, 6, 7,30, 8, 9, 10]))