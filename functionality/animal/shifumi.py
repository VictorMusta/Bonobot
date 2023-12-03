from random import randint
import time
data = {"1": "pierre", "2": "feuille", "3": "ciseaux"}


def shifumi_menu():
    print("Bienvenu dans mon jeu shifumi!")
    print("chaque round tu vas te battre contre moi, tu vas devoir choisir entre 'pierre', 'feuille' et 'ciseaux'.")
    print("Bonne chance! :)")
    play_round()


def play_round():
    computer_choice = data[str(randint(1, 3))]
    human_choice = input('"pierre", "feuille", "ciseaux"')
    for choice in data.keys():
        print(choice)
        time.sleep(0.5)
    print("TU AS FAIS :"+human_choice)
    print("J\'AI FAIS :"+computer_choice)
    if human_choice == "pierre":
        if computer_choice == "feuille":
            loose()
        if computer_choice == "pierre":
            equal()
        if computer_choice == "ciseaux":
            win()
    if human_choice == "feuille":
        if computer_choice == "ciseaux":
            loose()
        if computer_choice == "pierre":
            win()
        if computer_choice == "feuille":
            equal()
    if human_choice == "ciseaux":
        if computer_choice == "feuille":
            win()
        if computer_choice == "pierre":
            loose()
        if computer_choice == "ciseaux":
            equal()
    else:
        print("concentre toi stp")


def equal():
    print("EGALITEEEEEEE")
    exit()


def loose():
    print("LOOOSER MDR")
    exit()


def win():
    print("GG MAH BOY TA DEAD CA CHACAL")
    exit()


if __name__ == '__main__':
    shifumi_menu()
