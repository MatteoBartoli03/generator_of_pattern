import itertools
import functions
import os
import random

print('------------------ Summary ------------------')
print()
print('Questo programma serve a generare tutti i pattern (combinazioni possibili)')
print('da 3 ad un numero stabilito dall\' utente, puoi inoltre scegliere tra varie opzioni:')
print('Generare un pattern random, scorrere una lista di pattern generati o anche')
print('Visualizzare solo uno specifico pattern, in base alle tue esigenze')
print('premi qualsiasi tasto per iniziare')
print()
print('---------------------------------------------')

input()

while True:
  while True:
    print('Cosa vuoi fare?')
    print('1. genera un elenco completo di pattern')
    print('2. genera un elenco parziale di pattern')
    print('3. mostra un pattern singolo su base paramterica e casuale')
    print('4. esci dal programma')
    while True:
      try:
        res = int(input())
        break;
      except:
        print('\inserisci un valore corretto\n')

    os.system('cls')

    if res == 1:
      patNum = int(input('inserisci la lunghezza del pattern (es.: 7)  '))
      global maxReach
      maxReach = patNum
      os.system('cls')
      pattern = functions.generatePattern(1, patNum)
      functions.printPatterns(pattern)
      input()
      os.system('cls')
    
    elif res == 2:
      os.system('cls')
      print('definisci i parametri dell\'elenco da generare')
      print()
      r1=input('definisci la lunghezza del pattern: ')
      r2=input('definisci il numero di caratteri pieni: ')
      a=functions.partialGeneration(r1, r2)
      functions.printPartialPatterns(a, r1, r2)
      input()
      os.system('cls')
    
    elif res == 3:
      os.system('cls')
      print('definisci i parametri dell\'elenco da generare')
      print()
      r1=input('definisci la lunghezza del pattern: ')
      r2=input('definisci il numero di caratteri pieni: ')
      a=functions.partialGeneration(r1, r2)
      f=functions.ordPartialPatterns(a, r1, r2)
      print(f[0])
      i=0

      while True:
        r = input('cosa vuoi fare?')
        os.system('cls')
        if r.upper() != 'M':
          if r.upper() == 'W':
            if i != len(f)-1:
              i += 1
              print(f[i])
            else:
              i= 0
              print(f[i])
        
          elif r.upper() == 'S':
            if i != 0:
              i -= 1
              print(f[i])
            else:
              i=len(f)-1
              print(f[i])
     
        else:
          os.system('cls')
          break

    else:
      break
  if res == 4:
    break