separator = (20 * "-")
start = {"a": "", "b": "", "c": "", "d": "", "e": "", "f": "", "g": "",
         "h": "", "i": ""}
players = (1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2)
index = 0
# Players switching
while players:
    player = players[index]
    print(player)
    # Updating of Start dic. - game progress
    while start:
        x = int(input("Place your token pos. 1-9: ")) - 1
        # Checking of correct input value
        if x in range(0, 8):
            arg = "abcdefghi"
            play_arg = arg[x]
            # Deciding if the token will be marked as X or O based on active player
            if play_arg in start.keys():
                if player == 1:
                    start[play_arg] = "X"
                else:
                    start[play_arg] = "O"
        # In case that player place higher number
        else:
            print("Wrong pos. number. PLAY AGAIN or you loose your turn.")
            x = int(input("Place your token pos. 1-9: ")) - 1
            arg = "abcdefghi"
            play_arg = arg[x]
            # Deciding if the token will be marked as X or O based on active player
            if play_arg in start.keys():
                if player == 1:
                    start[play_arg] = "X"
                else:
                    start[play_arg] = "O"
        # Creating a play grid
        grid = "{0:^4}|{1:^5}|{2:^5}\n"\
               "{3:^5}|{4:^5}|{5:^5}\n"\
               "{6:^5}|{7:^5}|{8:^5}".format(start["a"], start["b"], start["c"],
                                             start["d"], start["e"], start["f"],
                                             start["g"], start["h"], start["i"])
        print("\n", grid, "\n")
        break
    index += 1
