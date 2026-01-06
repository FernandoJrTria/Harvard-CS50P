def convert(text):
    result = text.replace(":)", "\U0001F642")
    result = result.replace(":(", "\U0001F641")

    return result

def main():
    # ask for user input with ": )" or ": ("
    text = input()

    # print converted text
    print(convert(text))

main()