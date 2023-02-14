while True:
    try:
        level = int(input("Choose a level between 1 and 3:"))
    except ValueError:
        print("Incorrect input - try again")
        continue
    if 0 >= level:
        print("Incorrect input - try again")
        continue
    elif level >= 4:
        print("Incorrect input - try again")
        continue
    else:
        break

if 1 <= level <= 3:
    print("success")
else:
    print("not success")
