def abejas_comidas(actividades, dieta, dia):
    contador=0
    pos=0
    actividad=actividades
    cont=0
    días=0
    for i in actividades:
        for i in "!?":
            comer=0
            días=días+1
            cont=0
            for i in actividades:
                if i not in "!?":
                    if i=="C":
                        comer=comer+1
                    cont=cont+1
                else:
                    break
            if días<dia:
                actividad=actividad[cont:]
            if días==dia:
                comerf=comer
                cont=0
                for i in actividades:
                    if i not in "!?":
                        if i=="C":
                            comer=comer+1
                        cont=cont+1
                    else:
                        actividad=actividad[1:cont+3]
                        comer=0
                        for i in actividad:
                            if i=="C":
                                comer=comer+1
                        dieta=dieta[comerf:comer+comerf]
                        abejas=0
                            
                        for j in dieta:
                            if j=="A":
                                abejas=abejas+1
                        return print(abejas)

abejas_comidas("CCS!SCSP!CCCSPC?SCSCCSC!", "MAAGMGGGGGG", 2)
abejas_comidas("PSCSCCS!SPCCP?SPSSCSPP?SCSSPPCPS!CPCPCCS!PCPCPSSC?", "AEMGGGMAEMMAMAG", 1)