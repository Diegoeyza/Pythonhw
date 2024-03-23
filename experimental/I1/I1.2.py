act=input()
días=0
cont=0
comer=0
for i in act and ("!?" or "!" or "?"):
    comer=0
    días=días+1
    print(act)
    cont=0
    for i in act:
        if i not in "!?":
            if i=="C":
                comer=comer+1
                cont=cont+1
            else:
                cont=cont+1
        else:
            break

    act=act[cont+1:]
    if comer>0:
        print("Dia "+str(días)+" come "+str(comer)+ " vez")
    else:
        print("Dia "+str(días)+" no come ")
    print(act)
     






