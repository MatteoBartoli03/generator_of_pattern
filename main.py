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
      patNum = int(input('inserisci la lunghezza del pattern (es.: 7):  '))
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
      print('inserendo \'x\' al posto del numero di caratteri pieni verranno mostrati tutti i pattern con un numero di caratteri da stabilire con un ulteriore inserimento')
      r1 = input('inserisci il numero di caratteri pieni:  ')
      if r1 == 'x':
        print()
        print('inserendo \'x\' al posto del valore della lunghezza del pattern la lunghezza dei pattern generati la loro lunghezza sarà 10')
        r2=input('definisci la lunghezza del pattern: ')
        if r2 == 'x':
          print()
          a=functions.generatePattern(10, 10)
          functions.printPatterns(a)
          input()
          os.system('cls')
        else:
          a=functions.generatePattern(int(r2), int(r2))
          functions.printPatterns(a)
          input()
          os.system('cls')
      else:
        print()
        print('inserendo \'x\' al posto del valore della lunghezza minima di caratteri, questa sarà 1')
        print('inserendo \'x\' al posto del valore della lunghezza massima di caratteri, questa sarà 10')
        print()
        r2 = input('inserisci la lunghezza minima di caratteri:  ')
        r3 = input('inserisci la lunghezza massima di caratteri:  ')
        if r2 == 'x':
          r2 = '1'
        if r3 == 'x':
          r3 = '10'

        if int(r2) >= int(r3):
          print('hai inserito una lunghezza massima minore o uguale di quella minima per cui quest\'ultima rimarrà invariata, ma quella massima sarà uguale a', int(r2) + 1 )
          r3 == str(int(r2) + 1)

        pattern = functions.generatePattern(int(r2), int(r3))
        functions.printPartialPatterns(pattern, r1)
        input()
        os.system('cls')


      
    elif res == 3:
      r3 = 0
      r4 = 0
      os.system('cls')
      print('definisci i parametri del pattern da generare')
      print()
      print('inserendo \'x\' al posto del valore della lunghezza del pattern la lunghezza del pattern sarà 10')
      r1=input('definisci la lunghezza del pattern: ')
      print()
      print('inserendo \'x\' al posto del numero di caratteri pieni verrà ignorato questo parametro')
      r2=input('definisci il numero di caratteri pieni: ')

      if r1 == 'x':
        if r2 == 'x':
          pass
        elif int(r2) > 5:
          r2 = '5'
          print()
          print('siccome il numero di caratteri pieni è maggiore del numero complessivo di caratteri, il 2 parametro sarà uguale al numero di caratteri')
          input()
      elif r2 == 'x':
        pass
      elif int(r2) > int(r1):
        r2 = str(r1)
        print()
        print('siccome il numero di caratteri pieni è maggiore del numero complessivo di caratteri, il 2 parametro sarà uguale al numero di caratteri')
        input()

      if r2 == 'x':
        r3 = 1
      if r1 == 'x':
        r4 = 1
      a=functions.partialGeneration(r1, r2, r3, r4)
      f=functions.ordPartialPatterns(a, r1, r2)
      print(f[0])
      i=0

      while True:
        print('cosa vuoi fare?')
        print('w - mostra il pattern successivo')
        print('s - mostra il pattern precedente')
        print('m - torna al menu principale')
        r = input()
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