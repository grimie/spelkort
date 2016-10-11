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
