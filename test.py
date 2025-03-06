n = int(input("Enter a prime number: "))

# Generate prime numbers up to 1000
prime = []
for i in range(2, 1000):
    check = True
    for j in range(2, int(i ** 0.5) + 1):  # Only check divisibility up to sqrt(i)
        if i % j == 0:
            check = False
            break
    if check:
        prime.append(i)

# Ensure 'n' is a prime before searching for the next prime
if n not in prime:
    print(f"{n} is not a prime number. Finding next prime...")
    while n not in prime:
        n += 1  # Increment until we find the next prime

# Get the next prime number after 'n'
idx = prime.index(n)
print(f"The next prime after {n} is: {prime[idx+1]}")