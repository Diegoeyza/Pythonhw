t=float(input("ingrese el valor teórico: "))
e=float(input("ingrese el valor experimental: "))
if t<e:
    ert=abs((t-e)*100/t)
    print(f"lo que le falta al caso teórico para ser el experimental (error) es: {ert}%")
elif t>e:
    ere=abs((t-e)*100/t)
    print(f"lo que le falta al caso experimental para ser el teórico (error) es: {ere}%")
else:
    print("el error es 0")