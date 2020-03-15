num = int(input("Choose from the following:\n0: Rock\n1: Paper\n2: Scissor\n"))

comp = [0, 1, 2]
for item in comp:

    if num == 0:
        if comp[1]:
            print("The computer is Paper. You are Rock. You Lost")
        elif comp[2]:
            print("You are Rock. The computer is scissor. You won")
        else:
            print("You are Rock. The computer is Rock. Its a Tie")
        break

    elif num == 1:
        if comp[item] == num:
            print("The computer is Paper. You are Paper. Its a Tie")
        elif comp[0]:
            print("The computer is Rock. You are Paper. You Won")
        else:
            print("The computer is Scissor. You are Paper. You lost.")
        break

    elif num == 2:
        if comp[0]:
            print("You are Scissor. The computer is Rock. You Lost")
        elif comp[1]:
            print("You are Scissor. The computer is Paper. You Won")
        else:
            print("You are Scissor. The computer is Scissor. Its a Tie")
        break

    else:
        print("Invalid input")
    break