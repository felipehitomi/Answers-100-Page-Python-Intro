fh = open('f1.txt')
nums = fh.read().splitlines()
print(sum(float(i) for i in nums))
fh.close()
