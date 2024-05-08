import re  
import urllib.request

print("Welcome to the mail extractor 3000")
entry=input("Please enter the url of the webpage you want to analyze\n->")
print("Extracting mail adresses...\n\nThe adresses are:")
url=urllib.request.urlopen(entry)
data=str(url.read())
patron = re.compile(r'([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4})') #No lo hice usando \w porque preferí que fuera más versátil esto me permite reconocer todo el alfabeto en minuscula y mayuscula, números y el guion bajo (similar a \w), para así poderlo modificar a futuro y filtrar mails alfabeticamente. adicionalmente, luego del @ recibe un string con las mismas condiciones que el inicial, luego un punto y luego un string de tamaño entre 2 y 4 (pues 2 es el tamaño minimo y 4 el maximo de los identificadores del mail)
mail_list = re.findall(patron, data)

for mail in mail_list:
    print(mail)
print("\nSuccess!!\n")