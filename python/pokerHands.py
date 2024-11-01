from collections import Counter
from helpers import *

file_path = "../data/poker.txt"

def parse_poker_hands(file_path):
    with open(file_path, "r") as file:
        hands = []
        for line in file:
            cards = line.strip().split()
            player1_hand = cards[:5]
            player2_hand = cards[5:]
            hands.append((player1_hand, player2_hand))
    return hands

def cardNumericalValue(c):
    if c in ['2','3','4','5','6','7','8','9']:
        return int(c)
    elif c == 'T':
        return 10
    elif c == 'J':
        return 11
    elif c == 'Q':
        return 12
    elif c == 'K':
        return 13
    else:
        return 14
        
def determineHandRanking(ranks, suits):    
    def isFlush(s):
        return len(s) == 1
    def isStraight(r):
        if len(r) == 5:
            vals = list(map(cardNumericalValue, list(r)))
            if 14 in vals:
                vals2 = [1 if val == 14 else val for val in vals]
                if max(vals2) - min(vals2) == 4:
                    return True
            if max(vals) - min(vals) == 4:
                return True
        return False
    
    # straight flush (SF) check
    if isFlush(suits) and isStraight(ranks):
        return 8
    
    # four of a kind (4K) and full house (FH) check
    elif len(ranks) == 2:
        if ranks.most_common(1)[0][1] == 4:
            return 7
        else:
            return 6
        
    # flush (FL) check
    elif isFlush(suits):
        return 5
    
    # straight (ST) check
    elif isStraight(ranks):
        return 4
    
    # three of a kind (3K) and two pair (2P) check
    elif len(ranks) == 3:
        if ranks.most_common(1)[0][1] == 3:
            return 3
        else:
            return 2
    # one pair (OP) check    
    elif len(ranks) == 4:
        return 1
    # high card (HC) check
    else:
        return 0

# Function that returns 1 for player a win; returns 0 for player b win
def handWinner(a, b):
    a_ranks = Counter([card[0] for card in a])
    b_ranks = Counter([card[0] for card in b])
    a_suits = Counter([card[1] for card in a])
    b_suits = Counter([card[1] for card in b])

    aFinal = determineHandRanking(a_ranks, a_suits)
    bFinal = determineHandRanking(b_ranks, b_suits)
        
    if aFinal > bFinal:
        return 1
    elif bFinal > aFinal:
        return 0
    else: #tiebreaker
        if aFinal == 1:  # Both are pairs
            a_pair = int(cardNumericalValue(a_ranks.most_common(2)[0][0]))  # Get the highest pair value for Hand A
            b_pair = int(cardNumericalValue(b_ranks.most_common(2)[0][0]))  # Get the highest pair value for Hand B    
            if a_pair > b_pair:
                return 1  
            elif b_pair > a_pair:
                return 0  
            else:
                a_ranks = a_ranks.most_common()[:-3-1:-1]
                b_ranks = b_ranks.most_common()[:-3-1:-1]

        a_ranks = sorted(map(cardNumericalValue, [card[0] for card in a_ranks]), reverse=True)
        b_ranks = sorted(map(cardNumericalValue, [card[0] for card in b_ranks]), reverse=True)

        for a_card, b_card in zip(a_ranks, b_ranks):
            if a_card > b_card:
                return 1  
            elif b_card > a_card:
                return 0  

wins = 0
hands = parse_poker_hands(file_path)

for i in range(1000):
    wins += handWinner(hands[i][0], hands[i][1])
print(wins)
