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

print hand_farg

hand_siffror = []
for a in hand:
    hand_siffror.append(a[1])
#hand_siffror = [6, 3, 6, 6, 6]
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
n = 0
for x in hand_siffror[:-1]:
    if x==hand_siffror[(n+1)]:
        print "pair in", x
    n=n+1




#triss i hand
#vi har problemet att en triss genererar ocksa 2 par då den parar bår position 1,2 och 2,3... vi måste ändra denna kod
n = 0
for x in hand_siffror[:-2]:
    if x==hand_siffror[(n+1)]==hand_siffror[n+2]:
        print "triss in", x
    n=n+1



def farg():
    if hand_farg[0] == hand_farg[1] and hand_farg[1] == hand_farg[2] and hand_farg[2] == hand_farg[3] and hand_farg[3] == hand_farg[4]:
        return True
    else:
        return False


def stege():
    hand_siffror.sort()
    if hand_siffror[n] == hand_siffror[n+1] +1 and hand_siffror[n] == hand_siffror[n+2] +2 and hand_siffror[n] == hand_siffror[n+3] +3 and hand_siffror[n] == hand_siffror[n+4] +4:
        return True
    else:
        return False

#farg ochs stege är inte så svårt att få till, men frågan är om man ska göra det mer generellt? Men att hitta par i en hand med 10 kort kanske kan vara relevant, samma sak du letar efter.
# men om vi letar färg i en hand med 10 kort, letar vi då efter 5 av samma färg eller hela handen(10 kort) i samma färg. Generellt i all ära, men om vi inte ens har definerat vad vi vill
# ha blir det ju lite märkligt att skriva en generell funktion på det. Eftersom du inte finns ett vanligt spel med 10 kort på hand där något heter färg. Min tanke!
            
    
    
    





'''


def triss():
    hand_siffror.sort()
    for n in range(4):
        if hand_siffror[(n-1)] == hand_siffror[n] and hand_siffror[n] == hand_siffror[(n+1)] :
            return True

print triss()




def fyrtal():
    hand_siffror.sort()
    for n in range(4):
        if hand_siffror[(n-1)] == hand_siffror[n] and hand_siffror[n] == hand_siffror[(n+1)] and hand_siffror[(n+1)] == hand_siffror[(n+2)]:
            return True

print fyrtal()

for i in hand_siffror:
    if hand_siffror[i] > 1:
        print "you have pair"


#andring hejhopp


"for par in hand"
 xs=[1,3,2,3,4,6,6,3]
xs.sort()
n = 0
for x in xs[:-2]:
    if x==xs[(n+1)] and x==xs[n+2]:
        print "triple in ", x
    n=n+1


SYNS DET HAR?!?!?
'''
