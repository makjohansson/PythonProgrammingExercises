import random

lotto_set = set()

while len(lotto_set) < 7:
    num = random.randint(1, 35)
    lotto_set.add(num)

for num in sorted(lotto_set):
    print(num, end=" ")
