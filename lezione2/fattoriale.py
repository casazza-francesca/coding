### 1. Calcolo del Fattoriale
## Scrivere una funzione che calcoli il **fattoriale** di un numero intero positivo utilizzando un ciclo `for`.

#from functions import fattoriale 
import functions

n = int(input('Inserisci un numero: '))

#result = fattoriale(n)
result = functions.fattoriale(n)

print('Il fattoriale di', n, 'è', result)