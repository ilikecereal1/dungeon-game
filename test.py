import time

def betterprint(text, char, start, end):
    '''Prints the text with a delay'''
    if char == "":
        betterprint(text, text[0], start, end)
    else:
        print("\r", end="")
        if len(char) == len(text):
            print(text)
            time.sleep(end)
        else:
            print(char, end="")
            time.sleep(start)
            betterprint(text, f"{char}{text[len(char)]}", start, end)

betterprint("Hello World! Welcome to this program.", "", 0.03, 2)
