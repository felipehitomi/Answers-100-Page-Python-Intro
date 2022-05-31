def num(n):
    try:
        return print(float(n))
    except TypeError:
        print('TypeError: not a valid input')
    except ValueError:
        print('ValueError: could not convert string to int or float')


num(0x1f)
num(3.32)
num(' \t 52 \t')
num('3.982e5')
num(['1', '2.3'])
num('foo')
