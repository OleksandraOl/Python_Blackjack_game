import art
import random
from termcolor import colored


def deal_card():
    """returns a random card from the deck"""
    # jack, queen and king have a value of 10, ace is 11
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    # randomly pick a card from the list
    dealt_card = random.choice(cards)
    return dealt_card


def calc_score(cards):
    """return the sum of the integers in the list"""
    score = sum(cards)

    # check if somebody scored 21 at the beginning
    if score == 21 and len(cards) == 2:
        return 21

    # if score includes 11 and goes over 21, replace 11 with 1
    if 11 in cards and score > 21:
        cards.remove(11)
        cards.append(1)
        score = sum(cards)

    return score


def compare_score(user_final_score, computer_final_score):
    """compares two digits"""
    if user_final_score == computer_final_score:
        return "It's a DRAW!"
    elif computer_final_score == 21:
        return colored("LOSE, opponent has a Blackjack.", "red")
    elif user_final_score == 21:
        return colored("WIN with a Blackjack.", "green")
    elif user_final_score > 21:
        return colored("You went over. You LOSE.", "red")
    elif computer_final_score > 21:
        return colored("Opponent went over. You WIN.", "green")
    elif user_final_score > computer_final_score:
        return colored("You WIN.", "green")
    else:
        return colored("You LOSE.", "red")

def play_game():
    print(art.logo)
    # a list to hold user's cards
    user_hand = []
    # a list to hold computer's cards
    computer_hand = []
    user_score = -1
    computer_score = -1
    is_game_over = False

    # deal the first two cards to the user and computer
    for _ in range(2):
        # generate new card and add to the list
        user_hand.append(deal_card())
        computer_hand.append(deal_card())

    # let user draw
    while not is_game_over:
        # calculate the current score
        user_score = calc_score(user_hand)
        computer_score = calc_score(computer_hand)

        print(f"Your cards: {user_hand}, current_score: {user_score}")
        print(f"Computer's first card: {computer_hand[0]}")

        # check for a blackjack
        if user_score >= 21 or computer_score >= 21:
            is_game_over = True
        # check if user wants to draw more
        else:
            continue_game = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            # add card to the user's list of cards
            if continue_game == 'y':
                user_hand.append(deal_card())
            # exit the loop
            else:
                is_game_over = True


    # let computer draw when user is done and the computers score is less than 17
    while computer_score != 21 and computer_score < 17:
        computer_hand.append(deal_card())
        computer_score = calc_score(computer_hand)

    print("\n")
    print(f"Your final hand: {user_hand}, your final score: {user_score}")
    print(f"Computer's final hand: {computer_hand}, computer's final score: {computer_score}")
    print()
    print("*" * 10 + "  " + compare_score(user_score, computer_score) + "  " + "*" * 10)
    print("\n" * 2)

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower() == 'y':
    print("\n" * 20)
    play_game()