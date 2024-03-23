def escribir_archivo(x, y):
    archivo=open(x, "w")
    archivo.write(y)
    archivo.close

x=input()
n=int(input())
y=""
for i in range(0, n):
    palabra=input()
    if y=="":
        y=y+palabra
    else:
        y=y+"\n"+palabra
escribir_archivo(x, y)
import functions
functions.print_file(x)