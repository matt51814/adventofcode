from collections import Counter

with open('day7-input.txt', 'r') as file:
    puzzle_input = file.read()


print(puzzle_input.split('\n'))
hands = [x.split(' ')[0] for x in puzzle_input.split('\n')]
bids = [int(x.split(' ')[1]) for x in puzzle_input.split('\n')]

card_strength = ['2','3','4','5','6','7','8','9','T','J','Q','K','A']


def primary_rankings(hand):
    counter = Counter(hand)
    if len(counter.values()) == 1:
        # 5 of a kind
        return 1
    elif len(counter.values()) == 2:
        if counter.most_common(1)[0][1] == 4:
            # 4 of a kind
            return 2
        else:
            # full house
            return 3
    elif counter.most_common(1)[0][1] == 3:
        # 3 of a kind
        return 4
    elif len(counter.values()) == 3:
        # 2 pair
        return 5
    elif len(counter.values()) == 4:
        # 1 pair
        return 6
    else:
        # high card
        return 7
    
def secondary_ranking(first_hand, second_hand):
    for i in range(len(first_hand)):        
        if card_strength.index(first_hand[i]) > card_strength.index(second_hand[i]):
            return [first_hand, second_hand]
        elif card_strength.index(second_hand[i]) > card_strength.index(first_hand[i]):
            return [second_hand, first_hand]
    return [first_hand, second_hand]

print(secondary_ranking('KTJJT', 'KK677'))

r1_hands = list(map(primary_rankings, hands))
print(r1_hands)

one_1_hands = [x for x in hands if primary_rankings(x)==1]
two_1_hands = [x for x in hands if primary_rankings(x)==2]
three_1_hands = [x for x in hands if primary_rankings(x)==3]
four_1_hands = [x for x in hands if primary_rankings(x)==4]
five_1_hands = [x for x in hands if primary_rankings(x)==5]
six_1_hands = [x for x in hands if primary_rankings(x)==6]
seven_1_hands = [x for x in hands if primary_rankings(x)==7]

print(one_1_hands)
print(two_1_hands)
print(three_1_hands)
print(four_1_hands)
print(five_1_hands)
print(six_1_hands)
print(seven_1_hands)

# def sort_list(
#         list1,
#         list2
#     ):
 
#     zipped_pairs = zip(list2, list1)
 
#     z = [x for _, x in sorted(zipped_pairs)]
 
#     return z
def sort_list(
        list1,
        list2,
        list3,
        list4,
        list5,
        list6
    ):
 
    zipped_pairs = zip(list2, list3, list4, list5, list6, list1)
 
    z = [x for _, _, _, _, _, x in sorted(zipped_pairs)]
 
    return z

split_hands_lists = [
    one_1_hands, two_1_hands, three_1_hands, four_1_hands, five_1_hands, six_1_hands, seven_1_hands
]
hand_and_ranking = []
card_rank = len(hands)
for hands_list in split_hands_lists:
    if hands_list:
        y2 = [card_strength.index(x[0]) for x in hands_list]
        y3 = [card_strength.index(x[1]) for x in hands_list]
        y4 = [card_strength.index(x[2]) for x in hands_list]
        y5 = [card_strength.index(x[3]) for x in hands_list]
        y6 = [card_strength.index(x[4]) for x in hands_list]


        print(sort_list(hands_list,y2,y3,y4,y5,y6))
        for i in sort_list(hands_list,y2,y3,y4,y5,y6)[::-1]:
            hand_and_ranking.append((i, card_rank))
            card_rank -= 1


print(hand_and_ranking)
winnings_total = 0
print(hands)
print(bids)
for i in hand_and_ranking:
    print(bids[hands.index(i[0])], i[1])
    winnings_total += bids[hands.index(i[0])]*i[1]

print(winnings_total)


# So, the first step is to put the hands in order of strength:

# 32T3K is the only one pair and the other hands are all a stronger type, so it gets rank 1.
# KK677 and KTJJT are both two pair. Their first cards both have the same label, 
# but the second card of KK677 is stronger (K vs T), so KTJJT gets rank 2 and KK677 gets rank 3.
# T55J5 and QQQJA are both three of a kind. QQQJA has a stronger first card, so it gets rank 5 and T55J5 gets rank 4.