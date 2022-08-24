n = input()
card_list = [0]*10

for i in n:
    if i == '6' or i == '9':
        if card_list[6] == card_list[9]:
            card_list[6] += 1
        else:
            card_list[9] += 1
    else:
        card_list[int(i)] += 1

print(max(card_list))