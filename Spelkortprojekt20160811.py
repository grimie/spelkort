kortlek = []

farger = ["hjarter", "ruter", "spader", "klover"]
siffror = list(range(1, 14))


for farg in farger:
    for siffra in siffror:
        x = (farg, siffra)
        kortlek.append(x)


import random
random.shuffle(kortlek)
print kortlek

"nu ska vi plocka ur en hand"

hand = kortlek[:5]
print hand

"Nu delar vi upp handen i tva listor, farg, nummer."

hand_farg = []
for a in hand:
    hand_farg.append(a[0])
hand_farg = ["hjarter", "hjarter", "hjarter", "hjarter", "hjarter"]
print hand_farg


hand_siffror = []
for a in hand:
    hand_siffror.append(a[1])
hand_siffror = [1, 1, 2, 3, 4]
#[1, 2, 3, 4]

print hand_siffror



#par i hand
'''n = 0
for x in hand_siffror[:-1]:
    if x==hand_siffror[(n+1)]:
        print "pair in", x
    n=n+1'''

#par pa annat satt
par_i_hand=[]
def samlingar():
    for x in range(12):
        if hand_siffror.count(x+1) == 2:
            par_i_hand.append(x+1)
'''
            print "Par i", (x+1)
    print par_i_hand
print samlingar()
'''
#singelpar

def par():
    if len(par_i_hand) == 1:
        return True
    else:
        return False

#dubbelpar

def tvapar():
    if len(par_i_hand) == 2:
        return True
    else:
        return False


#triss
triss_i_hand=[]
for x in range(12):
    if hand_siffror.count(x+1) == 3:
        triss_i_hand.append(x+1)

def triss():
    if len(triss_i_hand) == 3:
        return True
    else:
        return False


#fyrtal
fyrtal_i_hand=[]
for x in range(12):
    if hand_siffror.count(x+1) == 4:
        fyrtal_i_hand.append(x+1)

def fyrtal():
    if len(fyrtal_i_hand) == 4:
        return True
    else:
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
