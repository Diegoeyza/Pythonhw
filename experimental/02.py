traductor=input()
alfanum = True
for caracter in traductor:
    if caracter.lower() not in "abcdefghijklmnopqkrstuvwxyz":
        if caracter not in "0123456789":   
            alfanum = False
if alfanum==True:
    if traductor==(traductor.upper()):
        print (traductor.lower())
    elif traductor==(traductor.lower()):
        print (traductor.upper())
    else:
        print (traductor)
else:
    print ("01111001 01100001")