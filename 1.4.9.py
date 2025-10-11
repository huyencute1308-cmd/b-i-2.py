
chuoi = input("Nhập một xâu ký tự: ")
dem_ky_tu = {}
for ky_tu in chuoi:
    if ky_tu in dem_ky_tu:
        dem_ky_tu[ky_tu] += 1
    else:
        dem_ky_tu[ky_tu] = 1
print("Số lần xuất hiện của từng ký tự là:")
for ky_tu, so_lan in dem_ky_tu.items():
    print(f"'{ky_tu}': {so_lan}")
