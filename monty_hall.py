import random


def initialize_doors(number_of_doors):
    lista = [False]*number_of_doors
    lista[random.randint(0,number_of_doors-1)]=True
    return lista


def remove_wrong_doors(chosen_door, doors):
    if doors[chosen_door-1]==True:
        i=random.randint(1,len(doors))
        while i == chosen_door:
            i=random.randint(1, len(doors))
    else:
        i = doors.index(True)
        i+=1
    return i


def print_doors(doors, dont_open):
    i = 0
    j = 0
    k = 0
    l = 0
    while i < len(doors):
        print(" _  ", end="")
        i+=1
    print("")

    while j < len(doors):
        if j+1 not in dont_open:
            if doors[j]==True:
                print("|C| ", end="")
            else:
                print("|G| ", end="")
        else:
            print("| | ",end="")
        j+=1
    print("")

    while k < len(doors):
        print("|_| ", end="")
        k+=1
    print("")

    while l < len(doors):
        l+=1
        print("{:^3d} ".format(l),end="")
    print("")

def main():
    seed = int(input("Set seed:\n"))
    random.seed(seed)
    doors = int(input("How many doors?\n"))
    while doors<3 or doors>999:
        print("The number of doors must be between 3-999!")
        doors = int(input("How many doors?\n"))
    numerolista =list(range(1,doors+1))
    ovi_lista = initialize_doors(doors)
    print_doors(ovi_lista, numerolista)
    mika_ovi = int(input("Choose a door 1-{:d}.\n".format(doors)))
    while mika_ovi < 1 or mika_ovi > doors:
        mika_ovi = int(input("Choose a door 1-{:d}.\n".format(doors)))
    print("You chose the door number {:d}.\n".format(mika_ovi))
    poista_vaarat_ovet = remove_wrong_doors(mika_ovi,ovi_lista)
    lista = [mika_ovi,poista_vaarat_ovet]
    print_doors(ovi_lista,lista)
    print("{:d} certainly wrong doors were opened. The door number {:d} was left.".format(doors-2,poista_vaarat_ovet))
    pidatko_oven = int(input("Choose {:d} if you want to keep the door you first chose and choose {:d} if you want to change the door.\n".format(mika_ovi,poista_vaarat_ovet)))
    while pidatko_oven!=mika_ovi and pidatko_oven!=poista_vaarat_ovet:
        pidatko_oven = int(input("Choose {:d} if you want to keep the door you first chose and choose {:d} if you want to change the door.\n".format(mika_ovi, poista_vaarat_ovet)))
    lista_2=[]
    print_doors(ovi_lista,lista_2)
    if ovi_lista[pidatko_oven-1]==False:
        print("A goat emerged from the door you chose! The car was behind the other door :(")
    else:
        print("Congratulations! The car was behind the door you chose!")














main()


