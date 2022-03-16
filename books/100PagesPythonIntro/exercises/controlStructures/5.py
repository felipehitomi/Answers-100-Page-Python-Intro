"""
Write a function that returns the maximum nested depth of curly braces for a given string input. For example,
'{{a+2}*{{b+{c*d}}+e*d}}' should give 4. Unbalanced or wrongly ordered braces like '{a}*b{' and '}a+b{' should return -1.
"""

a = '{{a+2}*{{b+{c*d}}+e*d}}'
b = '{a}*b{'
c = '}a+b{'

def maxDepth(S):
    current_max = 0
    max = 0
    n = len(S)

    for i in range(n):
        if S[i] == '{':
            current_max += 1

            if current_max > max:
                max = current_max
        elif S[i] == '}':
            if current_max > 0:
                current_max -= 1
            else:
                return -1

    if current_max != 0:
        return -1

    return max

print(maxDepth(a))
print(maxDepth(b))
print(maxDepth(c))
