fibList = []

a, b = 0, 1
while a < 4000000:
  a, b = b, a+b
  if a <= 4000000:
    fibList.append(a)

total = 0
for i in fibList:
  if i % 2 ==0:
    total +=i

print(total)
