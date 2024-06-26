def main():
    resepti_tiedosto = input("Enter the name of the file containing the recipe:\n")
    try:
        resepti = open(resepti_tiedosto,"r")

        ruuan_nimi = resepti.readline()
        ruuan_nimi = ruuan_nimi.rstrip()

        annos_maara = resepti.readline()
        a = int((annos_maara[0:2]))

        print("This recipe of {:s} makes {:d} servings.".format(ruuan_nimi,a))

        try:
            halutut_annos_maarat = int(input("How many servings do you want to make with this recipe?\n"))
            while halutut_annos_maarat < 1 and halutut_annos_maarat == int(halutut_annos_maarat) :
                print("The amount needs to be positive!")
                halutut_annos_maarat = float(input("How many servings do you want to make with this recipe?\n"))

            while halutut_annos_maarat != int(halutut_annos_maarat):
                print("The amount needs to be an integer!")
                halutut_annos_maarat = int(input("How many servings do you want to make with this recipe?\n"))

        except ValueError:
            print("The amount needs to be an integer!")
            halutut_annos_maarat = int(input("How many servings do you want to make with this recipe?\n"))


        print("\nFor {:d} servings of {:s} you will need:".format(int(halutut_annos_maarat),ruuan_nimi))

        skip_empty_line = resepti.readline()

        for rivi in resepti:
            rivi = rivi.rstrip()
            osat = rivi.split(" ")

            try:
                b = float(osat[0])
                c = (halutut_annos_maarat / a) * b
                uudet_maarat = round(c,1)
                testi = " ".join(osat[1:])
                print('',uudet_maarat,' ',testi,'',sep="")
            except ValueError:
                print(rivi)
        resepti.close()

    except OSError:
        print("File could not be read. Terminating program.")

main()