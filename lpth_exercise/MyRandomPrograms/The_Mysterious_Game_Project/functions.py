life = 3
score = 0
level = 1


def mainMenu(score, life, level):
    print(f"\t\t\tLEVEL {level}\t\t\t\n")
    print(f"Your Current Score is: {score}")
    print(f"You have {life} extra lives Remaining!!")
    print("You are infront of a big door of a palace.\nWhat do you want to do?\n")
    choice = (input("> "))
    if choice == "open door" or choice == "open":
        score += 5
        print("Welcome to the Game!!\nYou are now in the palace\n")
        score_life_info(score, life)
        room(score, life, level)
    else:
        loose(score, life)


def room(score, life, level):
    print("\nThere are Three Rooms around you.\nAll the rooms are Numbered as Room-1, Room-2 and Room-3.")
    print("What do you want to do?")
    choice = input("> ")
    if choice == "room-1" or choice == "Room-1":
        room_1(score, life, level)
    #elif choice == "room-2" or choice == "Room-2":
        #room_2(score, life, level)
    else:
        print("Wrong Command!!\nBetter luck next Time\n")
        score_life_info(score, life)


def dead(why):
    print(why)
    print("\n\t\tBETTER LUCK NEXT TIME\t\t\n")


def loose(score, life):
    print(f"You loose!!\nYour Score is still {score}!!")
    life -= 1
    print(f"You have only {life} extra lives Remaining!!\n\n")
    if life > 0:
        print("\n\t\tEXTRA LIFE\t\t\n")
        print(f"You have {life} more chances!!\n")
        mainMenu(score, life, level)
    else:
        print("You Loose!!\nYou Don't have any Extra Lives!!")


def score_life_info(score, life):
    print(f"Your current score is: {score}!!")
    print(f"You Also have {life} extra lives Remaining!!")


############################                 ROOMS              ###################################################

def room_1(score, life, level):
    level += 1
    print(f"\t\t\tLEVEL {level}\t\t\t\n")
    print("\nWelcome to the Room-1\n")
    score += 5
    score_life_info(score, life)
    print("Wow this looks as a Candy Room.\nIt has a lot of yummy candies!!\nAlso, there is a small cupboard and a piano may be a Royal one!!\nSo, what you want to do?")
    choice = input("> ")
    if choice == "eat" or choice == "eat candy":
        print("Delcious!!\nIt was really Delicious!")
        print("Oh No! what's happening to me?\nI am having pain in my stomach.\nwas there any poison or black magic?\nOh shit! I'm Dying!!!")
        dead("You died of poison!!!\nBe careful Next time!!")
        life -= 1
        score_life_info(score, life)
    elif choice == "play" or choice == "play piano":
        print("Great! You decided to play piano.\nLet's play it.")
        print("Playing it!!\nOh No!\nWhat just happened?\nYou beacame a Monkey!!\nIs it some kind of joke?\nI guess it's Black Magic!\nThere might be any witch living in here!\n")
        print("Ha Ha Ha Ha\nLaughing Sound of Witch!!\nWhere is it coming from?\nYou Dumb fellow, You dare to play my piano.\nNow, You are in my Black Magic and you are a Monkey now!!\nHa Ha Ha Ha\nSorry Mam! I didn't knew it was yours.\nPlease forgive me.\nYou dumb fellow I can't do anything for you but you can only come out of this black magic with \"THE GOLDEN MAGICAL RING\"\nIt's difficult to find that but that's your only hope.\nSo, keep exploring this room and you will find a way to the Ring!!")
    elif choice == "open cupboard" or choice == "cupboard":
        print("Amazing! There aren't any cups or clothes in it!!\nJust a Old Diary!!!\nWhat do you want to do?")
        choice = input("> ")
        if choice == "take" or choice == "read":
            score += 5
            print("This is a old diary with a name \"The Mysteries\"")
            score_life_info(score, life)
            print("Really! this diary is saying there is a door in this old cupboard which will take you to The Golde Magical Ring.\nWhat do you want to do now?")
            choice = input("> ")
            if choice == "open" or choice == "open door":
                score += 5
                level += 1
                print(f"\t\t\tLEVEL {level}\t\t\t\n")
                score_life_info(score, life)
                print("Well palyed!! Now, you are in the Jungle !!")
                print("And, There is a horse!!\nWhat do you want to do now?")
            else:
                print("As You Wish!!\n")
                score_life_info(score, life)
                loose(score, life)
        else:
            print("So, You don't want a read that diary.\nSo, you want to be in this room forever!!\nGreat!!")
            score_life_info(score, life)
            # need to import time library so that after certain time you will starve and die
    else:
        print("Sorry! I don't get you\nTry something else!!\nKeep trying!!")
        score_life_info(score, life)