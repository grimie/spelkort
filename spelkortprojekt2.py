def generate_hand():
    kortlek = []

    farger = ["hjarter", "ruter", "spader", "klover"]
    siffror = list(range(1, 14))


    for farg in farger:
        for siffra in siffror:
            x = (farg, siffra)
            kortlek.append(x)


    import random
    random.shuffle(kortlek)

    "nu ska vi plocka ur en hand"

    hand = kortlek[:5]

    "Nu delar vi upp handen i tva listor, farg, nummer."


    hand_farg = []
    for a in hand:
        hand_farg.append(a[0])

    #hand_farg = ["hjarter","hjarter", "hjarter", "hjarter", "hjarter"]

    hand_siffror = []
    for a in hand:
        hand_siffror.append(a[1])

    #hand_siffror = [1, 2, 3, 4, 5]
    return hand_farg, hand_siffror


def parn(hand_siffror):
    #definition av parformer
    par_i_hand=[]
    for x in range(1, 14):
        if hand_siffror.count(x) == 2:
            par_i_hand.append(x)


    if len(par_i_hand) == 1 or len(par_i_hand) == 2:
        if par_i_hand[0] == 1:
            par_i_hand[0]="Ess"
        elif par_i_hand[0] == 11:
            par_i_hand[0]="Knekt"
        elif par_i_hand[0] == 12:
            par_i_hand[0]="Dam"
        elif par_i_hand[0] == 13:
            par_i_hand[0]="Kung"

    if len(par_i_hand) == 2:
        if par_i_hand[1] == 11:
            par_i_hand[1]="Knekt"
        elif par_i_hand[1]== 12:
            par_i_hand[1]="Dam"
        elif par_i_hand[1] == 13:
            par_i_hand[1]="Kung"
    return par_i_hand



    ##singelpar

def par(hand_siffror):
        #par_i_hand = parn(hand_siffror)
        a = parn(hand_siffror)
        if len(a) == 1:
            return a
        else:
            return False

    ##dubbelpar

def tvapar(hand_siffror):
        par_i_hand =parn(hand_siffror)
        if len(par_i_hand) == 2:
            return par_i_hand
        else:
            return False


    #triss

def triss(hand_siffror):
        triss_i_hand=[]
        for x in range(1, 14):
            if hand_siffror.count(x) == 3:
                triss_i_hand.append(x)
                if triss_i_hand[0] == 1:
                    triss_i_hand[0]="Ess"
                elif triss_i_hand[0] == 11:
                    triss_i_hand[0]="Knekt"
                elif triss_i_hand[0] == 12:
                    triss_i_hand[0]="Dam"
                elif triss_i_hand[0] == 13:
                    triss_i_hand[0]="Kung"
                return triss_i_hand
        return False


    #fyrtal

def fyrtal(hand_siffror):
        fyrtal_i_hand=[]
        for x in range(1, 14):
            if hand_siffror.count(x) == 4:
                fyrtal_i_hand.append(x)
                if fyrtal_i_hand[0] == 1:
                    fyrtal_i_hand[0]="Ess"
                elif fyrtal_i_hand[0] == 11:
                    fyrtal_i_hand[0]="Knekt"
                elif fyrtal_i_hand[0] == 12:
                    fyrtal_i_hand[0]="Dam"
                elif fyrtal_i_hand[0] == 13:
                    fyrtal_i_hand[0]="Kung"
                return fyrtal_i_hand
        return False


    #full-house
def full_house():
        if par() == True and triss() == True:
            return True
        else:
            return False


    #farg i hand
def farg(hand_farg):
        if hand_farg[0] == hand_farg[1] and hand_farg[1] == hand_farg[2] and hand_farg[2] == hand_farg[3] and hand_farg[3] == hand_farg[4]:
            return hand_farg
        else:
            return False

    #stege i hand
    
