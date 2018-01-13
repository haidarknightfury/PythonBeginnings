def alak(n):
    board = newBoard(n)
    place = display(board,n)
    removed = removedlist(board,n)

    win=False
    turn=0
    while win is False:
        if turn%2==0:
            player=1
            print('Player 1')
            p1 = select(board,n,player,removed)
            put(board,n,1,removed,p1)
            display(board,n)
            #win(board,n)
        else:
            player=2
            print('Player 2')
            p2 = select(board,n,player,removed)
            put(board, n, 2, removed, p2)
            display(board,n)
            #win(board,n)
        turn=turn+1


def newBoard(n):
    board=[]
    while n<3:
        print('Enter a bigger number of squares')
        n=int(input('Enter the number of squares: '))
    for i in range(0,n):
        board.append(0)
    print("building board...")
    return board

def display(board,n):
    pawn=['.','x','o']
    for i in range(len(board)):
        if board[i]==0:
            board[i]=pawn[0]
        elif board[i]==1:
            board[i]=pawn[1]
        elif board[i]==2:
            board[i]=pawn[2]
    place=[]
    for i in range(1,(len(board)+1)):
        place.append(i)
    print ("initial board layout...");
    print(*board)
    print(*place)
    return place
    

def removedlist(board,n):
    pawn=['.','x','o']
    removed=[]
    for i in range(0,len(board)):
        removed.append(pawn[0])
    return removed

def possible(board,n,player,removed,i):
    i-=1
    pawn=['.','x','o']
    if i< 0 or i >= len(board):
        return False
    elif board[i] == pawn[1] or board[i] == pawn[2]:
        return False
    elif removed[i]==pawn[player]:
        return False
    else:
        return True

def select(board, n, player, removed):
    i = int(input('Choose a licit slot number: '))
    again= possible(board,n,player,removed,i)
    while again == False:
        i=int(input('Choose a licit number slot number: '))
        again = possible(board, n, player, removed, i)
    return i-1

def put(board,n,player,removed,i):
    pawn=['.','x','o']
    if player == 1:
        board[i] = pawn[1]
    if player == 2:
        board[i]= pawn[2]
    capture_enemy(board,i,player)

def capture_enemy(board, i, player):
    print("capure enemy")
    pawn = ['.', 'x', 'o']
    capturedLeft = []
    capturedRight = []
    player_pawn = pawn[player]
    enemy_pawn = pawn [3-player]
    #TO THE LEFT
    for a in range(i-1,-1,-1):
        if board[a] == enemy_pawn:
            capturedLeft.append(a)
        elif board [a] == pawn[0]:
            capturedLeft = []
            break
        elif board[a] == player_pawn or (a == 0 and board[a] == enemy_pawn):
            break
    #TO THE RIGHT
    for b in range(i+1, len(board),1):
        if board[b] == enemy_pawn:
            capturedRight.append(b)
        elif board[b] == pawn[0]:
            capturedRight = []
            break
        elif board[b] == player_pawn or (b== len(board)-1 and board(len(board)-1) == enemy_pawn):
            break
    print("displaying captured by player",player)
    for c in capturedLeft+capturedRight:
        board[c]= pawn[0]
    print(capturedLeft+capturedRight)

def capture(board,n,removed,player,i):
    pawn=['.','x','o']
    x=i-2
    if player==1:
        found=False
        for a in range(x,-1,-1):
            if board[a]=='x':
                found=True
                break
            if board[a]=='o':
                found=True
            else:
                found=False
                break
            if found is True:
                for b in range(x,a-1,-1):
                    if board[b]=='o':
                        board[b]='.'
                        removed[b]='o'

            y=i-1
            for a in range(y+1,(len(board))):
                if board[a]=='x':
                    found=True
                    break
            if board[a]=='o':
                found=True
            else:
                found=False
                break

            if found is True:
                for b in range(y+1,(len(board))):
                    if board[b]=='o':
                        board[b]='.'
                        removed[d]='o'

    elif player==2:
        found=False
        for a in range(x,-1,-1):
            if board[a]=='o':
                found=True
                break
            if board[a]=='x':
                found=True
            else:
                found=False
                break
            
            if found is True:
                for b in range(x,a-1,-1):
                    if board[b]=='x':
                        board[b]='.'
                        removed[b]='x'


            y=i-1
            for a in range(y+1,(len(board))):
                if board[a]=='o':
                    found=True
                    break
            if board[a]=='x':
                found=True
            else:
                found=False
                break

            if found is True:
                for b in range(y+1,(len(board))):
                    if board[b]=='x':
                        board[b]='.'
                        removed[d]='x'

def win(board,n):
    board=['x','x','x','0','0','x']
    win=False
    again= not possible(board,n,player,removed,i)
    if player==1 and again is True:
        win=True
    elif player==2 and again is True:
        win=True
    if win is True:
        player1=board.count('x')
        player2=board.count('o')
        if player1>player2:
            print('Winner: ',player)
        elif player2>player1:
            print('Winner: ',player)
        elif player1==player2:
            print('Draw')

alak(8)
                

