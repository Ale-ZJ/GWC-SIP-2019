x = True

print("One day you are walking down a street and you meet with your friend, the cat")
print ("The cat has a free concert ticket for you.")


while x == True:
    ticket= input("Press 1 for Exo concert or 2 for Taylor Swift concert: ")

    if ticket == "exit":
        break

    if not ticket.isnumeric():
        print("That wasn't an option :c")

    else:
        ticket= int(ticket)

        if ticket ==1:
            print("You're at an EXO concert!")
            action = input("Do you want to sing(1) or use your lightstick(2)? ")
            action = int(action)
            if action == 1:
                print("It's the love shot Na nanana nananana nanana nanana Na nanana nananana Oh oh oh oh oh~")
            elif action == 2:
                print("*Furiously waving lightstick*")
            x == False

        elif ticket ==2:
            print("You're at a Taylor swift concert!")
            paper = input("Do you want to sing(1) or Dance(2)?")
            paper = int(paper)
            if paper ==1:
                print("You belong with me~")
            elif paper== 2:
                print("*Furiously dancing*")
            x == False

        else:
            print("That wasn't in the option")

    store = input("Do you want to go to the merchandise store? (1yes/ 0no)")
    store = int(store)
    if store == 1:
        print("OH all the stuff is too expensive! Too bad I'm broke...well... bye!")
    elif store ==0:
        print("*Jin wink wink*")
    break

print("Thanks for playing!")
