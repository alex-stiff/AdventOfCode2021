import random

deck_of_cards = [int(x/4) for x in range(8,60)]

random.shuffle(deck_of_cards)

cards_on_display = [deck_of_cards.pop() for x in range(5)]

# print(cards_on_display)

for card_index in range(len(cards_on_display) -1):
    print(f'Your card is {cards_on_display[card_index]}. Higher or lower?')
    choice = random.choice(['higher', 'lower'])
    print(f'{choice}!')