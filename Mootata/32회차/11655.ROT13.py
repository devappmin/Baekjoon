from curses.ascii import isalpha

s = input()
answer = ''

for char in s:
    if isalpha(char):
        if ord(char) + 13 > 122:
            answer += chr(96 + ((ord(char) + 13) - 122))
        elif ord(char) + 13 > 90 and ord(char) < 91:
            answer += chr(64 + ((ord(char) + 13) - 90))
        else:
            answer += chr(ord(char) + 13)
    else:
        answer += char

print(answer)