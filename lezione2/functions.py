#creazione di una libreria

# definire una funzione: def nome_funzione (variabile)
def is_prime(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

def fattoriale(n):
    tot = 1
    for i in range (1, n+1):
        tot = tot * i
    return tot

def fibonacci(n):
    if n ==1 or n == 2:
        return 1
    return fibonacci(n-1) + fibonacci (n-2)
    # funzione ricorsiva