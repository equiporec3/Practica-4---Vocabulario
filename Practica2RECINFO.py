import nltk
import re
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer 
ps = PorterStemmer()
cont = 0
filename = "TodosLibros.txt"
file = open(filename,encoding="utf8")
text = file.readlines()
file.close()
longitud=len(text)
file = open("ResultadosdeEjecuacucion.txt", "w")	
#print(longitud) #108747  longitud del TXT en lineas
Textoprocesado=[]
for x in range(0,longitud):
	if text[x] == ".W"+"\n":
		y = x+1
		words=[]
		while text[y] != ".X"+"\n":
			#print(text[y])
			words = text[y].split()
			#print(words)
			words= re.split(r'\W+', text[y])
			#print(words)
			words = [word.lower() for word in words]
			#print(words)
			nltk_stopwords = set(stopwords.words('english'))
			text_without_stopword = [word for word in words if not word in nltk_stopwords]
			#print(text_without_stopword)

			todoo=[]
			for x in range(len(text_without_stopword)):
				ww= text_without_stopword[x]
				todoo.append(ps.stem(ww))
				#print(todoo)
			#print("  ")
			
			
			all = " ".join(todoo)
			
			file.write(all)
			file.write("\n")
			
			y+=1

file.close()	

filename = "ResultadosdeEjecuacucion.txt"
file = open(filename,encoding="utf8")
text = file.read()
file.close()

Textoprocesado = text.split()
Textoprocesado=set(Textoprocesado)
Textoprocesado=sorted(Textoprocesado)
file = open("Diccionario.txt", "w")
Texto = " ".join(Textoprocesado)
file.write(Texto)
file.close()
Longi = len(Textoprocesado)
file = open("LongitudDiccionario.txt", "w")
file.write(str(Longi))
file.close()
