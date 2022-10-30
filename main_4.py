Frutti=['mela', 'pera', 'fragola', 'lampone', 'banana']  
for x in Frutti:print(x)                                    #con il comando for possiamo eseguire un insieme di istruzioni, una volta per ogni elemento in una lista
for x in 'ombrello': print(x)                               #in questo caso si possono stampare le lettere delle parole tra virgolette
Auto=['mercedes', 'ferrari', 'lamborghini', 'audi']
for x in Auto:
  print(x)
  if x == "lamborghini":                                    #con il comando break interrompo il ciclo quando il valore x assume quello dato
    break
for x in Auto:
  if x == 'ferrari':                                        #in questo modo ferma il ciclo prima del valore dato
    break  
print(x)
città = ['Milano', 'Roma', 'Napoli']
for x in città:
  if x == 'Roma':
    continue                                                #il comando continue ferma il ciclo quando la variabile assume il valore dato, e riprende dopo
  print(x)
for x in range(0, 35 , 5):                                  #il comando range stampa tutti i numeri da 0 a quello indicato-1, posso aggiungere comandi break, continue,... , aggiungendo un numero dopo quello dato posso indicare il valore di incremento
    print(x)
else: 
    print('finito')                                         #else serve per fare realizzare un comando quando il loop finisce