from dice import dice_generator


def read_number():
    try:
        n = int(input())
    except:
        print("Please input an integer")
        n = read_number()
    return n


def read_input_yn():
    try:
        choice = input()
        if  choice != "y" and choice != "n":
            print("Sorry, didn't understand, please input y for yes, n for no")
            choice = read_input_yn()
    except:
        print("There was an error trying to read your input, please try again")
        choice = read_input_yn()
    return choice


def new_game():
    number = dice_generator(1,100)[0]
    print("Try to guess the number!!")
    win = False
    while not win:
        guess = read_number()
        if guess==number:
            win = True
            print("YAY! You guessed it!")
        elif guess > number:
            print("Too high!")
        elif guess < number:
            print("Too low")
    

def main():
    game_on = True
    while game_on:
        new_game()
        print("Do you want to play again?? [y/n]")
        choice = read_input_yn()
        if choice == "n":
            game_on = False

if __name__ == "__main__":
   main()