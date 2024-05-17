#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
#Hint 5: Deal the user and computer 2 cards each using deal_card()
#Hint 6: Create a function called calculate_score() that takes a List of cards as input 
#and returns the score. 
#Look up the sum() function to help you do this.
#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.
#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().
#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.
#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.
#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.
#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.
#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.
#Bug fix. If you and the computer are both over, you lose.
#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.


import random
from art import logo
import os
clear = lambda: os.system('cls')


print(logo)


def deal_card():
    """Returns a random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 11, 10]
    card = random.choice(cards)
    #Pop the chosen card from the deck to shorten it...
    return card


def calculate_score(list):
    score = sum(list)
    
    if score >= 21 and len(list) == 2:
        return 0    #Natural Blackjack by having [11, 10]
    
    elif score > 21 and 11 in list:
        index = list.index(11)
        list.remove(11)
        list.insert(index, 1)
        score = sum(list)
        return score
    
    else:
        return score


def compare(user_score, computer_score):

    if computer_score == 0:
        print("Opponent got blackjack. You lose 😭")
    elif user_score == 0:
        print("You got blackjack 😱")
    elif user_score > computer_score:
        print("You win 😃")
    elif computer_score > user_score:
        print("You lose 🫣")
    elif computer_score > 21:
        print("Opponent went over. You win 😁")
    elif user_score > 21:
        print("You went over. You lose 🥲")
    elif user_score == computer_score:
        print("Draw 🙃")
    elif computer_score > 21 and user_score > 21:   #Bug fixed
        print("You went over. You lose 🥲")


def main():
    choice = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    
    while choice != "n":
        
        game_ended = False
        
        if choice == "n":
            break
        
        else:
            if choice == "y":
                clear
                Users_List = []
                Computers_List = []
                
                for i in range(0, 2):
                    Users_List.append(deal_card())
                    Computers_List.append(deal_card())
                    Users_score = calculate_score(Users_List)
                    Computers_score = calculate_score(Computers_List)
                print("Your cards: " + str(Users_List) + ", current score: " + str(Users_score))
                print("Computer's first card: " + str(Computers_List[0]))
                
                while not game_ended:
                    
                    ingame_choice = input("Type 'y' to get another card, type 'n' to pass: ")
                    
                    if ingame_choice == "n":
                        Computers_List.append(deal_card())
                        Computers_score = calculate_score(Computers_List)
                        print("Your final hand: " + str(Users_List) + ", final score: " + str(Users_score))
                        print("Computer's final hand " + str(Computers_List) + ", final score " + str(Computers_score))
                        compare(Users_score, Computers_score)
                        game_ended = True
                        choice = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
                    
                    else:
                        if ingame_choice == "y":
                            Users_List.append(deal_card())
                            Users_score = calculate_score(Users_List)
                            Computers_List.append(deal_card())
                            Computers_score = calculate_score(Computers_List)
                            
                            if Users_score < 21 and Computers_score < 21:
                                print("Your hand: " + str(Users_List) + ", final score: " + str(Users_score))
                                print("Computer's first card: " + str(Computers_List[0]))
                                game_ended = False
                            
                            elif Users_score >= 21 or Computers_score >= 21:
                                print("Your final hand: " + str(Users_List) + ", final score: " + str(Users_score))
                                print("Computer's final hand " + str(Computers_List) + ", final score " + str(Computers_score))
                                compare(Users_score, Computers_score)
                                game_ended = True
                                choice = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")


main()