from random import randint
cardsNoSuit = ("A","1","2","3","4","5","6","7","8","9","10","J","Q","K")
cards = ["AH", "2H", "3H", "4H", "5H", "6H", "7H", "8H", "9H", "10H", "JH", "QH", "KH","AC", "2C", "3C", "4C", "5C", "6C", "7C", "8C", "9C", "10C", "JC", "QC", "KC","AS", "2S", "3S", "4S", "5S", "6S", "7S", "8S", "9S", "10S", "JS", "QS", "KS","AD", "2D", "3D", "4D", "5D", "6D", "7D", "8D", "9D", "10D", "JD", "QD", "KD"]
hand = []
enemyHand = []
pairValue = []
threeOfAKindValue = []
fourOfAKindValue = []
onePair = False
twoPair = False
threeOfAKind = False
fourOfAKind = False
fullHouse = False

for i in range(1,6):
    randomNum = randint(0, len(cards) - 1)
    hand.append(cards[randomNum])
    cards.remove(cards[randomNum])

for i in range(1,6):
    enemyHand.append(cards[randint(0, len(cards) - 1)])

print "Your hand:"      
print hand


valueCheck = []

for card in hand:
    valueCheck.append(card[0])

for i in range(0,14):
    if valueCheck.count(cardsNoSuit[i]) == 2:
        if cardsNoSuit[i] not in pairValue:
            pairValue.append(cardsNoSuit[i])
    if valueCheck.count(cardsNoSuit[i]) == 3:
        if cardsNoSuit[i] not in threeOfAKindValue:
            threeOfAKindValue.append(cardsNoSuit[i])
    if valueCheck.count(cardsNoSuit[i]) == 4:
        if cardsNoSuit[i] not in fourOfAKindValue:
            fourOfAKindValue.append(cardsNoSuit[i])

if len(pairValue) == 1:
    onePair = True
if len(pairValue) == 2:
    twoPair = True
if len(threeOfAKindValue) == 1:
    threeOfAKind = True
if len(fourOfAKindValue) == 1:
    fourOfAKind = True

if onePair == True and threeOfAKind == True:
    onePair = False
    threeOfAKind = False
    fullHouse = True

if onePair == True:
    print "One pair: %ss" % pairValue[0]
if twoPair == True:
    print "Two pair: %ss, %ss" % (pairValue[0], pairValue[1])
if threeOfAKind == True:
    print "Three of a kind: %ss" % threeOfAKindValue[0]
if fourOfAKind == True:
    print "Four of a kind: %ss" % fourOfAKindValue[0]
if fullHouse == True:
    print "Full house!"
    
print

print "Enemy hand:"
print enemyHand
enemyPairValue = []
enemyThreeOfAKindValue = []
enemyFourOfAKindValue = []
enemyValueCheck = []
enemyOnePair = False
enemyTwoPair = False
enemyThreeOfAKind = False
enemyFourOfAKind = False
enemyFullHouse = False

for card in enemyHand:
    enemyValueCheck.append(card[0])

for i in range(0,14):
    if enemyValueCheck.count(cardsNoSuit[i]) == 2:
        if cardsNoSuit[i] not in pairValue:
            enemyPairValue.append(cardsNoSuit[i])
    if enemyValueCheck.count(cardsNoSuit[i]) == 3:
        if cardsNoSuit[i] not in threeOfAKindValue:
            enemyThreeOfAKindValue.append(cardsNoSuit[i])
    if enemyValueCheck.count(cardsNoSuit[i]) == 4:
        if cardsNoSuit[i] not in fourOfAKindValue:
            enemyFourOfAKindValue.append(cardsNoSuit[i])

if len(enemyPairValue) == 1:
    enemyOnePair = True
if len(enemyPairValue) == 2:
    enemyTwoPair = True
if len(enemyThreeOfAKindValue) == 1:
    enemyThreeOfAKind = True
if len(enemyFourOfAKindValue) == 1:
    enemyFourOfAKind = True

if enemyOnePair == True and enemyThreeOfAKind == True:
    enemyOnePair = False
    enemyThreeOfAKind = False
    enemyFullHouse = True

if enemyOnePair == True:
    print "One pair: %ss" % enemyPairValue[0]
if enemyTwoPair == True:
    print "Two pair: %ss, %ss" % (enemyPairValue[0], enemyPairValue[1])
if enemyThreeOfAKind == True:
    print "Three of a kind: %ss" % enemyThreeOfAKindValue[0]
if enemyFourOfAKind == True:
    print "Four of a kind: %ss" % enemyFourOfAKindValue[0]
if enemyFullHouse == True:
    print "Full house!"

