
a, b = 1, 2
fibonacci = []

while a < 4000000:
    fibonacci.append(a)
    a, b = b, a + b
print("Dãy Fibonacci nhỏ hơn 4.000.000 là:")
print(fibonacci)


tong_chan = sum(x for x in fibonacci if x % 2 == 0)

print("\nTổng các số chẵn trong dãy là:", tong_chan)
