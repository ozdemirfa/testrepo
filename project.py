import sys
import random
import re
import cowsay

"""
    It is a number guessing game.
    User inputs game level.
    Level defines the digit of the number to be kept.
    User has given a number rounds to find the kept number.
    Round number is calculated regarding the game level
    At every round computer prints a message like;
    +1, -1
    where;
    +1 means one numeral is at the right place and
    -1 means one numeral is at the wrong place.
    0 is not included in the set of numerals.
"""

kept_number=""
round=1
lvl=1

intro=''' Hello, Gamer!
Do you want to play a number game with me?
Basicly, first define the level of the game.
'''
cowsay.cow(intro)

def main():
    """
     : param lvl: digit of the number to be kept
     : type lvl: int [4-6]
     : ValueError: raises ValueError when level is not between 4-6
     : IndexError: raises IndexError when level is input a str
    """
    global kept_number
    global round
    global lvl



    try:
        while True:
            lvl=int(input("Enter difficulty level between 4-6?: "))
            game_lvl(lvl)
            break

    except (IndexError, ValueError):
        print("Difficulty can be between 4-6")
        main()
    else:
        saying=f'''I kept a {lvl} digit number. Make your guess.
         I will moo hints like +2, -1. which means;
         3 numerals in your guess suit my number.
         +:2 at right digit
         -:1 at wrong digit.'''

        cowsay.cow(saying)
        #randomly select a lvl-digited number
        kept_number=pick_number(lvl)

        last3=0
        max_round= int(lvl**2/2)

        #max_round is converted to integer
        if isinstance(max_round, float):
            max_round=round(max_round,0)

        while round <= max_round:
            #control validation of the guess
            while True:
                try:
                    guess=input(f"Guess {lvl} digit number: ")
                    guess_input(guess)
                except ValueError:
                    continue
                else:
                    break

            #compare kept_number and guess
            right, wrong = guess_check(guess, kept_number, round)

            print(f"+{right}, -{wrong}")
            round +=1
            if max_round-round < 4 and last3==0:
                cowsay.cow("Last 3 chances to guess.")
                last3=1

    cowsay.cow(f"End of rounds. The number kept was {kept_number}")
    sys.exit()

def game_lvl(lvl):
    if lvl not in [4,5,6]:
        raise ValueError

def pick_number(lvl) -> str:

    nums=[1,2,3,4,5,6,7,8,9]
    digits=[]

    #no two digits should have use same numerals
    for _ in range(lvl):
        digit=random.choice(nums)
        digits.append(digit)
        nums.remove(digit)

    #generate the number kept by computer
    kept_number=""
    for n in digits:
        kept_number += str(n)

    return kept_number
def guess_input(guess) ->str:
    global lvl

    match lvl:
        case 4:
            if matches := re.search(r"^[1-9]{4}$", guess):
                pass
            else:
                print("Enter a number with 1-9 numerals")
                raise ValueError
        case 5:
            if matches := re.search(r"^[1-9]{5}$", guess):
                pass
            else:
                print("Enter a number with 1-9 numerals")
                raise ValueError
        case _:
            if matches := re.search(r"^[1-9]{6}$", guess):
                pass
            else:
                print("Enter a number with 1-9 numerals")
                raise ValueError

def guess_check(guess, kept_number, round):

    #digit position checkers reset
    right_pos=0
    wrong_pos=0

    if guess == kept_number:
        sys.exit(cowsay.cow(f"Congratulations! You found the number in {round} rounds." ))

    #check for matches for numerals and digit positions
    for g in guess:
        for k in kept_number:
            if g==k:
                if guess.index(g) == kept_number.index(k):
                    right_pos += 1
                    break
                else:
                    wrong_pos +=1
                    break
            else:
                continue

    return right_pos, wrong_pos

if __name__=="__main__":
    main()
