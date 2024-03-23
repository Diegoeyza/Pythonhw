import math

class Grineer:
    def __init__(self, level):
        self.level=level
        self.armor=500*(1+0.4+(level-8)**0.75)
        self.hp=300*(1+(24*math.sqrt(5)/5)*(level-8)**0.5)
        self.dmg=8*(1+0.015*(level-8)**1.55)
        self.dr=self.armor/(self.armor+300)
        self.ehp=self.hp/(1-self.dr)
        self.slash=self.hp/(0.35*1.55**2)
        self.raw=self.ehp/1.55
        self.sp_hp=self.hp*2.5
        self.sp_armor=self.armor*2.5
        self.sp_dr=self.sp_armor/(self.sp_armor+300)
        self.sp_ehp=self.sp_hp/(1-self.sp_dr)
        self.sp_slash=self.sp_hp/(0.35*1.55**2)
        self.sp_raw=self.sp_ehp/1.55


    def __str__(self):   
        grineer_stats=f"Heavy gunner stats:\nLevel={self.level}\nArmor={self.armor}\nHP={self.hp}\nDamage per shot={self.dmg}\nDamage reduction={self.dr*100}%\nEffective hp={self.ehp}\nBase damage needed to kill with 1 slash tick (with pbane)={self.slash}\nBase raw damage needed to kill in one shot (with pbane)={self.raw}\n\nFor steel path:\nArmor={self.sp_armor}\nHP={self.sp_hp}\nDamage reduction={self.sp_dr*100}%\nEffective hp={self.sp_ehp}\nBase damage needed to kill with 1 slash tick (with pbane)={self.sp_slash}\nBase raw damage needed to kill in one shot (with pbane)={self.sp_raw}"
        return grineer_stats

class Corpus:
    def __init__(self, level):
        self.level=level
        self.shields=450*(1+1.6+(level-1)**0.75)
        self.hp=80*(1+(24*math.sqrt(5)/5)*(level-1)**0.5)
        self.dmg=32*(1+0.015*(level-1)**1.55)       
        self.ehp=self.hp+self.shields
        self.tox=self.hp/(0.5*1.55**2)
        self.raw=self.ehp/1.55
        self.sp_hp=self.hp*2.5
        self.sp_shields=self.shields*2.5
        self.sp_ehp=self.sp_hp+self.sp_shields
        self.sp_tox=self.sp_hp/(0.5*1.55**2)
        self.sp_raw=self.sp_ehp/1.55
    def __str__(self):   
        corpus_stats=f"Vapos elite ranger stats:\nLevel={self.level}\nShields={self.shields}\nHP={self.hp}\nDamage per shot (without falloff)={self.dmg}\nEffective hp={self.ehp}\nBase damage needed to kill with 1 tox tick (with pbane)={self.tox}\nBase raw damage needed to kill in one shot (with pbane)={self.raw}\n\nFor steel path:\nShields={self.sp_shields}\nHP={self.sp_hp}\nEffective hp={self.sp_ehp}\nBase damage needed to kill with 1 tox tick (with pbane)={self.sp_tox}\nBase raw damage needed to kill in one shot (with pbane)={self.sp_raw}"
        return corpus_stats

class Infested:
    def __init__(self, level):
        self.level=level
        self.hp=400*(1+(24*math.sqrt(5)/5)*(level-1)**0.5)
        self.dmg=32*(1+0.015*(level-1)**1.55)       
        self.corro=(self.hp-0.75*self.hp)/1.55
        self.raw=self.hp/1.55
        self.sp_hp=self.hp*2.5
        self.sp_corro=(self.sp_hp-0.75*self.sp_hp)/1.55
        self.sp_raw=self.sp_hp/1.55
    def __str__(self):   
        infested_stats=f"Ancient healer stats:\nLevel={self.level}\nHP={self.hp}\nDamage per hit={self.dmg}\nDamage needed to kill with corro(with pbane)={self.corro}\nBase raw damage needed to kill in one shot (with pbane)={self.raw}\n\nFor steel path:\nHP={self.sp_hp}\nDamage needed to kill with corro(with pbane)={self.sp_corro}\nBase raw damage needed to kill in one shot (with pbane)={self.sp_raw}"
        return infested_stats

class Demolist:
    def __init_(self, level, faction):
        return None
    

faction=input("enter the faction of the enemy (C for corpus, G for grineer, I for infested)")
if faction=="g"or faction=="G":
    grineer_1=Grineer(int(input("Enter the enemy level (80+): ")))
    print (grineer_1) 
elif faction=="c" or faction=="C":
    corpus_1=Corpus(int(input("Enter the enemy level (80+): ")))
    print (corpus_1)
elif faction=="i" or faction=="I":
    infested_1=Infested(int(input("Enter the enemy level (80+): ")))
    print (infested_1)