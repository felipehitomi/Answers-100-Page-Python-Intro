def sum_nums(*args, initial=0):
    total = initial
    for n in args:
        total += n
    return total


print(sum_nums())
print(sum_nums(3, -8))
print(sum_nums(1, 2, 3, 4, 5))
print(sum_nums(1, 2, 3, 4, 5, initial=5))
#rint(sum_nums(initial=5, 2))
nums = (1, 2)
print(sum_nums(*nums, initial=3))
