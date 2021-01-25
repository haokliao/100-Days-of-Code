import random 
cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]




def deal_card():
    """
    Chooses random number from cards
    """
    card = random.choice(cards)
    return card

def calculate_score(cards):
    """
    Sums scores, changes losing on first turn
    """
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) == 2:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(player1_score,cpu_score):
    """
    This compares scores of p1 and cpu!
    """
    if player1_score == cpu_score:
        return 'It\'s a tie!'
    elif cpu_score == 0:
        return 'The computer got has 21! You lose'
    elif player1_score == 0:
        return 'You\'ve got 21! You WIN!'
    elif player1_score > 21:
        return  'BUST. You LOSE.'
    elif cpu_score > 21:
        return 'The computer has BUST. You WIN.'
    elif player1_score == 21:
        return 'You WIN!!'
    elif player1_score>cpu_score:
        return 'You\'ve beaten the dealer. You WIN!'
    else:
        return 'You lost!'

def play():
    gamestart = True
    player1 = []
    cpu = []

    for i in range(2):
        player1.append(deal_card())
        cpu.append(deal_card())

    while gamestart:

        player1_score = calculate_score(player1)
        cpu_score = calculate_score(cpu)

        print(f'You\'ve drawn {player1} your total is {player1_score}')
        print(f'The dealer\'s first card is {cpu[0]}')

        if player1_score == 0 or cpu_score == 0 or player1_score > 21:
            gamestart= False
        else: 
            agane = input('Would you like to draw another card? Type \'y\' for yes, \'n\' for no. \n')
            if agane == 'y':
                player1.append(deal_card())
            else:
                gamestart = False

    while cpu_score != 0 and cpu_score < 17:
        cpu.append(deal_card())
        cpu_score = calculate_score(cpu)

    print(f'Your final hand was {player1}, your final score was {player1_score}')
    print(f'The dealers hand was {cpu}, their final score was {cpu_score}')
    print(compare(player1_score,cpu_score))

while input('Would you like to play some blackjack? Type \'y\' for yes to begin \n') == 'y': 
    print(chr(27)+'[2j')
    print('\033c')
    print('\x1bc')
    #These three print lines simulate control + l in the console, which clears the console.
    play()
