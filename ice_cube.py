SPECIFIC_HEAT_CAPACITY_ICE = 2.09 # ominaislämpökapasiteetti c jäälle, yksikkö kJ / (kg * °C)
SPECIFIC_HEAT_CAPACITY_WATER = 4.1819 # ominaislämpökapasiteetti c vedelle, yksikkö kJ / (kg * °C)
SPECIFIC_HEAT_OF_FUSION_WATER = 333 # ominaissulamislämpö s, yksikkö kJ / kg
SPECIFIC_HEAT_OF_VAPORIZATION_WATER = 2260 # ominaishöyrystymislämpö r, yksikkö kJ / kg

def ice_cube_heating(energy,mass,start_temp,end_temp):
    energia = 0.0
    loppulampotila = 0.0
    if start_temp >=0:
        Q = SPECIFIC_HEAT_CAPACITY_WATER * mass * (end_temp-start_temp)
        energia = float(Q - energy)
        if energia < 0:
            energia = energia *(-1)
            loppulampotila = end_temp
        else:
            loppulampotila = (Q-energia)/(SPECIFIC_HEAT_CAPACITY_WATER*mass)+start_temp
            energia = 0.0
    else:
        Q = SPECIFIC_HEAT_CAPACITY_ICE * mass * (end_temp - start_temp)
        energia = float(Q - energy)
        if energia < 0:
            energia = energia * (-1)
            loppulampotila = end_temp
        else:
            loppulampotila = (Q-energia) / (SPECIFIC_HEAT_CAPACITY_ICE * mass) + start_temp
            energia = 0.0
    return float(energia),float(loppulampotila)

def ice_cube_melting(energy,mass):
    a = False
    Q = SPECIFIC_HEAT_OF_FUSION_WATER * mass
    energia = float(Q - energy)
    if energia <= 0:
        energia = energia *(-1)
        a = True
    else:
        energia = 0.0
    return energia,a

def ice_cube_vaporization(energy,mass):
    a = False
    Q = SPECIFIC_HEAT_OF_VAPORIZATION_WATER * mass
    energia = float(Q - energy)
    if energia <= 0:
        energia = energia * (-1)
        a = True
    else:
        energia = 0.0
    return energia, a


def print_heating_result(energy_total, mass, temp_init, temp_end, melted, vaporized):
    print("With {:.2f} kJ, an ice cube weighing {:.2f} kg heats from {:.2f} °C to {:.2f} °C."
          .format(energy_total, mass, temp_init, temp_end))
    if not melted and not vaporized:
        print("The ice cube stays solid.")
    elif melted and not vaporized:
        print("The ice cube has melted into fluid water.")
    else:
        print("The ice cube has vaporized and is now water vapor.")

def main():
    print("Welcome to the ice cube simulator! I will tell you stats about heating your ice cube.")
    mass = float(input("What is the mass of the ice cube (in kg)?\n"))
    while mass <= 0.0:
        print("Mass cannot be zero or negative!")
        mass = float(input("What is the mass of the ice cube?\n"))
    temp_init = float(input("What is the initial temperature of the ice cube (in °C)?\n"))
    while temp_init < -273.15 or temp_init > 0.0:
        print("The ice cube's temperature can't be under the absolute zero or above 0 degrees!")
        temp_init = float(input("What is the initial temperature of the ice cube (in °C)?\n"))
    energy_total = float(input("What is the total energy used for heating the ice cube (in kJ)?\n"))
    while energy_total < 0.0:
        print("Energy cannot be negative!")
        energy_total = float(input("What is the total energy used for heating the ice cube (in kJ)?\n"))

    melted = False
    vaporized = False
    energy_remaining, end_temp = ice_cube_heating(energy_total, mass, temp_init, 0.0)
    if energy_remaining != 0.0:
        energy_remaining, melted = ice_cube_melting(energy_remaining, mass)
        if energy_remaining != 0.0:
            energy_remaining, end_temp = ice_cube_heating(energy_remaining, mass, 0.0, 100.0)
            if energy_remaining != 0.0:
                energy_remaining, vaporized = ice_cube_vaporization(energy_remaining, mass)

    print_heating_result(energy_total, mass, temp_init, end_temp, melted, vaporized)

main()
