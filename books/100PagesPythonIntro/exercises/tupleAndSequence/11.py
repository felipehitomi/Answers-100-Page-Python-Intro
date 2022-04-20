odd = (1, 3, 5)(3)
even = (2, 4, 6)
total = 0
for i, j in zip(odd, even):
    total+= (i * j)
print(total)
