import random


door1 = 0
door2 = 0
door3 = 0
optional_choice = 0
winning_door = 0
gamer_choice = 0
choice = random.randint(1, 3)
if choice == 1:
    door1 = "car"
    door2 = "goat"
    door3 = "goat"
    winning_door = door1
elif choice == 2:
    door1 = "goat"
    door2 = "car"
    door3 = "goat"
    winning_door = door2
elif choice == 3:
    door1 = "goat"
    door2 = "goat"
    door3 = "car"
    winning_door = door3
choice1 = int(input("Znajdź samochód - wybierz odpowiednie drzwi:\nDrzwi1 - 1\nDrzwi2 - 2\nDrzwi3 - 3\n"))
if choice1 == 1:
    print("Wybrałeś drzwi nr 1.")
    gamer_choice = door1
    if door2 == "goat" and door3 == "goat":
        choice2 = random.randint(2, 3)
        if choice2 == 2:
            print("Uwaga! Pod drzwiami nr 2 kryje się koza.")
            optional_choice = door3
        else:
            print("Uwaga! Pod drzwiami nr 3 kryje się koza.")
            optional_choice = door2
    elif door2 == "goat" and door3 == "car":
        print("Uwaga! Pod drzwiami nr 2 kryje się koza.")
        optional_choice = door3
    elif door2 == "car" and door3 == "goat":
        print("Uwaga! Pod drzwiami nr 3 kryje się koza.")
        optional_choice = door2
elif choice1 == 2:
    print("Wybrałeś drzwi nr 2.")
    gamer_choice = door2
    if door1 == "goat" and door3 == "goat":
        choice2 = 2
        while choice2 == 2:
            choice2 = random.randint(1, 3)
        if choice2 == 1:
            print("Uwaga! Pod drzwiami nr 1 kryje się koza.")
            optional_choice = door3
        else:
            print("Uwaga! Pod drzwiami nr 3 kryje się koza.")
            optional_choice = door1
    elif door1 == "goat" and door3 == "car":
        print("Uwaga! Pod drzwiami nr 1 kryje się koza.")
        optional_choice = door3
    elif door1 == "car" and door3 == "goat":
        print("Uwaga! Pod drzwiami nr 3 kryje się koza.")
        optional_choice = door1
elif choice1 == 3:
    print("Wybrałeś drzwi nr 3.")
    gamer_choice = door3
    if door2 == "goat" and door1 == "goat":
        choice2 = random.randint(1, 2)
        if choice2 == 2:
            print("Uwaga! Pod drzwiami nr 2 kryje się koza.")
            optional_choice = door1
        else:
            print("Uwaga! Pod drzwiami nr 1 kryje się koza.")
            optional_choice = door2
    elif door2 == "goat" and door1 == "car":
        print("Uwaga! Pod drzwiami nr 2 kryje się koza.")
        optional_choice = door1
    elif door2 == "car" and door1 == "goat":
        print("Uwaga! Pod drzwiami nr 1 kryje się koza.")
        optional_choice = door2

final_choice = input("Czy chcesz dokonać zmiany decyzji?\n")
if final_choice == "Tak":
    gamer_choice = optional_choice
    if gamer_choice == winning_door:
        print("Wygrałeś samochód!")
    else:
        print("Przegrałeś.")
else:
    if gamer_choice == winning_door:
        print("Wygrałeś samochód!")
    else:
        print("Przegrałeś.")
