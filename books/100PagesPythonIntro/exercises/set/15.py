def has_duplicates(value):
    value1 = value
    value = set(value)
    if len(value1) != len(value):
        return True
    else:
        return False


print(has_duplicates('pip'))
print(has_duplicates((3, 2)))
print(has_duplicates([3, 2, 3.0]))
