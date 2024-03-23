N=int(input())
pok=input()
lista=pok.split(",")
pokemons=[]
for i in range(0, len(lista)):
    pokemons.append([])
    pokemons[i].append(lista[i])

for i in range (0, N):
    a=int(input())
    pokemons[i].append(a)
def pc(pokemons):
    return pokemons[1]
pokemonsO=sorted(pokemons, key=pc)
print (pokemonsO)