def main():
    rivi = input("How much does the apartment cost?\n")
    asunnon_hinta = int(rivi)

    rivi_2 = input("How much is your initial monthly salary?\n")
    kuukausi_palkka = int(rivi_2)

    rivi_3 = input("How many percent does your salary increase per year?\n")
    palkan_kasvu = int(rivi_3)

    rivi_4 = input("And how many percent of your salary will you save?\n")
    saastot_prosentteina = int(rivi_4)

    rivi_5 = input("How much savings do you have?\n")
    saastot = int(rivi_5)

    while asunnon_hinta <= 0 or kuukausi_palkka <= 0 or palkan_kasvu <0 or palkan_kasvu >100 or saastot_prosentteina <0 or saastot_prosentteina >100 or saastot <0:
        print("Enter only positive values and percentages between 0 - 100!")
        rivi = input("How much does the apartment cost?\n")
        asunnon_hinta = int(rivi)

        rivi_2 = input("How much is your initial monthly salary?\n")
        kuukausi_palkka = int(rivi_2)

        rivi_3 = input("How many percent does your salary increase per year?\n")
        palkan_kasvu = int(rivi_3)

        rivi_4 = input("And how many percent of your salary will you save?\n")
        saastot_prosentteina = int(rivi_4)

        rivi_5 = input("How much savings do you have?\n")
        saastot = int(rivi_5)
    rahat = asunnon_hinta - saastot
    tarvittava_summa = asunnon_hinta - saastot
    vuosi = 0
    kuukausi = 0
    a = kuukausi_palkka * (saastot_prosentteina/100)
    b = kuukausi_palkka
    while tarvittava_summa > 0:
        kuukausi = kuukausi + 1
        tarvittava_summa = tarvittava_summa - a
        if kuukausi == 12:
            vuosi = vuosi + 1
            b = kuukausi_palkka * (palkan_kasvu/100+1)**vuosi
            kuukausi = 0
            a = b *(saastot_prosentteina/100)
    print("\n")
    print("You need", rahat, "euros for the apartment.")
    if kuukausi == 0:
        print("It will take you exactly",vuosi,"years to save the money for the apartment.")
    else:
        print("It will take you", vuosi, "years and", kuukausi, "months to save the money for the apartment.")





main()