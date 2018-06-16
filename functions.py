import itertools
import random
import os

def Fattoriale(n):
  n = int(n)
  for i in range((n-1), 0, -1):
    n = n * i
  return n


def partialGeneration(r1, r2):
  r1 = int(r1)
  r2 = int(r2)
  pattern = {}
  for z in range(0, r1+1):
    pattern.update({z : {}})
    for x in range(z+1):
      if x == r1:
        pattern[z].update({'s'+ str(z) : {}})
        for y in range (x+1):
          if y == r2:
            pattern[z]['s' + str(z)].update({'n' + str(y) : {}})
            if y == 0 or y == x:
              pattern[z]['s' + str(z)]['n' + str(y)].update({'i0' : full(x, y)})
            else:
              num = []
              for i in range(x):
                num.append(i+1)
              combs = list(itertools.combinations(num, y))
              for i in range(len(combs)):
                pattern[z]['s' + str(z)]['n' + str(y)].update({'i'+str(i): printCurrentPattern(x, y, i)})
  return pattern

def printPartialPatterns(pattern, r1, r2):
  print()
  print('-------------------------')
  print()
  for z in pattern:
    if z == int(r1):
      print('S' + str(z))
      for x in pattern[z]:
        for y in pattern[z][x]:
          if y == ('n' + str(r2)):
            print('N'+ str(r2))
            print()
            for i in pattern[z][x][y]:
              print (i.upper(), '->', pattern[z][x][y][i])
            print()
            print('-------------------------')
            print()

def ordPartialPatterns(pattern, r1, r2):
  b = []
  for z in pattern:
    if z == int(r1):
      for x in pattern[z]:
        for y in pattern[z][x]:
          if y == ('n' + str(r2)):
            for i in pattern[z][x][y]:
              b.append(pattern[z][x][y][i]) 
  e = len(b)
  c = []
  h = Fattoriale(int(r1))/(Fattoriale(int(r2))*Fattoriale(int(r1)-int(r2)))
  for k in range(int(h)):
    d = random.randint(0, e-1)
    e -= 1
    f = b.pop(d)
    c.append(f)
  return c


def generatePattern(default, patNum):
  pattern = {}
  for z in range (default, patNum+1):
    pattern.update({z : {}})
    for x in range (z+1):
      pattern[z].update({'s'+ str(z) : {}})
      for y in range (x+1):
        pattern[z]['s' + str(z)].update({'n' + str(y) : {}})
        if y == 0 or y == x:
          pattern[z]['s' + str(z)]['n' + str(y)].update({'i0' : full(x, y)})
        else:
          num = []
          for i in range(x):
            num.append(i+1)
          combs = list(itertools.combinations(num, y))
          for i in range(len(combs)):
            pattern[z]['s' + str(z)]['n' + str(y)].update({'i'+str(i): printCurrentPattern(x, y, i)})
  return pattern

def printCurrentPattern(x, y, i):
  ans = ''
  numPos = i
  if y == 1:
    quad = [ '□' ] * x
    quad[i] = '■' 
    for i in range(len(quad)):
      ans += quad[i]
    return ans
  else:
    quad = [ '□' ] * x
    num = []
    for i in range (x):
      num.append(i+1)
    combs = list(itertools.combinations(num, y))
    for i in range(y):
      quad[(combs[numPos][i])-1] = '■'
    for i in range(len(quad)):
      ans += quad[i]
    return ans

def full(x, y):
  if y == x:
    return '■' * x
  else:
    return '□' * x

def printPatterns(pattern):
  print()
  print('-------------------------')
  print()
  for z in pattern:
    print('S' + str(z))
    print()
    for x in pattern[z]:
      for y in pattern[z][x]:
        for i in pattern[z][x][y]:
          print (y.upper(), '-', i.upper(), '->', pattern[z][x][y][i])
    print()
    print('-------------------------')
    print()

def getKeyPrint(var, pattern, maxReach):
  print('Q per uscire')
  key = input('Premi W per il successivo, S per il precedente: ')
  z = var

  if key.lower() == 's':
    z -= 1
  elif key.lower() == 'w':
    z += 1

  if key.lower() == 'q':
    os.system('cls')
    return 'exit'
  if z > maxReach:
    return 'maxReach'
  if z < 3:
    return 'minReach'

  if key.lower() == 'w':
    os.system('cls')
    for some in pattern:
      for x in pattern[some]:
        if x == 's' + str(z):
          for y in pattern[some][x]:
            print()
            for i in pattern[some][x][y]:
              print(y.upper(), '-', i.upper(), '->', pattern[some][x][y][i])
    return 'add'

  elif key.lower() == 's':
    os.system('cls')
    for some in pattern:
      for x in pattern[some]:
        if x == 's' + str(z):
          for y in pattern[some][x]:
            print()
            for i in pattern[some][x][y]:
              print(y.upper(), '-', i.upper(), '->', pattern[some][x][y][i])
    return 'rem'

  else:
    print('Key non riconosciuta, riprova')
    print()