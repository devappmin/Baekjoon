n = int(input())
print("int a;\nint *ptr = &a;")
for idx in range(2, n + 1):
    print("int ", "*" * idx, "ptr", idx, " = &ptr", idx - 1 if idx > 2 else "", ";", sep="")