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
print hand

"Nu delar vi upp handen i tva listor, farg, nummer."

hand_farg = []
for a in hand:
    hand_farg.append(a[0])


hand_siffror = []
for a in hand:
    hand_siffror.append(a[1])



#definition av parformer
par_i_hand=[]
for x in range(12):
    if hand_siffror.count(x+1) == 2:
        par_i_hand.append(x+1)

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
    for x in range(12):
        if hand_siffror.count(x+1) == 3:
            triss_i_hand.append(x+1)
            return True

    return False




#fyrtal
fyrtal_i_hand=[]
def fyrtal():
    for x in range(12):
        if hand_siffror.count(x+1) == 4:
            fyrtal_i_hand.append(x+1)
            return True

    return False


#full-house
def full_house():
    if par() == True and triss() == True:
        return True
    else:
        return False
#print "du har full-house i", triss_i_hand, "och", par_i_hand


#farg i hand
def farg():
    if hand_farg[0] == hand_farg[1] and hand_farg[1] == hand_farg[2] and hand_farg[2] == hand_farg[3] and hand_farg[3] == hand_farg[4]:
        return True
    else:
        return False

#stege i hand
def stege():
    hand_siffror.sort()
    n = 0
    if hand_siffror[n] +1 == hand_siffror[n+1] and hand_siffror[n]+2 == hand_siffror[n+2] and hand_siffror[n]+3 == hand_siffror[n+3] and hand_siffror[n]+4 == hand_siffror[n+4]:
        return True
    else:
        return False



def Main():
    if stege() == True and farg() == True:
        print "Du har fargstege i", hand_siffror[0:], "i fargen", hand_farg[0]

    elif fyrtal() == True:
        print "Du har fyrtal i", fyrtal_i_hand[0]

    elif par() == True and triss() == True:
        print "du har full-house med triss i", triss_i_hand, "och par i", par_i_hand
    elif farg() == True:
        print "du har farg i", hand_farg[1]
    elif stege() == True:
        print "Du har stege i", hand_siffror[0:]
    elif triss() == True:
        print "du har triss i", triss_i_hand
    elif tvapar() == True:
        print "du har tva par i", par_i_hand
    elif par() == True:
        print "du har par i", par_i_hand
    else:
        print "du har tyvarr inget bra pa handen"

print Main()
