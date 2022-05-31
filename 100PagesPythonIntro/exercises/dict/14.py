nums = [1, 4, 6, 22, 3, 5, 4, 3, 6, 2, 1, 51, 3, 1]

num = {}

for v in nums:
    if num.get(v):
        pass
    else:
        num[v] = num.setdefault(v, 0)

print(list(num))

print(list(dict.fromkeys(nums)))
