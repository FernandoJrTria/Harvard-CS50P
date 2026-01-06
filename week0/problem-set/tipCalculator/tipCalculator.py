def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    # Remove "$" from str
    dollars = d.replace("$", "")
    
    # turn str into float
    return float(dollars)

def percent_to_float(p):
    # Remove "%" from str
    input = p.replace("%", "")

    # convert str to float and float to percent
    percent = float(input) / 100

    # turn str into float
    return percent


main()