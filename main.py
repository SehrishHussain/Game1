

def level():
    l = input("Choose a level between 1 & 3:")
    if l.isdigit():
        l = int(l)
        if 1 <= l <= 3:
            return l
        if l > 3:
            print("Invalid input - try again")
            #level()
            break
        elif 1 > l:
            print("Invalid input - try again")
            level()
    elif l.isalpha():
        print("Invalid input - try again")
        return level()
    else:
        print("Invalid input - try again")
        return level()


l1 = level()
print(l1)