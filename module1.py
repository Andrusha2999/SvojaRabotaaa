def lists()->list:
	""" tegi listid failist
	"""
	palgad=[]
	with open("denjgi.txt", "r") as f1: #avastame ebaõnnestumisi
		for s in f1:
			palgad.append(s.strip()) # koostanud nimekirjad
	inimesed=[]
	with open ("inimised.txt", "r") as inimene:
		for q in inimene:
			inimesed.append(q.strip())
	return palgad,inimesed

def dobavka():
	""" lisamine inimese ja palk
	"""
	N=1
	palgad=[]
	inimesed=[]
	for n in range(N):
		nimi=input("Siseta nimi: ")

		inimesed.append(nimi)
		palk=input("Siseta palgad: ")
		palgad.append(palk)
	with open("inimised.txt", "a") as inimesed: #lisame nimi  
		inimesed.write(nimi+"\n")	
	with open("denjgi.txt", "a") as palgad: #lisame palk 
		palgad.write(palk+"\n")

def udalenie():
	"""delete_inimene()
	"""
	palgad,inimesed=lists()  
	nimi=input("Siseta nimi: ")
	if nimi not in inimesed: # kontrollime, kas nimi
		print("Kas sa tahad lisada nimi ja palgad?") 
		c=input("Y = jah, N = ei")
		if c.upper=="Y":
			add_person() # kasutame funktsiooni nime ja palga registreerimiseks
		else:
			pass
	else:
		a=inimesed.index(nimi) 
		inimesed.pop(a) 
		palgad.pop(a) 
	f=open("ludi.txt", "w")
	for g in inimesed:
		f.write(g+"\n")
	f.close()
	d=open("zarplata.txt", "w")
	for i in palgad:
		d.write(i+"\n")
	d.close()

def maksimalka():
	"""Arvutamine suurim palk
	"""
	palgad,inimesed=lists()
	suurim=max(palgad) # muutuv indeks edaspidiseks kasutamiseks
	b=palgad.index(suurim) 
	print("kõike suured palga on "+inimesed[b]+" palga")

def minimalka():
	"""arvumine kõige smal palk
	"""
	palgad,inimesed=lists()
	palgadS=palgad.copy()
	palgadS.sort()
	a=palgadS[0]
	b=palgad.index(a)
	print("kõike väiksem palga on "+inimesed[b]+" palga ja see on "+ palgadS[0]+" euro")

def sort():
	palgadS=[]
	palgad,inimesed=lists()
	palgadS=palgad.copy()
	palgadS.sort()
	for palk in palgadS:
		a=palgad.index(palk) # otsime registrist, et sortimata nimekirjadest leida nimi ja palk.
		print(palgad[a]+" "+inimesed[a])