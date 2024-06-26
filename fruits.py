def main():
    rivi_1 = input("How much money do you have?\n")
    rahan_maara = float(rivi_1)
    banaanin_paino = rahan_maara / 1.49
    banaanin_maara = banaanin_paino // 0.17
    print("You can buy ",banaanin_maara," bananas")
    omenan_paino = rahan_maara / 2.49
    omenan_maara = omenan_paino // 0.17
    print("You can buy ",omenan_maara," apples")
    appelsiinin_paino = rahan_maara / 1.99
    appelsiinin_maaara = appelsiinin_paino // 0.27
    print("You can buy ",appelsiinin_maaara," oranges")
main()