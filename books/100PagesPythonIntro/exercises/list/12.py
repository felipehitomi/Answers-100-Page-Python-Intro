def product(a):
    list(a)
    if len(a) == 0:
        raise TypeError('Value should not be empty')
    res=1
    for num in a:
        res = res * num
    print(res)

product([-4, 2.3e12, 77.23, 982, 0b101])
product(range(2,6))
product(())
product(['a', 'b'])
