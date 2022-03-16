# num_funcs.py
def sqr(n):
    return n * n

def fact(n):
    if n < 0:
        raise TypeError("You should input a positive number")
    try:
        total = 1
        for i in range(2, n+1):
            total *= i
        return total
    except TypeError as e:
        print(f"Input only positive integers, full track: \n'{e}'")

num = 5
print(f'square of {num} is {sqr(num)}')
print(f'factorial of {num} is {fact(num)}')
