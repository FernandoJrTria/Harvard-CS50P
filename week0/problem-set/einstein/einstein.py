def multiply(a, b):
    return a * b

def main():
    print("E = mc^2 \n")

    # prompt user to input mass in kg
    mass = int(input("Mass in Kg: "))

    speedOfLight = 300000000 * 300000000

    energy = multiply(mass, speedOfLight)

    print(f"{energy:,}")

main()