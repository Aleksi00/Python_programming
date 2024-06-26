def main():
    osallistujat = int(input("Enter the number of the participants.\n"))
    while osallistujat < 2:
        print("The number must be at least 2!")
        osallistujat = int(input("Enter the number of the participants.\n"))
    laskuri = 0
    i = 0
    summa = 0.0
    lista = []
    while i < osallistujat:
        raha_summat = float(input("Enter the sum (eur) paid by participant no {:d}.\n".format(laskuri+1)))
        laskuri = laskuri + 1
        lista.append(raha_summat)
        summa = summa + lista[i]
        i = i + 1
    keskiarvo = summa / osallistujat
    print("Total costs are {:.2f} eur.".format(summa))
    j = 1
    for osallistujat in lista:
        if osallistujat < keskiarvo:
            print("Participant no {:d} should pay {:.2f} eur.".format(j,keskiarvo-osallistujat))
        else:
            print("Participant no {:d} should receive {:.2f} eur.".format(j,osallistujat-keskiarvo))
        j+=1

main()
