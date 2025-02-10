N = int(input('Inserisci un numero: '))

numeri_primi = []

for i in range (2, N + 1):
    is_prime = True
    for j in range (2, i):
        if i % j == 0:
            is_prime = False
    if is_prime:
        numeri_primi.append(i)

print(f'I numeri primi fino a {N} sono {numeri_primi}.')