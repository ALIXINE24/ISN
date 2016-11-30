suite = ""
q = str("")
i = str("")
u = str("")

while (suite.find("U") == -1) or (suite.find("=") == -1) or (suite.find("*") == -1) or (suite.find("^") == -1):
	'''on debug l'entrée utilisateur'''
	print("Avec U a l'indice initial ,la valeure de U a l'indice initial et la raison (exemple U2=7*9^2)")
	suite = input("Quelle est la suite?(écrire Un=Un*q^n)  ")

for a in range(suite.find("*")+1,suite.find("^")):
	'''on cherche la raison q'''
	q = q+suite[a]

for a in range(suite.find("U")+1,suite.find("=")):
	'''on cherche l'indice a l'origine'''
	i = i+suite[a]

for a in range(suite.find("=")+1,suite.find("*")):
	'''On cherche le terme a l'origine'''
	u=u+suite[a]

i = int(i)
u = int(u)
q = int(q)
'''on les transforme en int'''

if q>-1 and q<1:
	print("la raison étant comprise entre -1 et 1 alors la suite est convergente vers 0")
	x = int(input("A quelle precision voulez vous que le resultat en rapport avec le terme U(n) soit? 10^"))
	if x<0:
		x = x
	else:
		x = -x
		'''partie debugage entrée utilisateur'''
	n = 0
	s = 100000000000000000000000000000000
	while s<-pow(10,x) or s>pow(10,x):
		n += 1
		s = u*pow(q,n-i)
	'''n=le rang a partir duquelle s est proche a 10^-n de 0'''
	
	n = n+1-i
	print("n=",n)

elif (q>1 and u>0) or (q<1 and u<0):
	print("la raison étant comprise entre [1;+infini] alors la suite est divergente vers +infini")
	x = int(input("A quelle precision voulez vous que le resultat en rapport avec le terme U(n) soit? 10^"))
	if x>0:
		x = x
	else:
		x = -x
	'''partie debugage entrée utilisateur'''
	n = 0
	s = 0
	while s<pow(10,x):
		n += 1
		s = u*pow(q,n-i)
	
	'''n=le rang a partir duquelle s est proche a 10^-n de 0'''
	
	n = n+1-i
	print("n=",n)

elif (q<1 and u>0) or (q>1 and u<0):
	print("la raison étant comprise entre [-infini;-1] alors la suite est divergente vers -infini")
	x = int(input("A quelle precision voulez vous que le resultat en rapport avec le terme U(n) soit? 10^"))
	if x>0:
		x = x
	else:
		x = -x
	'''partie debugage entrée utilisateur'''
	n = 0
	s = 0
	while s>-pow(10,x):
		n += 1
		s = u*pow(q,n-i)
	'''n=le rang a partir duquelle s est proche a 10^-n de 0'''
	n = n+1-i
	print("n=",n)
