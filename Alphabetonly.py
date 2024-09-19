def inputAlphabetOnly(name):
    while True:
        user_input=input(name)
        if user_input.isnumeric():
            return user_input
        else:
            print("invalid output")

name=inputAlphabetOnly("enter your name = ")
print(f"your name  is ,{name} !")            