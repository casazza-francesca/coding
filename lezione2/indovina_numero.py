### 3. Indovina il Numero
#Scrivere un gioco in cui il programma genera un numero casuale tra 1 e 100. L'utente deve indovinare il numero, con suggerimenti forniti ad ogni tentativo ("Troppo alto" o "Troppo basso"). Alla fine, il programma assegna un **indice di fortuna** basato sul numero di tentativi.

# 3. Indovina il Numero
    #Scrivere un gioco in cui il programma genera un numero casuale tra 1 e 100. L'utente deve indovinare il numero, con suggerimenti forniti ad ogni tentativo ("Troppo alto" o "Troppo basso"). Alla fine, il programma assegna un **indice di fortuna** basato sul numero di tentativi.
#importare una standard library
    #random.randint(a,b) numero casuale da 'a' a 'b'

import random

# 1. creare il numero casuale all'inizio all'oscuro dell'utente
n = random.randint(1, 100)

# 2. serve un ciclo while pk deve andare avanti fino a quando l'utente non ha azzeccato 
#     permettere all'utente di inserire un numero
#     condizionale if else per stabilire se il numero ch è stato inserito è < > o = a quello che è ststpo inserito

win = False
t=0
 while win == False:
    guess = int(input('Ciao, ho generato un numero casuale da 1 a 100. Prova a indovinare di che numero si tratta: '))
    t = t + 1
        if guess == n:
        win = True
        print (f'Hai indovinato! Complimenti hai vinto von {t} tentativi')
    elif guess < n:
        print (f'Mi dispiace ma hai sbagliato. Il numero che hai scelto è troppo piccolo. Prova di nuovo:')
    else guess > n:
         print (f'Mi dispiace ma hai sbagliato. Il numero che hai scelto è troppo grande. Prova di nuovo:')
    
# 3.quando l'utente indovina la condizione sarà falsa

# 4. conteggio dei tentativi