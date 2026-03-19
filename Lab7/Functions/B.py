a, n = input().split()
a = float(a)
n = int(n)

result = 1
for _ in range(n):
    result *= a

print(result)