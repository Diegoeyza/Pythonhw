file=open("C:\\Users\\diego\\Github\\Pythonhw\\Autómatas y computabilidad\\nfa4.txt","r")
line=[]
data=[]
initial_states=[]
base_states=[]
final_states=[]
alphabet=[]
transitions=[]
data2=[]
lenght=0
line=file.readline()
while line!='':             #guardo todos los datos en su lista correspondiente, eliminando los carácteres que no me entregan información y leyendo hasta que el archivo llega a una línea vacía
    if "Estados" in line: counter=1
    elif "Alfabeto" in line: counter=2
    elif "Transiciones" in line: counter=3
    if counter==1 and ">" in line: 
        initial_states.append(line.replace(">","").replace("\n",""))
        data.append(line.replace(">","").replace("\n",""))
    elif counter==1 and "*" in line: 
        final_states.append(line.replace("*","").replace("\n",""))
        data.append(line.replace("*","").replace("\n",""))
    elif counter==1 and "Estados" not in line: 
        base_states.append(line.replace("\n",""))
        data.append(line.replace("\n",""))
    line=file.readline()
    if counter==2 and "Transiciones" not in line: alphabet.append(line.replace("\n","")) 
    if counter==3 and line!="": transitions.append(line.replace("-> ","").replace("\n",""))
file.close()


chart=[]        #guardo las relaciones entre los estados y el alfabeto
chart2=[]       #guardo todas las tablas que no sean las hechas con los datos originales de estados
chart.append([""])
chart2.append([""])
for i in range(0,len(alphabet)):        #a ambos chart les pongo el alfabeto en la primera línea, a partir del índice 1 de la sublista (pues el 0 es vacío)
    chart[0].append(alphabet[i])
    chart2[0].append(alphabet[i])
for i in range(0,len(data)):            #al primer chart le pongo la columna de estados
    chart.append([data[i]])
    chart[i+1].append("")
    chart[i+1].append("")



for j in range(0,len(data)):
    for i in range (0, len(transitions)):
        if transitions[i][0]==data[j]:          #verifico si la transición en la que estoy corresponde al estado actual, si esque si, verifico si esque recibe un 0 o un 1 en el alfabeto y acorde a esto guardo el estado al que se llega en el item correspondiente de la sublista (1 si esque usa un 0, o 2 si usa un 1)
            if transitions[i][2]==chart[0][1]:
                if chart[j+1][1]=="":
                    chart[j+1][1]+=transitions[i][4]
                else:
                    chart[j+1][1]+=","
                    chart[j+1][1]+=transitions[i][4]
            elif transitions[i][2]==chart2[0][2]:
                if chart[j+1][2]=="":
                    chart[j+1][2]+=transitions[i][4]
                else:
                    chart[j+1][2]+=","
                    chart[j+1][2]+=transitions[i][4]
for j in range (1, len(chart)):             #armo la columna del chart2 con los elementos que no eran estados originales y no eran vacío
    for i in range (1, len(chart[j])):
        if chart[j][i] not in data and chart[j][i]!="":
            chart2.append([chart[j][i]])
while (lenght!=len(chart2)):            #verifico que siga en el ciclo while siempre y cuando se sigan incrementando la cantidad de estados nuevos, cuando ya no se agreguen más, salgo del ciclo while, guardando todos los estados nuevos
    lenght=len(chart2)
    for i in range (1, lenght):         #vacío toda la lista de estados a los que se llegan con comandos del alfabeto, para realizarlos de nuevo en cada iteración y así evitar cualquier problema de control de flujo (aunque haya más coste de procesamiento computacional, es preferible a la posibilidad de que haya algún error)
        if len(chart2[i])==1:
            chart2[i].append("")
            chart2[i].append("")
        else:
            chart2[i][1]=""
            chart2[i][2]=""
    for i in range (1, lenght):             #completo la tabla de transiciones al igual que antes
        for j in range (0, len(chart2[i])):
            for k in range (0, len(transitions)):
                if transitions[k][0] in chart2[i][0] and transitions[k][2]==chart2[0][1] and transitions[k][4] not in chart2[i][1]:
                    if chart2[i][1]=="":
                        chart2[i][1]+=transitions[k][4]
                    else:
                        chart2[i][1]+=","
                        chart2[i][1]+=transitions[k][4]
                if transitions[k][0] in chart2[i][0] and transitions[k][2]==chart2[0][2] and transitions[k][4] not in chart2[i][2]:
                    if chart2[i][2]=="":
                        chart2[i][2]+=transitions[k][4]
                    else:
                        chart2[i][2]+=","
                        chart2[i][2]+=transitions[k][4]
    data2=[]                             #vacío los datos nuevos para así llenarlos cada vez que se haga el ciclo
    for i in range (1, len(chart2)):     #lleno los datos (estados) nuevos
        data2.append(chart2[i][0])
    for i in range (1, len(chart2)):
        for j in range (1, len(chart2[i])):
            if chart2[i][j] not in data2 and chart2[i][j]!="":          #verifico si esque hay algún estado nuevo y si esque lo hay, lo agrego a mi chart2, haciendo que se realice un ciclo más del while
                chart2.append([chart2[i][j]])
file = open("C:\\Users\\diego\\Github\\Pythonhw\\Autómatas y computabilidad\\dfa4.txt","w")     #creo o edito el archivo en el cual voy a escribir todos los datos
file.write("Estados\n")
used=[]
for i in data2:                 #verifico si los datos están en las listas guardadas inicialmente para ver si alguno es estado inicial, cuales son estados finales, y cuales son intermedios, a medida que voy llenando una lista que me indica cuales ya anoté para no repetirlos
    if i in initial_states and i not in used:
        file.write(">{")
        file.write(i)
        file.write("}\n")
        used.append(i)
    for j in final_states:
        if j in i and i not in used:
            file.write("*{")
            file.write(i)
            file.write("}\n")
            used.append(i)
            continue
    if i not in used:
        file.write("{")
        file.write(i)
        file.write("}\n")
        used.append(i)
file.write("Alfabeto\n")
for i in alphabet:
    file.write(f'{i}\n')
file.write("Transiciones\n")
for i in range (1,len(chart2)):          #itero a partir de 1 porque el 0 son los valores del alfabeto
    file.write("{")
    file.write(chart2[i][0])
    file.write("} ")
    file.write(chart2[0][1])
    file.write(" -> ")
    file.write("{")
    file.write(chart2[i][1])
    file.write("}\n")

    file.write("{")
    file.write(chart2[i][0])
    file.write("} ")
    file.write(chart2[0][2])
    file.write(" -> ")
    file.write("{")
    file.write(chart2[i][2])
    file.write("}\n")





    
    

file.close()
        






                        

                            


    




