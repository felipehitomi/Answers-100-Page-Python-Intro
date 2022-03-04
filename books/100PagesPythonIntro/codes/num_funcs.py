# num_funcs.py
"""
This method returns a square and a factorial of a number
num_funcs.sqr()
num_funcs.fact()
"""
def sqr(n):
    try:
        return n * n
    except ValueError:
        print('return a valid number')

def fact(n):
    try:
        total = 1
        for i in range(2, n+1):
            total *= i
        return total
    except ValueError:
        print('return a valid number')

num = 5
print(f'square of {num} is {sqr(num)}')
print(f'factorial of {num} is {fact(num)}')
