
chuoi = input("Nhập một xâu ký tự: ")
ds_tu = chuoi.split()
print("Danh sách các từ sau khi tách bằng split():")
print(ds_tu)
chuoi_moi = "-".join(ds_tu)
print("Xâu mới sau khi nối bằng join():")
print(chuoi_moi)
