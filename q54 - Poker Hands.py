def appears(n,lst):
    a = 0
    for k in lst:
        if k == n:
            a += 1
    return (a,n)

def copy_lists(lst1):
    lst2 = []
    for k in lst1:
        lst2.append(k)
    return lst2
def three_of_a_kind(values):
    maxi = 0
    m_max = []
    for k in values:
        m = appears(k,values)
        if m[0] > maxi:
            maxi = m[0]
            m_max = m
    if maxi == 3:
        return m_max[1]
    return 0

def four_of_a_kind(values):
    maxi = 0
    m_max = []
    for k in values:
        m = appears(k,values)
        if m[0] > maxi:
            maxi = m[0]
            m_max = m
    if maxi == 4:
        return m_max[1]
    return 0

def pair(values):
    maxi = 0
    m_max = []
    for k in values:
        m = appears(k, values)
        if m[0] > maxi:
            maxi = m[0]
            m_max = m
    if maxi == 2:
        return m_max[1]
    return 0

def two_pairs(values):
    x = pair(values)
    if x != 0:
        while x in values:
            values.remove(x)
        y = pair(values)
        if y != 0:
            return (max(x,y),min(x,y))
    return 0

def straight(values):
    values = sorted(values)
    x = values[0]
    for k in range(5):
        if values[k] != k + x:
            return 0
    return values[4]

def full_house(values):
    x = three_of_a_kind(values)
    if x != 0:
        while x in values:
            values.remove(x)
        y = pair(values)
        if y != 0:
            return (x,y)
    return 0

def same_suit(suits):
    for a in suits:
        if a != suits[0]:
            return False
    return True

def rank(hand):
    value1 = []
    suit = []
    for card in hand:
        suit.append(card[1])
        value_card = card[0]
        if value_card == "T":
            value1.append(10)
        elif value_card == "J":
            value1.append(11)
        elif value_card == "Q":
            value1.append(12)
        elif value_card == "K":
            value1.append(13)
        elif value_card == "A":
            value1.append(14)
        else:
            value1.append(int(value_card))
    value = copy_lists(value1)
    if same_suit(suit) and straight(value) == 14:
        return (100,0,0)
    if straight(value) != 0 and same_suit(suit):
        return (22,straight(value),0)
    if four_of_a_kind(value) != 0:
        return (21,four_of_a_kind(value),0)
    x = full_house(value)
    if x != 0:
        return (20,x[0],x[1])
    value = copy_lists(value1)
    if same_suit(suit):
        m1 = max(value)
        value.remove(m1)
        m2 = max(value)
        return (19,m1,m2)
    value = copy_lists(value1)
    if straight(value) != 0:
        return (18,straight(value),0)
    value = copy_lists(value1)
    if three_of_a_kind(value) != 0:
        t = three_of_a_kind(value)
        while t in value:
            value.remove(t)
        return (17,t,max(value))
    x = two_pairs(value)
    if x != 0:
        return (16,x[0],x[1])
    value = copy_lists(value1)
    if pair(value) != 0:
        m = pair(value)
        value.remove(m)
        value.remove(m)
        m1 = max(value)
        return (15,m,m1)
    else:
        m1 = max(value)
        value.remove(m1)
        m2 = max(value)
        value.remove(m2)
        return (m1,m2,max(value))

file = open("0054_poker.txt","r")
string = file.read()
rounds = []
current_round = []
current_hand = []
current_card = ""
cards = 0
for char in string:
    if char == " ":
        current_hand.append(current_card)
        current_card = ""
        if cards == 4:
            current_round.append(current_hand)
            current_hand = []
            cards = 0
        else:
            cards += 1
    elif char == "\n":
        current_hand.append(current_card)
        current_round.append(current_hand)
        rounds.append(current_round)
        current_round = []
        current_hand = []
        current_card = ""
        cards = 0
    else:
        current_card += char

wins = 0
for round in rounds:
    player1 = rank(round[0])
    player2 = rank(round[1])
    if player1[0] > player2[0]:
        wins += 1
    elif player1[0] == player2[0]:
        if player1[1] > player2[1]:
            wins += 1
        elif player1[1] == player2[1]:
            if player1[2] > player2[2]:
                wins += 1
print(wins)

#answer = 376