n = int(input())
answer = n

for i in range(n):
    string = list(input())
    for idx, c in enumerate(string[:-2]):
        if c != string[idx + 1] and c in string[idx + 1:]:
            answer -= 1
            break

print(answer)