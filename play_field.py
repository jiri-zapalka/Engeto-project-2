def tic_tac_toe():
    separator = (20 * "-")
    s = {"a": "", "b": "", "c": "", "d": "", "e": "",
         "f": "", "g": "", "h": "", "i": ""}
    players = ["X", "O"] * 20
    index = 0
    # Players switching
    while players:
        player = players[index]
        print(player)
        # Updating of Start dic. - game progress
        while s:
            # Check if player write only number
            try:
                x = int(input("Place your token pos. 1-9: ")) - 1
            except:
                print("Error: Place only digit from 1 to 9")
            arg = "abcdefghi"
            p_arg = arg[x]
            # Checking of correct input value
            if x in range(0, 9) and s.get(p_arg) == "":
                # Deciding if the token will be marked as X or O based on active player
                if p_arg in s.keys():
                    if player == "X":
                        s[p_arg] = "X"
                    else:
                        s[p_arg] = "O"
            # In case that player place higher or used number
            else:
                print("Place correct token. PLAY AGAIN or you loose your turn.")
                # Check if player write only number
                try:
                    x = int(input("Place your token pos. 1-9: ")) - 1
                except:
                    print("Error: Place only digit from 1 to 9")
                arg = "abcdefghi"
                p_arg = arg[x]
                # Deciding if the token will be marked as X or O based on active player
                if p_arg in s.keys() and s.get(p_arg) == "":
                    if player == "X":
                        s[p_arg] = "X"
                    else:
                        s[p_arg] = "O"
            # Creating a play grid
            grid = "{0:^4}|{1:^5}|{2:^5}\n"\
                   "{3:^5}|{4:^5}|{5:^5}\n"\
                   "{6:^5}|{7:^5}|{8:^5}".format(s["a"], s["b"], s["c"],
                                                 s["d"], s["e"], s["f"],
                                                 s["g"], s["h"], s["i"])
            print(separator, "\n", grid, "\n", separator)
            # winner check
            if s["a"] == s[p_arg] and s["b"] == s[p_arg] and s["c"] == s[p_arg] \
                    or s["d"] == s[p_arg] and s["e"] == s[p_arg] and s["f"] == s[p_arg] \
                    or s["g"] == s[p_arg] and s["h"] == s[p_arg] and s["i"] == s[p_arg] \
                    or s["a"] == s[p_arg] and s["d"] == s[p_arg] and s["g"] == s[p_arg] \
                    or s["b"] == s[p_arg] and s["e"] == s[p_arg] and s["h"] == s[p_arg] \
                    or s["c"] == s[p_arg] and s["f"] == s[p_arg] and s["i"] == s[p_arg] \
                    or s["a"] == s[p_arg] and s["e"] == s[p_arg] and s["i"] == s[p_arg] \
                    or s["c"] == s[p_arg] and s["e"] == s[p_arg] and s["g"] == s[p_arg]:
                print("!!!!Player ", s[p_arg], " WIN!!!!")
                exit()
            elif "" not in s.values():
                print("The game ended in a draw")
                exit()
            else:
                print("Next round.")
            break
        index += 1
    return tic_tac_toe()
