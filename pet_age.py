def dog_age_in_human_years(dog_age):
    if dog_age >= 2:
        dog_age = 15+9+(dog_age-2)*5
    if 0 < dog_age <= 1:
        dog_age = dog_age*15
    if 1 < dog_age < 2:
        dog_age = 15+9*(dog_age-1)
    print("Your dog is {:.1f} years old in human years!".format(float(dog_age)))

def cat_age_in_human_years(cat_age):
    if cat_age >= 2:
        cat_age = 15+10+(cat_age-2)*4
    if 1<cat_age < 2:
        cat_age = 15 + (cat_age-1)*10
    if 0 < cat_age <= 1:
        cat_age = 15*cat_age
    print("Your cat is {:.1f} years old in human years!".format(cat_age))

def bunny_age_in_human_years(bunny_age):
    if bunny_age>=1:
        bunny_age = 16+5+(bunny_age-1)*6
    if 0.5<bunny_age<1:
        bunny_age=((bunny_age*12-6)/6)*5+16
    if 0<bunny_age<=0.5:
        bunny_age = (16*bunny_age)*2
    print("Your bunny is {:.1f} years old in human years!".format(bunny_age))


def main():
    print("Welcome to the pet age calculator! I will tell your pet's age in human years.")
    choice = 0
    while not 1 <= choice <= 3:
        print("Choose a pet:\n"
              "1: dog\n"
              "2: cat\n"
              "3: bunny")
        choice = int(input())
    age = float(input("How old is your pet?\n"))
    if choice == 1:
        dog_age_in_human_years(age)
    elif choice == 2:
        cat_age_in_human_years(age)
    else:
        bunny_age_in_human_years(age)

main()