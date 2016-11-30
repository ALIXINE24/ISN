phrase=str(input("Quelle est votre phrase?  "))
clef=str(input("Quelle est la clef?  "))
phraseC=str("")
v=0
for i in range (0,len(phrase)):
 '''phdec=phdec+clef[i]'''
 if phrase[i] == " ":
  phraseC=phraseC+" "
 else:
  phraseC=phraseC+clef[v%(len(clef))]
  v=v+1
print(phraseC)
lettre +lettre = lettre codée+1
