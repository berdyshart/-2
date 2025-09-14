n = int(input())
k = int(input())
amount_per_person = int(n/k)
amount_left = n - amount_per_person*k
print(amount_left)