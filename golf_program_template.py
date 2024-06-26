# Y1 AUTUMN 2020
# Basic Course in Programming Y1
# Author: Anni Niskanen
# Template for Exercise 9.2


from golfer import Golfer
from golf_course import GolfCourse


def ask_list_of_integers():
    """
    Asks the user for integers separated by commas. Converts the inputted string into a list of integers and
    returns it.
    """
    string = input()
    list_in_characters = string.split(",")  # creates a list
    list_in_integers = []
    for character in list_in_characters:
        list_in_integers.append(int(character))
    return list_in_integers


def main():
    input("Press enter to continue.\n")

    # Create two golfers and one golf course here
    nimi_1 = input("Name of the first golfer:\n")
    nimi_2 = input("Name of the second golfer:\n")
    golf_kurssin_nimi = input("Name of the golf course:\n")
    print("Par scores of the golf course (separated by commas):")
    par = ask_list_of_integers()
    slope = input("Slope rating of the golf course:\n")
    golfari_1 = Golfer(nimi_1)
    golfari_2 = Golfer(nimi_2)
    kentta = GolfCourse(golf_kurssin_nimi, par, int(slope))
    input()
    print("The golfers:")
    print(golfari_1)
    print(golfari_2)
    # Print information about the golfers and the golf course here
    print("\nThe golf course:")
    print(kentta)
    input()
    # The golfers play a round of Golf here
    print("{:s} and {:s} are off to play a round of Golf in {:s}!".format(golfari_1.get_name(),golfari_2.get_name(),kentta.get_name()))
    print("Enter {:s}'s results (separated by commas):".format(golfari_1.get_name()))
    tulokset_1 = ask_list_of_integers()
    print("Enter {:s}'s results (separated by commas):".format(golfari_2.get_name()))
    tulokset_2 = ask_list_of_integers()
    tulos_1 = golfari_1.play_round(kentta,tulokset_1)
    tulos_2 = golfari_2.play_round(kentta,tulokset_2)
    input()
    print("{:s}'s round looks like this:".format(golfari_1.get_name()))
    print(golfari_1.get_round_statistics(kentta,tulokset_1))

    # Print the results of the first golfer here
    input()
    print("And {:s}'s round looks like this:".format(golfari_2.get_name()))
    print(golfari_2.get_round_statistics(kentta, tulokset_2))
    # Print the results of the second golfer here
    input()
    if golfari_1.compare_scores(tulokset_1,tulokset_2):
        print("{:s} won the round!".format(golfari_1.get_name()))
    else:
        print("{:s} won the round!".format(golfari_2.get_name()))
    # Determine and print which golfer won the game here
    input()
    print("The golfers have played {:d} holes in {:s} and count their new handicaps.".format(len(par),golf_kurssin_nimi))
    print("{:s}'s handicap lowered by {:d}.".format(golfari_1.get_name(),tulos_1))
    print("{:s}'s handicap lowered by {:d}.".format(golfari_2.get_name(),tulos_2))
    # Print how much the golfers' handicaps lowered here
    input()
    print("The golfers again:")
    print(golfari_1)
    print(golfari_2)
    # Print information about the golfers again here
    input()
    if golfari_1.compare_golfers(golfari_2):
        print("{:s} has a lower handicap.".format(golfari_1.get_name()))
    else:
        print("{:s} has a lower handicap.".format(golfari_2.get_name()))
    # Comare the golfers with each other and print which one has a lower handicap


main()