def stege(hand_siffror):
        stege_lista = []
        hand_siffror.sort()
        n = 0
        if hand_siffror[n]+1 == hand_siffror[n+1] and hand_siffror[n]+2 == hand_siffror[n+2] and hand_siffror[n]+3 == hand_siffror[n+3] and hand_siffror[n]+4 == hand_siffror[n+4]:
            for a in hand_siffror:
                if a == 1:
                    stege_lista.append("Ess")
                elif a == 11:
                    stege_lista.append("Knekt")
                elif a == 12:
                    stege_lista.append("Dam")
                elif a == 13:
                    stege_lista.append("Kung")
                else:
                    stege_lista.append(a)
            return stege_lista
        else:
            return False
        

def stege_special(hand_siffror):
        stege_special_lista = [10, "Knekt", "Dam", "Kung", "Ess"]
        if hand_siffror[0] == 1 and hand_siffror[1] == 10 and hand_siffror[2] == 11 and hand_siffror[3] == 12 and hand_siffror[4] == 13:
            return stege_special_lista
        else:
            return False


def Main():
        f, s = generate_hand()
        if stege(s) and farg(f):
            return "Du har straight flush i", stege(s) , "i fargen", f[1]
        elif stege_special(s) and farg(f):
            return "Du har royal straight flush i", stege_special(s), "i fargen", f[0]
        elif fyrtal(s):
            return "Du har fyrtal i", fyrtal(s)
        elif par(s) and triss(s):
            return "Du har full-house med triss i",triss(s), "och par i", par(s)
        elif farg(f):
            return "Du har flush i", farg[1]
        elif stege(s):
            return "Du har stege i", stege(s)
        elif stege_special(s):
            return "Du har royal straight i", stege_special(s)
        elif triss(s):
            return "Du har triss i", triss(s)
        elif tvapar(s):
            return "Du har dubbla par i", tvapar(s)
        elif par(s):
            return "Du har par i", par(s)
        else:
            return "Du har tyvarr inget bra pa handen :("

print Main()



def raknare_fargstege():
    n = 1
    while True:
        f, s = generate_hand() 
        if stege(s) and farg(f):
            return "Denna gang tog det", n, "ganger att fa straight flush."
        n = n+1

def raknare_fargstegespecial():
    n = 1
    while True:
        f, s = generate_hand() 
        if stege_special(s) and farg(f):
            return "Denna gang tog det", n, "ganger att fa Royal straight flush."
        n = n+1

def raknare_fyrtal():
    n = 1
    while True:
        f, s = generate_hand() 
        if fyrtal(s):
            return "Denna gang tog det", n, "ganger att fa fyrtal."
        n = n+1

def raknare_fullhouse():
    n = 1
    while True:
        f, s = generate_hand() 
        if triss(s) and par(s):
            return "Denna gang tog det", n, "ganger att fa full-house."
        n = n+1

def raknare_farg():
    n = 1
    while True:
        f, s = generate_hand() 
        if farg(f):
            return "Denna gang tog det", n, "ganger att fa flush."
        n = n+1


def raknare_stege():
    n = 1
    while True:
        f, s = generate_hand() 
        if stege(s):
            return "Denna gang tog det", n, "ganger att fa stege."
        n = n+1

def raknare_stegespecial():
    n = 1
    while True:
        f, s = generate_hand() 
        if stege_special(s):
            return "Denna gang tog det", n, "ganger att fa royal straight."
        n = n+1

def raknare_triss():
    n = 1
    while True:
        f, s = generate_hand() 
        if triss(s):
            return "Denna gang tog det", n, "ganger att fa triss."
        n = n+1


def raknare_tvapar():
    n = 1
    while True:
        f, s = generate_hand() 
        if tvapar(s):
            return "Denna gang tog det", n, "ganger att fa dubbla par."
        n = n+1

def raknare_par():
    n = 1
    while True:
        f, s = generate_hand() 
        if par(s):
            return "Denna gang tog det", n, "ganger att fa par."
        n = n+1
print "---------"    
print raknare_farg()

        



        




