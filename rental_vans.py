import math
def calculate_cost(consumption,distance,gas_price,rent,time):
    price_for_van = ((distance/100) * consumption)*gas_price + rent * math.ceil(time)
    return price_for_van

def main():
    rivi = input("How much does gas cost (per litre)?\n")
    polttoaineen_hinta = float(rivi)

    rivi_2 = input("Enter the hourly rent for the big van:\n")
    tunnin_vuokra_big = float(rivi_2)

    rivi_3 = input("Enter the estimated rental time (hours) for the big van:\n")
    vuokra_aika_big= float(rivi_3)

    rivi_4 = input("Enter estimated driving distance (km) for the big van:\n")
    ajo_matka_big = float(rivi_4)

    rivi_5 = input("Enter fuel consumption (litres / 100 km) for the big van:\n")
    polttoaineen_kulutus_big = float(rivi_5)

    rivi_6 = input("Enter the hourly rent for the small van:\n")
    tunnin_vuokra_small = float(rivi_6)

    rivi_7 = input("Enter the estimated rental time (hours) for the small van:\n")
    vuokra_aika_small = float(rivi_7)

    rivi_8 = input("Enter estimated driving distance (km) for the small van:\n")
    ajo_matka_small = float(rivi_8)

    rivi_9 = input("Enter fuel consumption (litres / 100 km) for the small van:\n")
    polttoaineen_kulutus_small = float(rivi_9)

    ison_pakun_hinta = calculate_cost(polttoaineen_kulutus_big,ajo_matka_big,polttoaineen_hinta,tunnin_vuokra_big,vuokra_aika_big)
    pienen_pakun_hinta = calculate_cost(polttoaineen_kulutus_small,ajo_matka_small,polttoaineen_hinta,tunnin_vuokra_small,vuokra_aika_small)
    print("Renting the bigger van would cost {:.2f} euros and renting the smaller van would cost {:.2f} euros.".format(ison_pakun_hinta,pienen_pakun_hinta))
    if ison_pakun_hinta <= pienen_pakun_hinta:
        print("You should rent the big van.")
    else:
        print("You should rent the small van.")
main()