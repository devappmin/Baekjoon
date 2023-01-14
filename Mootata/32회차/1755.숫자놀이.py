m, n = map(int, input().split())
dic = {'1':'one', '2':'two', '3':'three', '4':'four', '5':'five', '6':'six', '7':'seven', '8':'eight', '9':'nine', '0':'zero'}
numbers = [str(i) for i in range(m, n + 1)]
num = []

for i in numbers:
    str = ''
    for j in i:
        str += dic[j]
    num.append([''.join(i), str])

num.sort(key=lambda x:x[1])

for i in range(len(num)):
    if i % 10 == 0 and i != 0:
        print()
    print(num[i][0], end=' ')