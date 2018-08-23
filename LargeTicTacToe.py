def make_board_tictactoe_large(x, y, z, p, q, r, t, u ,v):
    print (" --- --- ---  " * 3)
    print ("| %s | %s | %s | | %s | %s | %s | | %s | %s | %s |" %(x[0][0], x[0][1], x[0][2], y[0][0], y[0][1], y[0][2], z[0][0], z[0][1], z[0][2]))
    print (" --- --- ---  " * 3)
    print ("| %s | %s | %s | | %s | %s | %s | | %s | %s | %s |" %(x[1][0], x[1][1], x[1][2], y[1][0], y[1][1], y[1][2], z[1][0], z[1][1], z[1][2]))
    print (" --- --- ---  " * 3)
    print ("| %s | %s | %s | | %s | %s | %s | | %s | %s | %s |" %(x[2][0], x[2][1], x[2][2], y[2][0], y[2][1], y[2][2], z[2][0], z[2][1], z[2][2]))
    print (" --- --- ---  " * 3)
    print (" --- --- ---  " * 3)
    print ("| %s | %s | %s | | %s | %s | %s | | %s | %s | %s |" %(p[0][0], p[0][1], p[0][2], q[0][0], q[0][1], q[0][2], r[0][0], r[0][1], r[0][2]))
    print (" --- --- ---  " * 3)
    print ("| %s | %s | %s | | %s | %s | %s | | %s | %s | %s |" %(p[1][0], p[1][1], p[1][2], q[1][0], q[1][1], q[1][2], r[1][0], r[1][1], r[1][2]))
    print (" --- --- ---  " * 3)
    print ("| %s | %s | %s | | %s | %s | %s | | %s | %s | %s |" %(p[2][0], p[2][1], p[2][2], q[2][0], q[2][1], q[2][2], r[2][0], r[2][1], r[2][2]))
    print (" --- --- ---  " * 3)
    print (" --- --- ---  " * 3)
    print ("| %s | %s | %s | | %s | %s | %s | | %s | %s | %s |" %(t[0][0], t[0][1], t[0][2], u[0][0], u[0][1], u[0][2], v[0][0], v[0][1], v[0][2]))
    print (" --- --- ---  " * 3)
    print ("| %s | %s | %s | | %s | %s | %s | | %s | %s | %s |" %(t[1][0], t[1][1], t[1][2], u[1][0], u[1][1], u[1][2], v[1][0], v[1][1], v[1][2]))
    print (" --- --- ---  " * 3)
    print ("| %s | %s | %s | | %s | %s | %s | | %s | %s | %s |" %(t[2][0], t[2][1], t[2][2], u[2][0], u[2][1], u[2][2], v[2][0], v[2][1], v[2][2]))
    print (" --- --- ---  " * 3)

def define_board(game):
    for i in range(0,3):
        for j in range(0,3):
            if game[i][j] == " ":
                game[i][j] = "*"

def undefine_board(game):
    for i in range(0,3):
        for j in range(0,3):
            if game[i][j] == "*":
                game[i][j] = " "

def check_win(game):
    no_win = "nowin"
    for i in range(0,2):
        if game[i][0] == game[i][1] == game[i][2] and game[i][0] != " " and game[i][0] != "*":
            return ((game[i][0]))
            break
    for i in range(0,2):
        if game[0][i] == game[1][i] == game[2][i] and game[0][i] != " " and game[0][i] != "*":
            return ((game[0][i]))
            break
    if game[0][0] == game[1][1] == game[2][2] and game[0][0] != " " and game[0][0] != "*":
        return ((game[0][0]))
    elif game[0][2] == game[1][1] == game[2][0] and game[0][2] != " " and game[0][2] != "*":
        return ((game[0][2]))
    else:
        return (no_win)

