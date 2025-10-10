n = int(input("Enter a number: "))
d = {}  # tạo dictionary rỗng
for i in range(1, n + 1):
    d[i] = i*i
print(d)
