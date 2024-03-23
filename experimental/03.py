str1=input()
str2=input()
str3=input()
str4=input()
def verificador_letras(palabra):
    contador=0
    verificador=0
    for letra in str1:
        if letra in palabra:
            verificador=verificador+1
        contador=contador+1
    if verificador==contador:
       return print(True)
    else:
       return print(False)
verificador_letras(str2)
verificador_letras(str3)
verificador_letras(str4)