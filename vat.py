def main():
    tiedoston_nimi = input("Enter the name of the file containing selling prices.\n")
    summa = 0
    try:
        tiedosto = open(tiedoston_nimi, "r")
        print("    Price       VAT    Price (incl. VAT)")
        for rivi in tiedosto:
            rivi = rivi.rstrip()
            rivi_2 = float(rivi)
            vat = rivi_2 * 0.24
            summa+=vat
            print("{:9.2f} {:9.2f} {:9.2f}".format(rivi_2,vat,(vat+rivi_2)))
        tiedosto.close()
        print("------------------------------------------")
        print("Total VAT {:.2f} eur.".format(summa))
    except OSError:
        print("Error in reading file {:s}. Closing program.".format(tiedoston_nimi))
    except ValueError:
        print("Incorrect line in file {:s}. Closing program.".format(tiedoston_nimi))



main()