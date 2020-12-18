def sortList(arr):
    arr.sort()
    return arr

for i in range(5):
    cards = (input("Enter the cards: ")).split(",")
    top_card = []
    dealer_cards = []
    cards_same_suit = []
    output = ""
    top_card.append(cards[0])
    top_card.append(cards[1])
    for i in range(10):
        dealer_cards.append(cards[i+2])
    for i in range(len(dealer_cards)):
        if i % 2 == 1:
            if dealer_cards[i] == top_card[1]:
                cards_same_suit.append(dealer_cards[i-1])
                cards_same_suit.append(dealer_cards[i])

    if len(cards_same_suit) == 0:
        output = "NONE"
    else:
        card_numbers = []
        for i in range(len(cards_same_suit)):
            if i % 2 == 0:
                card_numbers.append(int(cards_same_suit[i]))

        card_numbers = sortList(card_numbers)

        bigger_card = False

        for i in range(len(card_numbers)):
            if card_numbers[i] > int(top_card[0]):
                best_card = str(card_numbers[i])+","+top_card[1]
                bigger_card = True
                break

        if bigger_card == True:
            output = best_card
        elif bigger_card == False:
            output = str(card_numbers[0])+","+top_card[1]


    print(output)
