buzz=[]
zorg=[]
palabra=""
e=""
contador=1
while palabra!="end":
    palabra=(input())
    if palabra!="end":
        buzz.append(palabra)
while e!="end":
    e=(input())
    if e!="end":
        zorg.append(e)
for i in range (0, len(buzz)):
	buzz[i]=int(buzz[i])
for i in range (0, len(zorg)):
	zorg[i]=int(zorg[i])
while len(buzz)!=0 and len(zorg)!=0:
    if buzz[0]>zorg[0]:
        buzz[0]=buzz[0]-1
        del zorg[0]
        print("Buzz ha ganado esta ronda!")
    elif zorg[0]>=buzz[0]:
        zorg[0]=zorg[0]-1
        del buzz[0]
        print("Zurg ha ganado esta ronda!")
if len(buzz)>0:
    print("Buzz! Nos has salvado, estamos agradecidos!")
else:
    print("El malvado emperador Zurg tomara control de la Unimente!")