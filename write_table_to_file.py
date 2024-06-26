GAS_CONSTANT = 8.31446261815324 # moolinen kaasuvakio R
def main():
    ainemaara = int(input("What is the amount of substance of the gas (in moles)?\n"))
    alaraja_lampotila = int(input("Enter a lower limit for the temperature (in Kelvins)?\n"))
    ylaraja_lampotila = int(input("Enter a higher limit for the temperature (in Kelvins)?\n"))
    alaraja_tilavuus = int(input("Enter a lower limit for the volume (in cubic metres)?\n"))
    ylaraja_tilavuus = int(input("Enter a higher limit for the volume (in cubic metres)?\n"))
    nimi = input("Enter the name of the file where the table will be written:\n")
    try:
        print("The table was written successfully.")
        print("\nThe file '{:s}' looks like this:".format(nimi))
        tiedosto = open(nimi,"w")
        tiedosto.write("The pressure of {:d} moles of gas between {:d} - {:d} Kelvins and {:d} - {:d} cubic metres, measured in kilopascals\n".format(ainemaara,alaraja_lampotila,ylaraja_lampotila,alaraja_tilavuus,ylaraja_tilavuus))


        tiedosto.close()



    except OSError:
        print("Could not write to file.")



main()