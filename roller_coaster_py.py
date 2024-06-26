def main():
    rivi = input("How many heights will be entered?\n")
    pituuksien_maara = int(rivi)
    a = 0
    while pituuksien_maara <= 0:
        print("Enter a positive value!")
        rivi = input("How many heights will be entered?\n")
        pituuksien_maara = int(rivi)

    print("Enter the heights of the children on separate lines.")

    for i in range(pituuksien_maara):
        rivi= input()
        pituus = int(rivi)
        if pituus >= 140:
            a= a + 1

    print("There are",pituuksien_maara,"children.")
    print(a,"of the children are allowed and",pituuksien_maara-a,"are not allowed on the roller coaster.")

main()