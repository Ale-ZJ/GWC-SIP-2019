#Opens a file. You can now look at each line in the file individually with a statement like "for line in f:
f = open("dictionary.txt","r")

def main():
    print("Can your password survive a dictionary attack?")

    #Take input from the keyboard, storing in the variable test_password
    password = input("Type in a trial password: ").strip().lower() #strip the whitespaces in the password

    test_password(password)

def test_password(password):
    Continue = True
    x = 0

    for line in f:
        if len(line) == len(password):
            for i in range(len(line)):
                if line[i] == password[i]:
                    x += 1
        if x > len(password) // 1.2:
            print("Your password is weak!")
            Continue = False
            break

    if Continue == True:
        print("Wow, your password survived!")


if __name__ == "__main__":
    main()
