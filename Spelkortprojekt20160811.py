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
hand_siffror = [1, 2, 3, 4, 5]
#[1, 2, 3, 4]

print hand_siffror

'''
def par():
    hand_siffror.sort()
    langd = len(hand_siffror)
    for n in range(langd-1):
        if hand_siffror[n] == hand_siffror[n+1]:
            return True
    return False
    if hand_siffror[0] == hand_siffror[1]:
        return True
    elif hand_siffror[1] == hand_siffror[2]:
        return True
    elif hand_siffror[2] == hand_siffror[3]:
        return True
    elif hand_siffror[3] == hand_siffror[4]:
        return True
    else:
        return False
print "par", par()
'''

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

            print "Par i", (x+1)
    print par_i_hand
print samlingar()

def par():
    if len(par_i_hand) == 1:
        return True
    else:
        return False

def tvapar():
    if len(par_i_hand) == 2:
        return True
    else:
        return False



triss_i_hand=[]
def triss():
    for x in range(12):
        if hand_siffror.count(x+1) == 3:
            triss_i_hand.append(x+1)
            print "Triss i", x+1
    print triss_i_hand

print triss()


#full-house
def full_house():
    if par() == True and triss() == True:
        return True
print "du har full-house i", triss_i_hand, "och", par_i_hand




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


print stege()
#farg ochs stege ar inte sa svart att fa till, men fragan ar om man ska gora det mer generellt? Men att hitta par i en hand med 10 kort kanske kan vara relevant, samma sak du letar efter.
# men om vi letar farg i en hand med 10 kort, letar vi da efter 5 av samma farg eller hela handen(10 kort) i samma farg. Generellt i all ara, men om vi inte ens har definerat vad vi vill
# ha blir det ju lite markligt att skriva en generell funktion pa det. Eftersom du inte finns ett vanligt spel med 10 kort pa hand dar nagot heter farg. Min tanke!









'''
def fyrtal():
    hand_siffror.sort()
    for n in range(4):
        if hand_siffror[(n-1)] == hand_siffror[n] and hand_siffror[n] == hand_siffror[(n+1)] and hand_siffror[(n+1)] == hand_siffror[(n+2)]:
            return True

print fyrtal()

for i in hand_siffror:
    if hand_siffror[i] > 1:
        print "you have pair"


'''
