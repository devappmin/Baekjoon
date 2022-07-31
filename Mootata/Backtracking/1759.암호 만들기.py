l, c = map(int, input().split()) # C개의 문자중 L개로 이루어진 암호
alphabet = sorted(list(input().split()))

def recursive(index, sub_sum):
    if len(sub_sum) >= l:
        a, b = 0, 0
        for i in sub_sum:
            if i in ['a', 'e', 'i', 'o', 'u']:
                a += 1
            else:
                b += 1
        
        if a >= 1 and b >= 2:
            print(''.join(sub_sum))
        return
    
    for i in range(index, c):
        sub_sum.append(alphabet[i])
        recursive(i + 1, sub_sum)
        sub_sum.pop()

recursive(0, [])