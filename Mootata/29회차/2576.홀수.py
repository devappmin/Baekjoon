answer = []
nums = []
for i in range(7):
    nums.append(int(input()))

for i in nums:
    if i % 2 != 0:
        answer.append(i)

if answer:
    print(sum(answer), min(answer), sep='\n')
else:
    print(-1)