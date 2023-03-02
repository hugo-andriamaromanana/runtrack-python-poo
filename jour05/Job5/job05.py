def fibonnaci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonnaci(n - 1) + fibonnaci(n - 2)
    
def my_append(arr, n):
    if arr == []:
        return [n]
    else:
        return [arr[0]] + my_append(arr[1:], n)
    
def print_fibonnaci(n):
    if n == 0:
        return []
    else:
        return my_append(print_fibonnaci(n - 1), fibonnaci(n - 1))
    
print(print_fibonnaci(10))

#Source https://www.codewars.com/users/hugo-andriamaromanana/completed_solutions