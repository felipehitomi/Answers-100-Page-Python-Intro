# sum_two_nums.py
import ast
import sys

num1, num2 = sys.argv[1:]
total = ast.literal_eval(num1) + ast.literal_eval(num2)

    # sys.exit(e)
    print(e)
else:
    print(f'{num1} + {num2} = {total}')



types_allowed = (int, float)
if type(num1) not in types_allowed or type(num2) not in types_allowed:
    raise TypeError('Argument should be an integer or a float value')
print(f'{num1} + {num2} = {total}')
