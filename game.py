

'''I probably did too many choices for my first attempt. I tried to have less code by making elif statements with two variables
for example 'elif choice or sub_choice2 == "PHONE"' , but i couldnt get it to work that way '''


#level 1
#introduction
print("""After an evening out in the city you are on your way home. It is already 3AM and you
are kind of tipsy. You suddenly hear a scream in the near distance. It sounds like a person 
in fear screaming for help.""")

level1_done = False



# if phone path is picked before it will not be available if returned to start

#player input
print("""What do you do?
    INVESTIGATE/PHONE/LEAVE""")
while level1_done == False:



    choice = input("")


    if choice == "INVESTIGATE":
     print("""You move through the quiet streets towards the screams which are getting louder.
    You notice an empty glass bottle lying on the pavement. It could be useful if you need a weapon""")
     print("Pick up empty bottle? (Y/N)")
     sub_choice = input()
     if sub_choice == "Y":
        bottle = True
        print("""You pick up the bottle and move on towards the screams.
        You arrive at an old creepy looking house. There is nobody around,
        but you can hear the screams coming from inside the house""")
        print("""What do you do next?
        KNOCK/BREAK IN/PHONE/LEAVE""")
        sub_choice2 = input()
     else:
        bottle = False
        print("""You leave the bottle lying there and move on towards the screams.
        You arrive at an old creepy looking house. There is nobody around,
        but you can hear the screams coming from inside the house""")
        print("""What do you do next?
        KNOCK/BREAK IN/PHONE/LEAVE""")
        sub_choice2 = input()
     if sub_choice2 == "KNOCK":
             print("""You slowly walk towards the creepy old wooden door and bang against it.
            Nothing happens. You bang again several times but nobody comes. The screams continue though""")
             print("""Try something else
            BREAK IN/PHONE/LEAVE""")
             sub_choice3 = input()
             if sub_choice3 == "BREAK IN":
                print("""You sneak around behind the house and see the basement window half open.
            You forcefully push against it until it snaps and climb through the window.
            You are now inside the basement of the creepy house, but there are still no people in sight""")
                level1_done = True
             elif sub_choice3 == "PHONE":
                print("You take out your phone. Who you gonna call? (GHOSTBUSTERS/POLICE/PLAY)")
             phone_choice = input()
             if phone_choice == "GHOSTBUSTERS":
                print("""nananana nananana nanananana GHOSTBUSTERS nananananana - 
                The screaming person is probably dead now but at least you have a cool song stuck in your head""")
                print("GAME OVER")
                exit()
             elif phone_choice == "POLICE":
                print("""You call the police but they say they will take 10 minutes. It could be too long for the 
                person in danger
                What do you do? (INVESTIGATE/LEAVE)""")
                level1_done = False
             elif phone_choice == "PLAY":
                print("""You see your 'Clash of Clans' notifications on your mobile and hop into the game.
                You forget about space and time while gaming on your phone. Good job nerd, the screaming person is dead""")
                print("GAME OVER")
     elif sub_choice2 == "BREAK IN":
             print("""You sneak around behind the house and see the basement window half open.
            You forcefully push against it until it snaps and climb through the window.
            You are now inside the basement of the creepy house, but there are still no people in sight""")
             level1_done = True
     elif sub_choice2 == "PHONE":
             print("You take out your phone. Who you gonna call? (GHOSTBUSTERS/POLICE/PLAY)")
             phone_choice = input()
             if phone_choice == "GHOSTBUSTERS":
                print("""nananana nananana nanananana GHOSTBUSTERS nananananana - 
                The screaming person is probably dead now but at least you have a cool song stuck in your head""")
                print("GAME OVER")
                exit()
             elif phone_choice == "POLICE":
                print("""You call the police but they say they will take 10 minutes. It could be too long for the 
                person in danger
                What do you do? (INVESTIGATE/LEAVE)""")
                level1_done = False
             elif phone_choice == "PLAY":
                print("""You see your 'Clash of Clans' notifications on your mobile and hop into the game.
                You forget about space and time while gaming on your phone. Good job nerd, the screaming person is dead""")
                print("GAME OVER")
            
    elif choice == "PHONE":                                                                     #tried to do 'elif choice or sub_choice2 == "PHONE"' here, it wouldnt work though
            print("You take out your phone. Who you gonna call? (GHOSTBUSTERS/POLICE/PLAY)")
            phone_choice = input()
            if phone_choice == "GHOSTBUSTERS":
                print("""nananana nananana nanananana GHOSTBUSTERS nananananana - 
                The screaming person is probably dead now but at least you have a cool song stuck in your head""")
                print("GAME OVER")
                exit()
            elif phone_choice == "POLICE":
                print("""You call the police but they say they will take 10 minutes. It could be too long for the 
                person in danger
                What do you do? (INVESTIGATE/LEAVE)""")
                level1_done = False
            elif phone_choice == "PLAY":
                print("""You see your 'Clash of Clans' notifications on your mobile and hop into the game.
                You forget about space and time while gaming on your phone. Good job nerd, the screaming person is dead""")
                print("GAME OVER")
                exit()
    elif choice == "LEAVE":
                 print("You chicken out and go home. The screaming person will probably die")
                 print("GAME OVER")
                 exit()
     # back to start

    
        




        # level 2
level1_done == True
print("""You look around in the dark old basement. There is not much around except an old rusty dagger.
    It could maybe be used as a weapon """)
if bottle == True:
    print("Swap empty bottle for rusty dagger? (Y/N)")
    weapon_choice = input()
    if weapon_choice == "Y":
        print("You leave the empty bottle and pick up the dagger")
    else:
        print("You keep the empty bottle and leave the dagger behind")
elif bottle == False:
    print("Pick up rusty dagger? (Y/N)")
    weapon_choice = input()
    if weapon_choice == "Y":
        print("You pick up the rusty dagger and move on")
    else:
        print("You leave the dagger and move on")