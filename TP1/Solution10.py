print("\nProblem10\n")
# a
def is_prime(n):
    if n < 2:
        return False

    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        d+=1
    return True

numbers = [32, 2, 1, 92, 5, 11]

for n in numbers:
    print(n, "->", is_prime(n))

# b
print("Prime below 50:")
for n in range(2, 50):
    if is_prime(n):
        print(n, end=" ")

count = 0
for n in range(2, 100):
    if is_prime(n):
        count+=1

print("\nThe numbers of prime below 100:", count)

# c
def goldbach(n):
    for i in range(2, n):
        p = n - i

        if is_prime(i) and is_prime(p):
            return i, p
    return None

for n in range(4, 31, 2):
    i, p = goldbach(n)
    print(f"{n} = {i} + {p}")

# d
result = True
for n in range(4, 10001, 2):
    if goldbach(n) is None:
        result = False
        break

print("Goldbach holds for every even number from 4 to 10000:", result)
print("\n")