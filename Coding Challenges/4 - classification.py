if input("Does it have 4 legs?")=="y":
    if input("Is it a farm animal?")=="y":
        if input("Does it produce milk?")=="y":
            if input("Does it also produce wool?")=="y":
                print("you are thinking of a sheep")
            else:
                print("you are thinking of a cow")
        else:
            if input("Is it pink?")=="y":
                print("you are thinking of a pig")
            else:
                print("you are thinking of a horse")
    else:
        if input("Is it a common pet?")=="y":
            if input("Does it bark?")=="y":
                print("you are thinking of a dog")
            else:
                print("you are thinking of a cat")
        else:
            if input("Does it have a mane?")=="y":
                print("you are thinking of a lion")
            else:
                print("you are thinking of a tiger")
else:
    if input("Is it a bug?")=="y":
        if input("Does it sting?")=="y":
            if input("Does it produce honey?")=="y":
                print("you are thinking of a bee")
            else:
                print("you are thinking of a wasp")
        else:
            if input("Does it have 6 legs?")=="y":
                if input("Does it form colonies?")=="y":
                    print("you are thinking of an ant")
                else:
                    print("you are thinking of a termite")
            else:
                print("you are thinking of a spider")
    else:
        if input("Is it a bird?")=="y":
            if input("Does it fly?")=="y":
                print("you are thinking of a sparrow")
            else:
                if input("Does it live in cold climates?")=="y":
                    print("you are thinking of a penguin")
                else:
                    print("you are thinking of a ostrich")
        else:
            if input("Is it a mammal?")=="y":
                if input("Does it go arf?")=="y":
                    print("you are thinking of a seal")
                else:
                    if input("Is it big?")=="y":
                        print("you are thinking of a whale")
                    else:
                        print("you are thinking of a dolphin")
            else:
                if input("Does it have tentacles?")=="y":
                    print("you are thinking of a squid")
                else:
                    print("you are thinking of an octopus")
            
