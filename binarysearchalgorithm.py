

a = 81
print("Liczba wygenerowana przez komputer to", a)
minimum = 1
maximum = 100
choice = int((minimum+maximum)/2)  # average = choice
print("Zgaduję, że liczba to", choice)
while choice != a:
    if choice > a:
        print("Liczba za duża")
        maximum = choice - 1
        choice = int((minimum + maximum) / 2)
        print("Zgaduję, że liczba to", choice)
    elif choice < a:
        print("Liczba za mała")
        minimum = choice + 1
        choice = int((minimum + maximum) / 2)
        print("Zgaduję, że liczba to", choice)
else:
    print("To ta liczba")

waiting = input()
