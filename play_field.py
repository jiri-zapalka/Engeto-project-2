separator = (20 * "-")
start = {"a": "", "b": "", "c": "", "d": "", "e": "", "f": "", "g": "",
         "h": "", "i": ""}
while start:
    players = input("player nr. 1 or 2: ")
    x = int(input("vlož číslo pozice: ")) - 1
    arg = "abcdefghi"
    play_arg = arg[x]
    if play_arg in start.keys():
        if players == "1":
            start[play_arg] = "X"
        else:
            start[play_arg] = "O"
    grid = "{0:^4}|{1:^5}|{2:^5}\n" \
          "{3:^5}|{4:^5}|{5:^5}\n" \
          "{6:^5}|{7:^5}|{8:^5}".format(start["a"], start["b"], start["c"],
                                        start["d"], start["e"], start["f"],
                                        start["g"], start["h"], start["i"])
    print(separator, "\n", grid, "\n", separator)
