objetivo=int(input())
actual=int(input())
a=abs(100-abs(objetivo-actual))
if a>50:
    b=(abs(a-100))
    if actual+b==objetivo:
    	print (str(b)+ " veces arriba")
    else:
        print (str(b)+ " veces abajo")
else:
    if actual+a==objetivo or actual+a-100==objetivo:
        print (str(a)+ " veces arriba")
    else:
        print (str(a)+ " veces abajo")