def xturn(x, y, z, game1, game2, game3, game4, game5, game6, game7, game8, game9, board, count):
    while z:
        make_board_tictactoe_large(game1, game2, game3, game4, game5, game6, game7, game8, game9)
        xcoor = str(input("X give your coordinates in 'row,col' format: "))
        xcoorlist = xcoor.split(",")
        row = int(xcoorlist[0])
        col = int(xcoorlist[1])
        if not row > 3 and not col > 3:
            if board[row - 1][col - 1] == " " or board[row - 1][col - 1] == "*":
                board[row - 1][col - 1] = "X"
                undefine_board(board)
                count += 1
                z = False
                if not row > 3 and not col > 3:
                    if row == 1:
                        if col == 1:
                            if check_win(game1) == "nowin":
                                z = False
                                board = game1
                            else:
                                board = "choose"
                        elif col == 2:
                            if check_win(game2) == "nowin":
                                z = False
                                board = game2
                            else:
                                board = "choose"
                        elif col == 3:
                            if check_win(game3) == "nowin":
                                z = False
                                board = game3
                            else:
                                board = "choose"
                    elif row == 2:
                        if col == 1:
                            if check_win(game4) == "nowin":
                                z = False
                                board = game4
                            else:
                                board = "choose"
                        elif col == 2:
                            if check_win(game5) == "nowin":
                                z = False
                                board = game5
                            else:
                                board = "choose"
                        elif col == 3:
                            if check_win(game6) == "nowin":
                                z = False
                                board = game6
                            else:
                                board = "choose"
                    elif row == 3:
                        if col == 1:
                            if check_win(game7) == "nowin":
                                z = False
                                board = game7
                            else:
                                board = "choose"
                        elif col == 2:
                            if check_win(game8) == "nowin":
                                z = False
                                board = game8
                            else:
                                board = "choose"
                        elif col == 3:
                            if check_win(game9) == "nowin":
                                z = False
                                board = game9
                            else:
                                board = "choose"
            else:
                print ("That place has already been taken, please try again.")
        else:
            print ("That's out of range, please try again")
    return board

def oturn(x, y, z, game1, game2, game3, game4, game5, game6, game7, game8, game9, board, count):
    while y:
        make_board_tictactoe_large(game1, game2, game3, game4, game5, game6, game7, game8, game9)
        ocoor = str(input("O give your coordinates in 'row,col' format: "))
        ocoorlist = ocoor.split(",")
        row = int(ocoorlist[0])
        col = int(ocoorlist[1])
        if not row > 3 and not col > 3:
            if board[row - 1][col - 1] == " " or board[row - 1][col - 1] == "*":
                board[row - 1][col - 1] = "O"
                count += 1
                undefine_board(board)
                y = False
                if not row > 3 and not col > 3:
                    if row == 1:
                        if col == 1:
                            if check_win(game1) == "nowin":
                                z = False
                                board = game1
                            else:
                                board = "choose"
                        elif col == 2:
                            if check_win(game2) == "nowin":
                                z = False
                                board = game2
                            else:
                                board = "choose"
                        elif col == 3:
                            if check_win(game3) == "nowin":
                                z = False
                                board = game3
                            else:
                                board = "choose"
                    elif row == 2:
                        if col == 1:
                            if check_win(game4) == "nowin":
                                z = False
                                board = game4
                            else:
                                board = "choose"
                        elif col == 2:
                            if check_win(game5) == "nowin":
                                z = False
                                board = game5
                            else:
                                board = "choose"
                        elif col == 3:
                            if check_win(game6) == "nowin":
                                z = False
                                board = game6
                            else:
                                board = "choose"
                    elif row == 3:
                        if col == 1:
                            if check_win(game7) == "nowin":
                                z = False
                                board = game7
                            else:
                                board = "choose"
                        elif col == 2:
                            if check_win(game8) == "nowin":
                                z = False
                                board = game8
                            else:
                                board = "choose"
                        elif col == 3:
                            if check_win(game9) == "nowin":
                                z = False
                                board = game9
                            else:
                                board = "choose"
            else:
                print ("That place has already been taken, please try again.")
        else:
            print ("That's out of range, please try again")
    return board

