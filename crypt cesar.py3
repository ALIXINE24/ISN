print("Menu")
print("1:cryptage")
print("2:")
x=int(input())
if x==1:
	phrase=str(input("Entrez votre phrase"))
	clef=int(input("Quelle est la clef"))
	a=len(phrase)
	'''nombre de caracteres = a'''
	espace=" "
	alpha="abcdefghijklmnopqrstuvwxyz "
	'''mon alphabet'''
	phraseC=""
	for i in range(0,a,1):
		if phrase[i] == espace:
			phraseC=phraseC+espace
		else:
			v=alpha.find(phrase[i])
			'''v= l'indice dans mon alphabet '''
			phraseC=phraseC+alpha[(v+clef)%26]
	print(phraseC)
