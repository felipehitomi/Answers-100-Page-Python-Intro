"""
Print all numbers from 1 to 1000 (inclusive) which reads the same in reversed
form in both binary and decimal format. For example, 33 in decimal is 100001
in binary and both of these are palindromic. You can either implement your own
logic or search online for palindrome testing in Python.
"""

for i in range(1,10000):
    numeroParaLista = list(str(i))
    if (numeroParaLista == numeroParaLista[::-1]):
        if (f'{i:b}') == (f'{i:b}')[::-1]:
            print(f"palindronmo achado, numero {i} e binário {(f'{i:b}')}")
