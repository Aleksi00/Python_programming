def main():
    rivi = input("Enter the wavelength of the electromagnetic radiation in metres:\n")
    aallonpituus = float(rivi)
    if aallonpituus == 0.0 or aallonpituus <= 0 or aallonpituus > 100000000:
        print("The wavelength doesn't correspond to any type of radiation.")

    if 1 < aallonpituus <= 100000000:
        print("The radiation is radio waves.")

    if 0.001 < aallonpituus <= 1:
        print("The radiation is micro waves.")

    if 7.0*1e-7 < aallonpituus <= 0.001:
        print("The radiation is infrared light.")

    if 4.0*1e-7 < aallonpituus <= 7.0*1e-7:
        print("The radiation is visible light.")
    if 4.0*1e-7 < aallonpituus <= 4.5*1e-7:
        print("The light is violet.")
    if 4.5*1e-7 < aallonpituus <= 4.9*1e-7:
        print("The light is blue.")
    if 4.9*1e-7 < aallonpituus <= 560e-9:
        print("The light is green.")
    if 560e-9 < aallonpituus <= 5.9*1e-7:
        print("The light is yellow.")
    if 5.9*1e-7 < aallonpituus <= 6.3*1e-7:
        print("The light is orange.")
    if 6.3*1e-7 < aallonpituus <= 7.0*1e-7:
        print("The light is red.")

    if 1.0*1e-8 < aallonpituus <= 4.0*1e-7:
        print("The radiation is ultraviolet radiation.")

    if 1.0*1e-11 < aallonpituus <= 1.0*1e-8:
        print("The radiation is X-radiation.")

    if 0.0 < aallonpituus <= 1.0*1e-11:
        print("The radiation is gamma radiation.")
        print("The radiation is highly dangerous!")
main()