def agregar_deber(ld, prio, ramo, des):
    largo=len(ld)
    for i in range (0, largo):
        if prio<ld[i][0]:
            ld.insert(i, [])
            ld[i].append(prio)
            ld[i].append(ramo)
            ld[i].append(des)
            return ld