list = []
amt = []

while True:
    try:
        item = input('item: ').title()
        if item not in list:
            amt.append(1)
            list.append(item.lower())
        elif item in list:
            for i in range(len(list)):
                if list[i] == item.lower:
                    amt[i] += 1
                    break
    except EOFError:
        for i in range(len(list)):
            print(f"{amt[i]} {list[i].Upper()}")
        break
