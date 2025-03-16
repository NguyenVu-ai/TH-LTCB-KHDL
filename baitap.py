#bai 1 : 
# Nhập số nguyên dương n
n = int(input("Nhập số nguyên dương n: "))
while n <= 0:
    print("Vui lòng nhập số nguyên dương lớn hơn 0.")
    n = int(input("Nhập lại số nguyên dương n: "))

# Tính tổng S4 = 1^2 + 2^2 + ... + n^2
S4 = 0
i = 1
while i <= n:
    S4 += i ** 2
    i += 1

# Tính tổng S5 = 1^3 + 3^3 + 5^3 + ... + (2n+1)^3
S5 = 0
i = 1
while i <= (2 * n + 1):
    S5 += i ** 3
    i += 2

# Tính tổng S6 = 2^4 + 4^4 + 6^4 + ... + (2n)^4
S6 = 0
i = 2
while i <= (2 * n):
    S6 += i ** 4
    i += 2

# Hiển thị kết quả
print(f"Tổng S4 = {S4}")
print(f"Tổng S5 = {S5}")
print(f"Tổng S6 = {S6}")
#bai2:
