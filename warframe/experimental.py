DBOi=int(input("DBOi:   "))
DBOU=int(input("DBOU:   "))
DBOL=int(input("DBOL:   "))
DBOFU=(DBOi-DBOU)/DBOi*100
DBOFL=(DBOi-DBOL)/DBOi*100
print(f"DBOFU={DBOFU},     DBOFL={DBOFL}")