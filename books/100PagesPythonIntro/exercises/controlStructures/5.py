"""
Write a function that returns the maximum nested depth of curly braces for a given string input. For example,
'{{a+2}*{{b+{c*d}}+e*d}}' should give 4. Unbalanced or wrongly ordered braces like '{a}*b{' and '}a+b{' should return -1.
"""

a = '{{a+2}*{{b+{c*d}}+e*d}}'
b = '{a}*b{'
c = '}a+b{'
