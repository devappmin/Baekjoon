num = [int(input()) for _ in range(9)]
max_value = max(num)
max_index = num.index(max_value) + 1
print(max_value, max_index, sep='\n')