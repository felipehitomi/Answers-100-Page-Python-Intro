"""
Write a function that returns the maximum nested depth of curly braces for a given string input. For example,
'{{a+2}*{{b+{c*d}}+e*d}}' should give 4. Unbalanced or wrongly ordered braces like '{a}*b{' and '}a+b{' should return -1.
"""

a = '{{a+2}*{{b+{c*d}}+e*d}}'
b = '{a}*b{'
c = '}a+b{'

count1 = 0
count2 = 0

for c in a:
    if c == '{':
        count1 += 1
    elif c == '}':
        count2 += 1
print(count1)
print(count2)
