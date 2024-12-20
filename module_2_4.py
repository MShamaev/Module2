numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for i in numbers[1:]:
    is_prime = True
    for j in range(2, i):
        is_prime = i % j != 0
        if not is_prime:
            not_primes.append(i)
            break
        else:
            continue
    if is_prime:
        primes.append(i)
    else:
        continue
print('Primes:', primes)
print('Not Primes:', not_primes)