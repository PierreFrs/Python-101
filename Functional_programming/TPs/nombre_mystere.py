import random
import time

def game():
    max_tries, mystery_number, min_num, max_num = init_game()

    for i in range(max_tries):
        player_guess = int(input(f"Veuillez saisir un nombre entier entre {min_num} et {max_num} : "))
        time.sleep(1)
        if is_guess_equal(mystery_number, player_guess):
            print_message(mystery_number, True)
            return
        else : 
            print(give_tip(mystery_number, player_guess))
            if ((max_tries - (i + 1)) > 1):
                print(f"Il vous reste {max_tries - (i + 1)} essais")
                time.sleep(1)
            elif ((max_tries - (i + 1)) == 1):
                print("Attention, il ne vous reste qu'un seul essai !!!")
                time.sleep(1)
            else:
                break

    print_message(mystery_number, False)

def init_game() -> tuple :
    print(f"Bonjour, jouons au nombre mystère.")
    time.sleep(.5)
    max_tries = int(input(f"En combien de manches voulez vous jouer ? "))
    time.sleep(1)
    print(f"Très bien, vous avez {max_tries} essais pour deviner un nombre choisi par l'ordinateur.")
    time.sleep(1)
    min_num = int(input(f"Quel est le nombre minimal à trouver ? "))
    time.sleep(1)
    max_num = int(input(f"Quel est le nombre maximal à trouver ? "))
    time.sleep(1)
    print("Je choisis un nombre...")
    time.sleep(1)
    mystery_number = mystery_number_gen(min_num, max_num)
    print("Très bien j'ai choisi, commençons !")
    time.sleep(1)
    return max_tries, mystery_number, min_num, max_num

def mystery_number_gen(min, max) :
    return random.randint(min, max)

def is_guess_equal(mystery_number : int, player_guess : int) -> bool :
    return player_guess == mystery_number

def give_tip(mystery_number : int, player_guess : int) -> str :
    if mystery_number < player_guess :
        return "Le nombre mystère est plus petit."
    else:
        return "Le nombre mystère est plus grand."

def print_message(mystery_number : int, victory : bool) -> None :
    if victory:
        print(f"Félicitation, le nombre mystère était bien {mystery_number} !")
    else:
        print(f"Désolé, le nombre mystère était {mystery_number}")

game()