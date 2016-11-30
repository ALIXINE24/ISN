from math import *
def basexenbase10(b,n):
 a=0
 result=""
 print("Entrer la base dans laquelle est le nombre")
 b=int(input())
 print("Quel est le nombre a convertir")
 n=str(input())[::-1]
 e=len(n)
 '''e=nombrre de caractheres de n'''
 for q in range(0,e,+1):
  a=n[q]*pow(b,q)
  s=s+a
  

def base10enbasex(x,y):
 o=0
 result=""
 while pow(x,o)<=y:
  o=o+1
  '''o-1 est egal au rang max'''
 for p in range(o,0,-1):
  for r in range(x-1,-1,-1):
   if y-(r * pow(x,p-1))>=0:
     result=result + str(r)
     y=y-(r * pow(x,p-1))
     break
 return result

def menu():
 print("1.Conversion de la base (x) a la base 10") 
 print("2.Conversion de la base 10 a la base (x)")
 print("3.Conversion de la base (x) a la base (x)")
 valeurmenu=int(input())

 if valeurmenu==2:
  print("Entrer la base voulue(entre la base 2 et 10)")
  x=int(input())
  '''x = la base'''
  print("Entrez le nombre a convertir")
  y=int(input())
  '''y = le nombre a convertir'''
  print (base10enbasex(x,y))
 elif valeurmenu == 1:
  print("Entrer la base dans laquelle est le nombre")
  b=int(input())
  print("Quel est le nombre a convertir")
  n=str(input())[::-1]
  basexenbase10(b,n)
  print (s)
 elif valeurmenu==3:
  print("Entrer la base dans laquelle est le nombre")
  b=int(input())
  print("Quel est le nombre a convertir")
  n=str(input())[::-1]
  basexenbase10(b,n)
  y=s
  print("Entrer la base voulue(entre la base 2 et 10)")
  x=int(input())
  print (base10enbasex(x,y))
menu()
  
  
  
  
  
  
  
  
  
  
  
  
