def clobber(n, p):

    n = int(input('Enter the number of rows you wish to have in the board: '))
    p = int(input('Enter the number of columns you wish to have in the board: '))

    board = newBoard(n, p)
    display(board, n, p)

    won = False
    turn = 1
    while True:

        print('Player', str(turn))
        player = turn
        s1 = selectPawn(board, n, p, player)

        i = s1[0]
        j = s1[1]

        s2 = selectDestination(board, n, p, player, i, j)
        display(board, n, p)

        turn = playerTurn(player)
        check = again(board, n, p, player)
        if check == True:
            print(again(board, n, p, player))
            turn = playerTurn(player)
        else:
            if player == 1:
                print('Winner: Player 2')
            else:
                print('Winner: Player 1')
            break


def newBoard(n, p):
    board = []
    for i in range(n):
        board.append([])
        for j in range(p):
            if (i + j) % 2 == 0:
                board[i].append(1)
            elif (i + j) % 2 == 1:
                board[i].append(2)
            else:
                board[i].append(0)
    return board


def display(board, n, p):
    pawn = ['.', 'x', 'o']
    for i in range(n):
        for j in range(p):
            if board[i][j] == 1:
                board[i][j] = pawn[1]
            elif board[i][j] == 2:
                board[i][j] = pawn[2]
            elif board[i][j] == 0:
                board[i][j] = pawn[0]
    for row in board:
        print(*row, sep=' ')


def possiblePawn(board, n, p, player, i, j):
    pawn = ['.', 'x', 'o']
    i -= 1
    j -= 1
    if ((i >= 0) and (i <= n)) and (j <= p):
        if board[i][j] == pawn[player]:
            if board[i][j - 1] == pawn[3 - player]:
                return True
            elif board[i][j + 1] == pawn[3 - player]:
                return True
            elif board[i + 1][j] == pawn[3 - player]:
                return True
            elif board[i - 1][j] == pawn[3 - player]:
                return True
            else:
                return False
        else:
            return False;
    return False

def selectPawn(board, n, p, player):
    i = int(input('Select a pawn,row: '))
    j = int(input('Select a pawn,column: '))
    test = possiblePawn(board, n, p, player, i, j)
    list = [i, j]
    while test == False:
        i = int(input('Select a pawn,row: '))
        j = int(input('Select a pawn,column: '))
        test = possiblePawn(board, n, p, player, i, j)
        list = [i,j]
    return list


def possibleDestination(board, n, p, player, i, j, k, l):
    pawn = ['.', 'x', 'o']
    k -= 1
    l -= 1

    #k and l are destination
    #check if k and l are one square within i and j and check if the content are different

    if k >= 0 and k <= n and l >= 0 and l <= p:
        if (abs(i-k) + abs(j-l)) == 1:
            if board[k][l] == pawn[3 - player]:
                return True
    return False


def selectDestination(board, n, p, player, i, j):
    k = int(input('Select a destination,row: '))
    l = int(input('Select a destination,column: '))
    again = possibleDestination(board, n, p, player, i, j, k, l)
    while again == False:
        k = int(input('Select a destination,row: '))
        l = int(input('Select a destination,column: '))
        again = possibleDestination(board, n, p, player, i, j, k, l)
    if player == 1:
        board[k - 1][l - 1] = 1
        board[i - 1][j - 1] = 0
    if player == 2:
        board[k - 1][l - 1] = 2
        board[i - 1][j - 1] = 0


def playerTurn(player):
    if player == 1:
        player = 2
        return player
    else:
        player = 1
        return player


def again(board, n, p, player):
    pawn = ['.', 'x', 'o']
    count_player_1 = 0
    count_player_2 = 0
    count_left = 0
    for i in range(n):
        for j in range(p):
            for k in range(n):
                for l in range(p):
                    if possibleDestination(board, n, p, player, i, j, k, l) == True:
                        return True
    return False


clobber(3, 4)
