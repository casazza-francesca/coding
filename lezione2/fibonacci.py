### 2. Sequenza di Fibonacci
##Scrivere una funzione ricorsiva che generi i primi `N` numeri della **sequenza di Fibonacci**. 

from functions import fibonacci

n=int(input('Inserisci un numero: '))

numbers = []

for i in range (1, n + 1):
    numbers.append(fibonacci(i))


print(f'I primi {n} termini della successione di Fibonacci sono {numbers}')