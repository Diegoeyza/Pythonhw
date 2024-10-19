memory=[]
memsize=256 #16*16
#fila varía entre 4 y 8, la fila 4 es 16*4

def printb(memory):
    print("\n\n")
    for i in range (0, 16):
        print(f"{memory[(16*i)]}{memory[(16*i)+1]}{memory[(16*i)+2]}{memory[(16*i)+3]}{memory[(16*i)+4]}{memory[(16*i)+5]}{memory[(16*i)+6]}{memory[(16*i)+7]}{memory[(16*i)+8]}{memory[(16*i)+9]}{memory[(16*i)+10]}{memory[(16*i)+11]}{memory[(16*i)+12]}{memory[(16*i)+13]}{memory[(16*i)+14]}{memory[(16*i)+15]}\n")
    print("\n\n")

def N(movlist, mem, ball):
    mem[ball[0]+ball[1]*16]=" - "
    ball[1]-=1
    mem[ball[0]+ball[1]*16]=" O "
    movlist[0]=0

def S(movlist, mem, ball):
    mem[ball[0]+ball[1]*16]=" - "
    ball[1]+=1
    mem[ball[0]+ball[1]*16]=" O "
    movlist[0]=4

def E(movlist, mem, ball):
    mem[ball[0]+ball[1]*16]=" - "
    ball[0]+=1
    mem[ball[0]+ball[1]*16]=" O "
    movlist[0]=2

def W(movlist, mem, ball):
    mem[ball[0]+ball[1]*16]=" - "
    ball[0]-=1
    mem[ball[0]+ball[1]*16]=" O "
    movlist[0]=6

def NE(movlist, mem, ball):
    mem[ball[0]+ball[1]*16]=" - "
    ball[0]+=1
    ball[1]-=1
    mem[ball[0]+ball[1]*16]=" O "
    movlist[0]=1

def NW(movlist, mem, ball):
    mem[ball[0]+ball[1]*16]=" - "
    ball[1]-=1
    ball[0]-=1
    mem[ball[0]+ball[1]*16]=" O "
    movlist[0]=7

def SE(movlist, mem, ball):
    mem[ball[0]+ball[1]*16]=" - "
    ball[1]+=1
    ball[0]+=1
    mem[ball[0]+ball[1]*16]=" O "
    movlist[0]=3

def SW(movlist, mem, ball):
    mem[ball[0]+ball[1]*16]=" - "
    ball[1]+=1
    ball[0]-=1
    mem[ball[0]+ball[1]*16]=" O "
    movlist[0]=5

def move_ball(movlist, mem, ball):
    mov=movlist[0]
    if (mov==0):    #N
        if (mem[ball[0]+(ball[1]-1)*16]==" X "):
            S(movlist,mem,ball)
        else:
            N(movlist,mem,ball)
    elif(mov==1):   #NE
        if ((mem[(ball[0]+1)+(ball[1])*16]==" X ") and (mem[(ball[0])+(ball[1]-1)*16]==" X ")):  #corner case
            SW(movlist,mem,ball)
        elif (mem[(ball[0]+1)+(ball[1])*16]==" X "):  #hits wall on x
            NW(movlist,mem,ball)
        elif (mem[(ball[0])+(ball[1]-1)*16]==" X "):  #hits wall on y
            SE(movlist,mem,ball)
        else:
            NE(movlist,mem,ball)
    elif(mov==2):   #E
        if (mem[(ball[0]+1)+(ball[1])*16]==" X "):
            W(movlist,mem,ball)
        else:
            E(movlist,mem,ball)
    elif(mov==3):   #SE
        if ((mem[(ball[0])+(ball[1]+1)*16]==" X ") and (mem[(ball[0]+1)+(ball[1])*16]==" X ")):
            NW(movlist,mem,ball)
        elif (mem[(ball[0]+1)+(ball[1])*16]==" X "):
            SW(movlist,mem,ball)
        elif (mem[(ball[0])+(ball[1]+1)*16]==" X "):
            NE(movlist,mem,ball)
        else:
            SE(movlist,mem,ball)
    elif(mov==4):   #S
        if (mem[(ball[0])+(ball[1]+1)*16]==" X "):
            N(movlist,mem,ball)
        else:
            S(movlist,mem,ball)
    elif(mov==5):   #SW
        if ((mem[(ball[0]-1)+(ball[1])*16]==" X ") and (mem[(ball[0])+(ball[1]+1)*16]==" X ")):
            NE(movlist,mem,ball)
        elif (mem[(ball[0]-1)+(ball[1])*16]==" X "):
            SE(movlist,mem,ball)
        elif (mem[(ball[0])+(ball[1]+1)*16]==" X "):
            NW(movlist,mem,ball)
        else:
            SW(movlist,mem,ball)
    elif(mov==6):   #W
        if (mem[(ball[0]-1)+(ball[1])*16]==" X "):
            E(movlist,mem,ball)
        else:
            W(movlist,mem,ball)
    elif(mov==7):   #NW
        if ((mem[(ball[0]-1)+(ball[1])*16]==" X ") and (mem[(ball[0])+(ball[1]-1)*16]==" X ")):
            SE(movlist,mem,ball)
        elif (mem[(ball[0]-1)+(ball[1])*16]==" X "):
            NE(movlist,mem,ball)
        elif (mem[(ball[0])+(ball[1]-1)*16]==" X "):
            SW(movlist,mem,ball)
        else:
            NW(movlist,mem,ball)


head= 5
ballx= 1
bally= 6
endx= 14
endy= 10
mov= 7
max_iterations=100
ball= [ballx,bally]
end = [endx,endy]
movlist=[mov]
for i in range (0,16*16): 
    if ((i%16==0 and (i/16>=head and i/16<=12)) or (i/16>=head and i/16<head+1) or (i/16>=12 and i/16<13) or (i%16==15 and (i/16>=head and i/16<=12)) ):
        memory.append(" X ")
    elif (i==ball[0]+ball[1]*16):
        memory.append(" O ")
    elif (i==end[0]+end[1]*16):
        memory.append(" ! ")
    else:
        memory.append(" - ")

for i in range (0, 16):
    print(f"{memory[(16*i)]}{memory[(16*i)+1]}{memory[(16*i)+2]}{memory[(16*i)+3]}{memory[(16*i)+4]}{memory[(16*i)+5]}{memory[(16*i)+6]}{memory[(16*i)+7]}{memory[(16*i)+8]}{memory[(16*i)+9]}{memory[(16*i)+10]}{memory[(16*i)+11]}{memory[(16*i)+12]}{memory[(16*i)+13]}{memory[(16*i)+14]}{memory[(16*i)+15]}\n")

counter=0

while (counter<max_iterations):
    move_ball(movlist,memory,ball)
    if (ball[0]==end[0] and ball[1]==end[1]):
        counter=max_iterations
        print("The ball has hit the red spot!!\n")
    else:
        printb(memory)
    counter+=1
print("GAME OVER")