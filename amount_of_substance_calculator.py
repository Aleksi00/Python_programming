def alkuaineet(filename):
    with open(filename) as f:
        for i, l in enumerate(f):
            pass
    return i+1

def main():
    name = input("Enter the name of the file with the molar masses:\n")
    dictionary = {}

    try:
        moolimassa_tiedosto = open(name,"r")
        for rivi in moolimassa_tiedosto:
            rivi = rivi.rstrip()
            a = rivi.split(":")

            if len(a) != 2:
                print("Invalid line: '{:s}'".format(rivi))
            else:
                try:
                    float(a[1])
                    nimi = a[0]
                    moolimassa = a[1]

                    if nimi in dictionary:
                        print("A molar mass for {:s} has already been saved in the dictionary ({:.3f} g/mol).".format(nimi,float(dictionary[nimi])))
                        vaihto = input("Should it be replaced by the value {:.3f} g/mol (y/n)?\n".format(float(moolimassa)))
                        if vaihto == "y":
                            dictionary[nimi]=moolimassa
                    else:
                        dictionary[(nimi)] = moolimassa
                except ValueError:
                    print("Invalid molar mass on line: '{:s}'".format(rivi))

        amount = len(dictionary)
        print("Molar masses of {:d} substances were successfully read from the file.".format(amount))
        while True:
            kemiallinen_aine = input("\nEnter the chemical formula of the substance. Stop by entering an empty line.\n")
            while kemiallinen_aine not in dictionary and kemiallinen_aine != "":
                print("A molar mass for '{:s}' could not be found in the file.".format(kemiallinen_aine))
                kemiallinen_aine = input("\nEnter the chemical formula of the substance. Stop by entering an empty line.\n")
            if kemiallinen_aine == "":
                print("Program terminating.")
                return
            muuttuja = True
            while muuttuja:
                massa = input("Enter the mass of the substance (in grams):\n")
                try:
                   if float(massa) < 0:
                       print("The mass needs to be positive or zero!")
                   else:
                       if float(massa) >= 0:
                           muuttuja = False
                       print("{:.3f} grams of {:s} is equal to {:.3f} moles.".format(float(massa), kemiallinen_aine,float(massa) / (float(dictionary[kemiallinen_aine]))))
                except ValueError:
                    print("The mass needs to be a number!")
    except OSError:
        print("File could not be read.")
        print("Program terminating.")

main()