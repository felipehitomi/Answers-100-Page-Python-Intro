nums = [321, 1, -4, 0, 5, 2]

a = [ x*x if (x%2 == 0) else x*x*x for x in nums]
print(a)
