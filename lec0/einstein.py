def main():
    mass = int(input("input mass value: ")) # units of mass in kg
    print(equation(mass))

def equation(mass):
    light = 300000000 # speed of light
    energy = mass * pow(light, 2)
    return energy


main()