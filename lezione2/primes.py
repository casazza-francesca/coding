# per importare una funzione da un altro file
from functions import is_prime

# determinare i numeri primi fino a n
n = int(input('Inserisci un numero: '))

# creazione lsita numeri primi
primes = []
# per definire una lsita, mettere il nome_lista = []

for i in range(2, n + 1):
# inserire una variabile di carattere buleano is_... (variabili del tipo vero/falso)
    if functions.is_prime (i):
        primes.append(i)
# nome_lista.append(x) --> aggiungi x alla lista chiamata nome_lista

print('I numeri primi finon a ', n, 'sono', primes)   
#print(f'I numeri primi fino a {n} sono {primes}.') 