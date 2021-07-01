import random


def main():
    pack_of_cards = 4 * ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
    values_of_cards = {'A': 14, 'K': 13, 'Q': 12, 'J': 11, 'T': 10, '9': 9, '8': 8, '7': 7, '6': 6, '5': 5, '4': 4,
                       '3': 3, '2': 2}

    def generate_deck(pack_of_cards: list, number_of_draws: int) -> str:
        """ Generate a randomized deck of cards."""
        player_hand_preslection = []
        player_hand = ''
        random.shuffle(pack_of_cards)
        i = 0
        while i < number_of_draws:
            card = pack_of_cards.pop()
            player_hand_preslection.append(card)
            i += 1
        return player_hand.join(player_hand_preslection)

    Alec_hand = generate_deck(pack_of_cards, 6)
    Bob_hand = generate_deck(pack_of_cards, 6)


    def play_war(Alec_hand:str, Bob_hand:str) -> int:
        """ Evaluation of cards"""
        Alec_points = 0
        Bob_points = 0
        for i in range(0,6):
            if values_of_cards[Alec_hand[i]] > values_of_cards[Bob_hand[i]]:
                Alec_points += 1
            elif values_of_cards[Alec_hand[i]] < values_of_cards[Bob_hand[i]]:
                Bob_points += 1
        if Alec_points > Bob_points:
            print('Alec won.')
            return Alec_points
        elif Alec_points < Bob_points:
            print('Bob won.')
            return Bob_points
        else:
            print('tie')
            return f'{Alec_points}:{Bob_points}'

    print(play_war(Alec_hand, Bob_hand))

main()
