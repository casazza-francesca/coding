#esercizi con cicli di istruzioni - somma di tutti i numeri da uno a N
numero = int(input('Inserisci un numero: '))

totale = 0

# i = 1 
# utilizzando il ciclo while
# while i <= numero: 
#     totale = totale + i 
#     i = i + 1

# utilizzando il ciclo for
for i in range(1, numero + 1):
    totale = totale + i 

print (f'La somma dei numeri fino a {numero} è {totale}')