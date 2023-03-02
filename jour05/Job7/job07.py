def drop_to_zero(number):
    if number==0:
        return number
    else:
        print(number)
        return drop_to_zero(number-1)

print(drop_to_zero(20))