
keys = input("Nhập danh sách khóa, cách nhau bằng dấu cách: ").split()
values = input("Nhập danh sách giá trị, cách nhau bằng dấu cách: ").split()
tu_dien = dict(zip(keys, values))
print("Từ điển sau khi kết nối hai danh sách là:")
print(tu_dien)
