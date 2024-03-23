print("Welcome to the cc and sc warframe calculator")
weapon=str(input("select between melee, primary or secondary: "))
if weapon=="melee":
    base_cc=int(input("enter its base cc:  "))
    base_cd=float(input("enter its base cd:  "))
    base_sc=int(input("enter its base sc:  "))
    br=int(input("enter 1 if using the blood rush mod, 0 if not:    "))
    gladiator_set=int(input("enter the ammount of gladiator set mods you are using:  "))
    ww=int(input("enter 1 if using weeping wounds, 0 if not:  "))
    modded_sc=int(input("enter the status chance you modded for (60, 70, etc):  "))
    modded_cc=int(input("enter the sum of the cc mods on the weapon without br or glad mods:  "))
    modded_cd=int(input("enter the modded cd of the weapon:  "))
    combo_count=int(input("enter the combo counter:  "))
    cc=base_cc+base_cc*(combo_count-1)*0.1*br*4+base_cc*(combo_count-1)*gladiator_set*0.1*1+base_cc*modded_cc*0.01
    sc=base_sc+base_sc*(combo_count-1)*0.1*ww*4+base_sc*modded_sc*0.1
    avg_cd=(cc/100+1)*(base_cd*modded_cd*0.01)+base_cd
    print("your weapons critical chance at "+str(combo_count)+" combo will be: "+str(cc)+" on regular atacks and "+str(cc*2)+" on heavy atacks")
    print("your weapons average critical damage per hit will be: "+str(avg_cd))
    print("your weapons status chance at "+str(combo_count)+" combo will be: "+str(sc))