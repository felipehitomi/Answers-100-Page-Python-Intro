# sum_two_nums.py
import ast
import sys
from math import prod

try:
    num1 = sys.argv[1:]
except ValueError:
    sys.exit('Error: Please provide exactly two numbers as arguments')
except TypeError:
    sys.exit('Error: Please provide 2 ints')
else:
    #print(f'{num1} + {num2} = {total}')
    num1 = [int(num) for num in num1]
    print(sum(num1))
    print(prod(num1))
    print(round(sum(num1)/len(num1),))
