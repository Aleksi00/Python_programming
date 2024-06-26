def main():
    print("Welcome to the darts calculator! I will keep track of your game of darts.")
    rivi = input("What is the start score of the game?\n")
    alku_pisteet = int(rivi)
    a = alku_pisteet
    round_counter = 0
    while 1>0:
        round_counter = round_counter + 1
        print("Enter the results of your throws for round " + str(round_counter) + ":")
        h_1 = input("Throw 1: ")
        h_2 = input("Throw 2: ")
        h_3 = input("Throw 3: ")
        a = alku_pisteet
        alku_pisteet = alku_pisteet - int(h_1) - int(h_2) - int(h_3)
        if alku_pisteet < 0 or alku_pisteet ==1 :
            print("You have reduced your score to " + str(alku_pisteet) + ". Score resetting to the initial score of the round.")
            alku_pisteet = a
            print("You have "+str(alku_pisteet)+" points remaining.\n")

        else:
            print("You have "+str(alku_pisteet)+" points remaining.")
            if alku_pisteet == 0:
                print("You have won the game after " + str(round_counter) + " rounds. Congratulations!\n")
                break

main()