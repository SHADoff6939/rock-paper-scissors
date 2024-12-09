import random as r


def menu():
    menu_op = ['1. start game', '2.exit']
    for i in menu_op:
        print(i)
    menu_ch = ''
    #retrying to ask user input
    while menu_ch not in range(1, len(menu_op) + 1):
        try:
            menu_ch = int(input('Choose the option: '))
        except ValueError:
            print('please type a number of the choice')
    return menu_ch


def game():
    game_op = ['rock', 'paper', 'scissors']
    p1 = input("Choose your hand (rock, paper, or scissors): ").lower()
    # Validate user input
    while p1 not in game_op:
        p1 = input("Invalid choice. Please choose rock, paper, or scissors: ").lower()
    p2 = r.choice(game_op)
    print('I choose ' + p2 + '!')
    # Determine winner
    if (p1 == 'rock' and p2 == 'scissors') or (p1 == 'paper' and p2 == 'rock') or (p1 == 'scissors' and p2 == 'paper'):
        return True
    elif p1 == p2:
        return None  # No winner in case of a draw
    else:
        return False


if __name__ == '__main__':
    choice = menu()
    if choice == 1:
        while ext := '' != 'exit':
            result = game()
            if result is None:
                print("It's a draw!")
            elif result:
                print('You win!')
            else:
                print("You lose!")
            ext = input('Play again or exit?')
    elif choice == 2:
        print("Exiting the game.")
        exit()
