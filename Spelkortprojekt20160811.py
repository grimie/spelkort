def final_hand():
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
    #print hand
    "Nu delar vi upp handen i tva listor, farg, nummer."


    hand_farg = []
    for a in hand:
        hand_farg.append(a[0])

    #hand_farg = ["hjarter","hjarter", "hjarter", "hjarter", "hjarter"]

    hand_siffror = []
    for a in hand:
        hand_siffror.append(a[1])

    #hand_siffror = [1, 10, 11, 12, 13]


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




    ##singelpar

    def par():
        if len(par_i_hand) == 1:
            return True
        else:
            return False

    ##dubbelpar

    def tvapar():
        if len(par_i_hand) == 2:
            return True
        else:
            return False


    #triss
    triss_i_hand=[]
    def triss():
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
                return True
        return False


    #fyrtal
    fyrtal_i_hand=[]
    def fyrtal():
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
                return True
        return False


    #full-house
    def full_house():
        if par() == True and triss() == True:
            return True
        else:
            return False


    #farg i hand
    def farg():
        if hand_farg[0] == hand_farg[1] and hand_farg[1] == hand_farg[2] and hand_farg[2] == hand_farg[3] and hand_farg[3] == hand_farg[4]:
            return True
        else:
            return False

    #stege i hand
    stege_lista = []
    def stege():
        hand_siffror.sort()
        print hand_siffror
        n = 0
        if hand_siffror[n]+1 == hand_siffror[n+1] and hand_siffror[n]+2 == hand_siffror[n+2] and hand_siffror[n]+3 == hand_siffror[n+3] and hand_siffror[n]+4 == hand_siffror[n+4]:
            for a in hand_siffror:
                if a == 11:
                    stege_lista.append("Knekt")
                elif a == 12:
                    stege_lista.append("Dam")
                elif a == 13:
                    stege_lista.append("Kung")
                else:
                    stege_lista.append(a)
            return True
        else:
            return False
        
    stege_special_lista = [10, "Knekt", "Dam", "Kung", "Ess"]
    def stege_special():
        if hand_siffror[0] == 1 and hand_siffror[1] == 10 and hand_siffror[2] == 11 and hand_siffror[3] == 12 and hand_siffror[4] == 13:
            return True
        else:
            return False


    def Main():
        if stege() and farg():
            return "Du har fargstege i", stege_lista, "i fargen", hand_farg[0]
        elif stege_special() and farg():
            return "Du har fargstege i", stege_special_lista, "i fargen", hand_farg[0]
        elif fyrtal():
            return "Du har fyrtal i", fyrtal_i_hand[0]
        elif par() and triss():
            return "Du har full-house med triss i", triss_i_hand[0], "och par i", par_i_hand[0]
        elif farg():
            return "Du har farg i", hand_farg[1]
        elif stege():
            return "Du har stege i", stege_lista
        elif stege_special():
            return "Du har steg i", stege_special_lista
        elif triss():
            return "Du har triss i", triss_i_hand[0]
        elif tvapar():
            return "Du har tvapar i", par_i_hand[0], "och", par_i_hand[1]
        elif par():
            return "Du har par i", par_i_hand[0]
        else:
            return "Du har tyvarr inget bra pa handen"

    return Main()

def raknare():
    n = 1
    x = 0
    while x < 1:
        final_hand()
        if final_hand() == final_hand(Main(stege())):
            x = x+1
            return n
        else:
            n = n+1
            return n

print raknare()
        



        




