def alak(n):
    board = newBoard(n)
    display(board, n)
    removed = removedlist(board, n)

    won = False
    turn = 0
    while won is False:
        if turn % 2 == 0:
            player = 1
            print('Player 1')
            p1 = select(board, n, player, removed)
            removed = removedlist(board,n)
            put(board, n, 1, removed, p1)
            display(board, n)
            won = win(board,n,player)
        else:
            player = 2
            print('Player 2')
            p2 = select(board, n, player, removed)
            removed = removedlist(board,n)
            put(board, n, 2, removed, p2)
            display(board, n)
            won = win(board, n, player)
        turn = turn + 1


def newBoard(n):
    board = []
    while n < 3:
        print('Enter a bigger number of squares')
        n = int(input('Enter the number of squares: '))
    for i in range(0, n):
        board.append(0)
    print("building board...")
    return board


def display(board, n):
    pawn = ['.', 'x', 'o']
    for i in range(len(board)):
        if board[i] == 0:
            board[i] = pawn[0]
        elif board[i] == 1:
            board[i] = pawn[1]
        elif board[i] == 2:
            board[i] = pawn[2]
    place = []
    for i in range(1, (len(board) + 1)):
        place.append(i)
    print("initial board layout...");
    print(*board)
    print(*place)
    return place


def removedlist(board, n):
    pawn = ['.', 'x', 'o']
    removed = []
    for i in range(0, len(board)):
        removed.append(pawn[0])
    return removed


def possible(board, n, player, removed, i):
    i -= 1
    pawn = ['.', 'x', 'o']
    if i < 0 or i >= len(board):
        return False
    elif board[i] == pawn[1] or board[i] == pawn[2]:
        return False
    elif removed[i] == pawn[player]:
        return False
    else:
        return True


def select(board, n, player, removed):
    i = int(input('Choose a licit slot number: '))
    again = possible(board, n, player, removed, i)
    while again == False:
        i = int(input('Choose a licit number slot number: '))
        again = possible(board, n, player, removed, i)
    return i - 1


def put(board, n, player, removed, i):
    pawn = ['.', 'x', 'o']
    if player == 1:
        board[i] = pawn[1]
    if player == 2:
        board[i] = pawn[2]
    capture_enemy(board, i, player, removed)


def get_next_index(board, index, position): # (1) 2 (3) 4 5 6 7 8
    if(position == 'LEFT'):
        if index < 0:
            return len(board) - 1
        else:
            return index - 1
    elif(position == 'RIGHT'):
        if(index >= len(board)):
           return 0;
        else:
            return index + 1

def capture_enemy(board, i, player, removed):
    pawn = ['.', 'x', 'o']
    capturedLeft = []
    capturedRight = []
    player_pawn = pawn[player]
    enemy_pawn = pawn[3 - player]
    # TO THE LEFT
    L = i-1;     #0 1 2 3 4 5 6 7
    while(True):
        if L > 0:
            if board[L] == enemy_pawn:
                capturedLeft.append(L)
            elif board[L] == pawn[0]:
                capturedLeft = []
                break
            elif board[L] == player_pawn:
                break
        L = get_next_index(board, L, 'LEFT')

    #RIGHT
    L = i + 1;
    while(True):
        if L < len(board):
            if board[L] == enemy_pawn:
                capturedRight.append(L)
            elif board[L] == pawn[0]:
                capturedRight = []
                break
            elif board[L] == player_pawn:
                break
        L = get_next_index(board, L, 'RIGHT')
        print("RIGHT BY :", L)


    print("displaying captured by player", player)
    for c in capturedLeft + capturedRight:
        board[c] = pawn[0]
    captured = (capturedLeft + capturedRight)
    for d in range(0, len(board)):
        if d in captured:
            removed[d] = enemy_pawn
    print("removed", removed)


def win(board, n, player):
    pawn = ['.', 'x', 'o']
    count_player_1 = 0;
    count_player_2 = 0;
    count_left = 0
    for i in range(0, len(board)):
        if (board[i] == pawn[1]):
            count_player_1 += 1
        elif (board[i] == pawn[2]):
            count_player_2 += 1
        else:
            count_left += 1
    if count_left == 0:
        if count_player_1 > count_player_2:
            print("player 1 wins")
        elif count_player_2 > count_player_1:
            print("player 2 wins")
        else:
            print("Draw")
        return True
    return False

alak(8)
