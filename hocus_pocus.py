def main():

    rivi = input("Enter the first number to be printed.\n")
    eka_numero = int(rivi)
    while eka_numero <= 0:
        print("Enter a positive number!")
        rivi = input("Enter the first number to be printed.\n")
        eka_numero = int(rivi)

    rivi_2 = input("Enter the last number to be printed.\n")
    vika_numero = int(rivi_2)
    while vika_numero <= eka_numero:
        print("Enter a number that is larger than the first number!")
        rivi_2 = input("Enter the last number to be printed.\n")
        vika_numero = int(rivi_2)

    print('Hocus pocus between',eka_numero,'-',vika_numero, end='')
    print(':')
    for i in range(eka_numero,vika_numero+1):
        if i % 3 == 0 and i % 5 == 0:
            print("HOCUS POCUS!")
        elif i % 3 == 0:
            print("hocus")
        elif i % 5 == 0:
            print("pocus")
        elif i % 3:
            print(i)

main()

