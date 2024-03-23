frase=input()
x=0
frasef="a"
for i in frase:
        if i in ".,:;" and frasef=="a":
            frasef=frase[x+1:]
            y=x
        else:
            x=x+1
frasef1=frasef
x=0
for i in frasef:
        if i in ".,:;" and frasef1==frasef:
            x=x+1
            frasef=frasef[0:x-1]
            z=x
        else:
            x=x+1
print(frasef)
print("posiciones "+str(y)+" - "+str(z+y))