def large_tictactoe():
    count = 0
    entire_game = [[" "," "," "],
    	           [" "," "," "],
    	           [" "," "," "]]

    xwins = [["X","X","X"],
    	     ["X","X","X"],
    	     ["X","X","X"]]

    owins = [["O","O","O"],
    	     ["O","O","O"],
    	     ["O","O","O"]]

    game1 = [[" "," "," "],
    	    [" "," "," "],
    	    [" "," "," "]]

    game2 = [[" "," "," "],
    	    [" "," "," "],
    	    [" "," "," "]]

    game3 = [[" "," "," "],
    	    [" "," "," "],
    	    [" "," "," "]]

    game4 = [[" "," "," "],
    	    [" "," "," "],
    	    [" "," "," "]]

    game5 = [[" "," "," "],
    	    [" "," "," "],
    	    [" "," "," "]]

    game6 = [[" "," "," "],
    	    [" "," "," "],
    	    [" "," "," "]]

    game7 = [[" "," "," "],
    	    [" "," "," "],
    	    [" "," "," "]]

    game8 = [[" "," "," "],
    	    [" "," "," "],
    	    [" "," "," "]]

    game9 = [[" "," "," "],
    	    [" "," "," "],
    	    [" "," "," "]]

    print("Welcome to Tic-Tac-Toe extreme edition!")
    print("X can begin and choose one of the boards he would like to play in!")
    print("Every board is a Tic-Tac-Toe game on its own")
    print("The place in the small board where your opponent places its sign is the place in the big board")
    print("where you have to play next.")
    print("If one player has already won in that place you can choose a new place yourself.")
    print("Your goal is to conquer the entire board!")
    make_board_tictactoe_large(game1, game2, game3, game4, game5, game6, game7, game8, game9)
    z = True
    board = 0
    while z:
        xcoor = str(input("X give your coordinates in 'row,col' format: "))
        xcoorlist = xcoor.split(",")
        row = int(xcoorlist[0])
        col = int(xcoorlist[1])
        if not row > 3 and not col > 3:
            if row == 1:
                if col == 1:
                    z = False
                    print("You have chosen to start in board 1")
                    board = game1
                elif col == 2:
                    z = False
                    print("You have chosen to start in board 2")
                    board = game2
                elif col == 3:
                    z = False
                    print("You have chosen to start in board 3")
                    board = game3
            elif row == 2:
                if col == 1:
                    z = False
                    print("You have chosen to start in board 4")
                    board = game4
                elif col == 2:
                    z = False
                    print("You have chosen to start in board 5")
                    board = game5
                elif col == 3:
                    z = False
                    print("You have chosen to start in board 6")
                    board = game6
            elif row == 3:
                if col == 1:
                    z = False
                    print("You have chosen to start in board 7")
                    board = game7
                elif col == 2:
                    z = False
                    print("You have chosen to start in board 8")
                    board = game8
                elif col == 3:
                    z = False
                    print("You have chosen to start in board 9")
                    board = game9
        else:
            print ("That's out of range, please try again")
    x = True
    y = True
    z = True
    define_board(board)
    while x:
        if check_win(game1) == "X":
            game1 = xwins
            entire_game[0][0] = "X"
        elif check_win(game1) == "O":
            game1 = owins
            entire_game[0][0] = "O"
        if check_win(game2) == "X":
            game2 = xwins
            entire_game[0][1] = "X"
        elif check_win(game2) == "O":
            game2 = owins
            entire_game[0][1] = "O"
        if check_win(game3) == "X":
            game3 = xwins
            entire_game[0][2] = "X"
        elif check_win(game3) == "O":
            game3 = owins
            entire_game[0][2] = "O"
        if check_win(game4) == "X":
            game4 = xwins
            entire_game[1][0] = "X"
        elif check_win(game4) == "O":
            game4 = owins
            entire_game[1][0] = "O"
        if check_win(game5) == "X":
            game5 = xwins
            entire_game[1][1] = "X"
        elif check_win(game5) == "O":
            game5 = owins
            entire_game[1][1] = "O"
        if check_win(game6) == "X":
            game6 = xwins
            entire_game[1][2] = "X"
        elif check_win(game6) == "O":
            game6 = owins
            entire_game[1][2] = "O"
        if check_win(game7) == "X":
            game7 = xwins
            entire_game[2][0] = "X"
        elif check_win(game7) == "O":
            game7 = owins
            entire_game[2][0] = "O"
        if check_win(game8) == "X":
            game8 = xwins
            entire_game[2][1] = "X"
        elif check_win(game8) == "O":
            game8 = owins
            entire_game[2][1] = "O"
        if check_win(game9) == "X":
            game9 = xwins
            entire_game[2][2] = "X"
        elif check_win(game9) == "O":
            game9 = owins
            entire_game[2][2] = "O"
        if check_win(entire_game) == "X":
            make_board_tictactoe_large(game1, game2, game3, game4, game5, game6, game7, game8, game9)
            print("X has won the game! Congratulations")
            x = False
            y = False
            z = False
            e = False
            break
        elif check_win(entire_game) == "O":
            make_board_tictactoe_large(game1, game2, game3, game4, game5, game6, game7, game8, game9)
            print("O has won the game! Congratulations")
            x = False
            y = False
            z = False
            e = False
            break
        board = xturn(x, y, z, game1, game2, game3, game4, game5, game6, game7, game8, game9, board, count)
        if check_win(entire_game) == "X":
            make_board_tictactoe_large(game1, game2, game3, game4, game5, game6, game7, game8, game9)
            print("X has won the game! Congratulations")
            x = False
            y = False
            z = False
            e = False
            break
        elif check_win(entire_game) == "O":
            make_board_tictactoe_large(game1, game2, game3, game4, game5, game6, game7, game8, game9)
            print("O has won the game! Congratulations")
            x = False
            y = False
            z = False
            e = False
            break
        if board == "choose":
            e = True
            while e:
                ocoor = str(input("O please give your coordinates in 'row,col' format for your next board: "))
                ocoorlist = ocoor.split(",")
                row = int(ocoorlist[0])
                col = int(ocoorlist[1])
                if not row > 3 and not col > 3:
                    if row == 1:
                        if col == 1:
                            if check_win(game1) == "nowin":
                                e = False
                                print("You have chosen to play on 1")
                                board = game1
                            else:
                                print("You can't play on that board, please try again!")
                        elif col == 2:
                            if check_win(game2) == "nowin":
                                e = False
                                print("You have chosen to play on 2")
                                board = game2
                            else:
                                print("You can't play on that board, please try again!")
                        elif col == 3:
                            if check_win(game3) == "nowin":
                                e = False
                                print("You have chosen to play on 3")
                                board = game3
                            else:
                                print("You can't play on that board, please try again!")
                    elif row == 2:
                        if col == 1:
                            if check_win(game4) == "nowin":
                                e = False
                                print("You have chosen to play on 4")
                                board = game4
                            else:
                                print("You can't play on that board, please try again!")
                        elif col == 2:
                            if check_win(game5) == "nowin":
                                e = False
                                print("You have chosen to play on 5")
                                board = game5
                            else:
                                print("You can't play on that board, please try again!")
                        elif col == 3:
                            if check_win(game6) == "nowin":
                                e = False
                                print("You have chosen to play on 6")
                                board = game6
                            else:
                                print("You can't play on that board, please try again!")
                    elif row == 3:
                        if col == 1:
                            if check_win(game7) == "nowin":
                                e = False
                                print("You have chosen to play on 7")
                                board = game7
                            else:
                                print("You can't play on that board, please try again!")
                        elif col == 2:
                            if check_win(game8) == "nowin":
                                e = False
                                print("You have chosen to play on 8")
                                board = game8
                            else:
                                print("You can't play on that board, please try again!")
                        elif col == 3:
                            if check_win(game9) == "nowin":
                                e = False
                                print("You have chosen to play on 9")
                                board = game9
                            else:
                                print("You can't play on that board, please try again!")
                else:
                    print ("That's out of range, please try again")

        define_board(board)
        if check_win(game1) == "X":
            game1 = xwins
            entire_game[0][0] = "X"
        elif check_win(game1) == "O":
            game1 = owins
            entire_game[0][0] = "O"
        if check_win(game2) == "X":
            game2 = xwins
            entire_game[0][1] = "X"
        elif check_win(game2) == "O":
            game2 = owins
            entire_game[0][1] = "O"
        if check_win(game3) == "X":
            game3 = xwins
            entire_game[0][2] = "X"
        elif check_win(game3) == "O":
            game3 = owins
            entire_game[0][2] = "O"
        if check_win(game4) == "X":
            game4 = xwins
            entire_game[1][0] = "X"
        elif check_win(game4) == "O":
            game4 = owins
            entire_game[1][0] = "O"
        if check_win(game5) == "X":
            game5 = xwins
            entire_game[1][1] = "X"
        elif check_win(game5) == "O":
            game5 = owins
            entire_game[1][1] = "O"
        if check_win(game6) == "X":
            game6 = xwins
            entire_game[1][2] = "X"
        elif check_win(game6) == "O":
            game6 = owins
            entire_game[1][2] = "O"
        if check_win(game7) == "X":
            game7 = xwins
            entire_game[2][0] = "X"
        elif check_win(game7) == "O":
            game7 = owins
            entire_game[2][0] = "O"
        if check_win(game8) == "X":
            game8 = xwins
            entire_game[2][1] = "X"
        elif check_win(game8) == "O":
            game8 = owins
            entire_game[2][1] = "O"
        if check_win(game9) == "X":
            game9 = xwins
            entire_game[2][2] = "X"
        elif check_win(game9) == "O":
            game9 = owins
            entire_game[2][2] = "O"
        if check_win(entire_game) == "X":
            make_board_tictactoe_large(game1, game2, game3, game4, game5, game6, game7, game8, game9)
            print("X has won the game! Congratulations")
            x = False
            y = False
            z = False
            e = False
            break
        elif check_win(entire_game) == "O":
            make_board_tictactoe_large(game1, game2, game3, game4, game5, game6, game7, game8, game9)
            print("O has won the game! Congratulations")
            x = False
            y = False
            z = False
            e = False
            break
        board = oturn(x, y, z, game1, game2, game3, game4, game5, game6, game7, game8, game9, board, count)
        if check_win(entire_game) == "X":
            make_board_tictactoe_large(game1, game2, game3, game4, game5, game6, game7, game8, game9)
            print("X has won the game! Congratulations")
            x = False
            y = False
            z = False
            e = False
            break
        elif check_win(entire_game) == "O":
            make_board_tictactoe_large(game1, game2, game3, game4, game5, game6, game7, game8, game9)
            print("O has won the game! Congratulations")
            x = False
            y = False
            z = False
            e = False
            break
        if board == "choose":
            e = True
            while e:
                xcoor = str(input("X please give your coordinates in 'row,col' format for your next board: "))
                xcoorlist = xcoor.split(",")
                row = int(xcoorlist[0])
                col = int(xcoorlist[1])
                if not row > 3 and not col > 3:
                    if row == 1:
                        if col == 1:
                            if check_win(game1) == "nowin":
                                e = False
                                print("You have chosen to play on 1")
                                board = game1
                            else:
                                print("You can't play on that board, please try again!")
                        elif col == 2:
                            if check_win(game2) == "nowin":
                                e = False
                                print("You have chosen to play on 2")
                                board = game2
                            else:
                                print("You can't play on that board, please try again!")
                        elif col == 3:
                            if check_win(game3) == "nowin":
                                e = False
                                print("You have chosen to play on 3")
                                board = game3
                            else:
                                print("You can't play on that board, please try again!")
                    elif row == 2:
                        if col == 1:
                            if check_win(game4) == "nowin":
                                e = False
                                print("You have chosen to play on 4")
                                board = game4
                            else:
                                print("You can't play on that board, please try again!")
                        elif col == 2:
                            if check_win(game5) == "nowin":
                                e = False
                                print("You have chosen to play on 5")
                                board = game5
                            else:
                                print("You can't play on that board, please try again!")
                        elif col == 3:
                            if check_win(game6) == "nowin":
                                e = False
                                print("You have chosen to play on 6")
                                board = game6
                            else:
                                print("You can't play on that board, please try again!")
                    elif row == 3:
                        if col == 1:
                            if check_win(game7) == "nowin":
                                e = False
                                print("You have chosen to play on 7")
                                board = game7
                            else:
                                print("You can't play on that board, please try again!")
                        elif col == 2:
                            if check_win(game8) == "nowin":
                                e = False
                                print("You have chosen to play on 8")
                                board = game8
                            else:
                                print("You can't play on that board, please try again!")
                        elif col == 3:
                            if check_win(game9) == "nowin":
                                e = False
                                print("You have chosen to play on 9")
                                board = game9
                            else:
                                print("You can't play on that board, please try again!")
                else:
                    print ("That's out of range, please try again")
        define_board(board)
    print ("The game is over!")

large_tictactoe()
