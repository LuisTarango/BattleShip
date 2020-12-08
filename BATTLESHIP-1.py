def main ():
    global archivos
    option=0    
    while option == 0:
        print("Game Menu")
        print("1 - Load archives")
        print("2 - Play Game")
        print("3 - Exit\n")
        option=int(input())
    if option == 1:
        load_archives()
    elif option == 2:
        if archives == True:
            start_game()
        else:
            print("You haven't loaded the archives\n")
            main()
    elif option == 3:
        exit()
    else:
        print("Invaid option\n")
        main()
        
def load_archives():
    global archives
    global board1
    global board2
    global hitboard1
    global hitboard2
    board1=[]
    board2=[]
    hitboard1=[['-',"-","-","-","-","-","-"],
                  ["-","-","-","-","-","-","-"],
                  ["-","-","-","-","-","-","-"],
                  ["-","-","-","-","-","-","-"],
                  ["-","-","-","-","-","-","-"],
                  ["-","-","-","-","-","-","-"],
                  ["-","-","-","-","-","-","-"]]
    hitboard2=[["-","-","-","-","-","-","-"],
                  ["-","-","-","-","-","-","-"],
                  ["-","-","-","-","-","-","-"],
                  ["-","-","-","-","-","-","-"],
                  ["-","-","-","-","-","-","-"],
                  ["-","-","-","-","-","-","-"],
                  ["-","-","-","-","-","-","-"]]
    i=1
    with open ('Tablero1.txt','r') as Tab1:
        while i > 0:
            linea=list(Tab1.readline())
            if len (linea)==0:
                break
            else:
                board1.append(linea[0:13:2])
    with open ('Tablero2.txt','r') as Tab2:
        while i > 0:
            linea=list(Tab2.readline())
            if len (linea)==0:
                break
            else:
                board2.append(linea[0:13:2])
    archives = True
    main()
def start_game():
    global turn
    global winner
    global turn
    while winner == 0:
        if turn == 1:
            print("Turn of Player 1")
            for y in hitboard1:
                print("")
                for x in y:
                    print(x,end=" ")
            print("")
            print("Continue?\n 1.-Yes \n 2.- I give up")
            cont=int(input())
            if cont== 2:
                print("Are You Sure?\n 1.-Yes \n 2.- No, Bring me back")
                conti=int(input())
                if conti== 1:
                     winner=2
                     start_game()
            print("Input Coordinate for X:")
            x=int(input())-1
            print("Input Coordinate for Y:")
            y=int(input())-1
            if x > 6 or y > 6:
                print("Invalid Coordinate, Try again")
                start_game()
            if hit_scan(x,y) == True:
                print("You damaged the enemy ship\n")
                counter=0
                for y in hitboard1:
                    for x in y:
                        if x=='H':
                            counter+=1
                            
                            if counter==3:
                                winner=1
                                start_game()
                            else:
                                continue
                        
                        else:
                            counter=0
                for y in range (6):
                    for x in range(6):
                        n=hitboard1[x][y]
                        if n=='H':
                            counter+=1
                            if counter==3:
                                winner=1
                                start_game()
                            
                        else:
                            counter=0
                
            else:
                print("You missed, better luck next time\n")
            turn=2

        elif turn == 2:
            for y in hitboard2:
                print("")
                for x in y:
                    print(x,end=" ")
            print("")
            print("Continue?\n 1.-Yes \n 2.- I give up")
            cont=int(input())
            if cont== 2:
                print("Are You Sure?\n 1.-Yes \n 2.- No, Bring me back")
                conti=int(input())
                if conti:
                     winner=1
                     start_game()
                print("Inválido")
                start_game()
            print("Turn of Player 2")
            print("Input Coordinate for X:")
            x=int(input())-1
            print("Input Coordinate for Y:")
            y=int(input())-1
            if x > 6 or y > 6:
                print("Invalid Coordinate, Try again")
            if hit_scan(x,y) == True:
                print("You damaged the enemy ship\n")
                n=9
                counter=0
                for y in hitboard2:
                    for x in y:
                        if x=='H':
                            counter+=1
                            
                            if counter==3:
                                winner=2
                                start_game()
                            else:
                                continue
                        
                        else:
                            counter=0
                    for y in range (6):
                        for x in range(6):
                            n=hitboard1[x][y]
                            if n=='H':
                                counter+=1
                                if counter==3:
                                    winner=2
                                    start_game()
                                
                            else:
                                counter=0
            else:
                print("You missed, better luck next time\n")
            turn=1
            
    if winner==1:
        print("Player 1 has won, Congratulations")
        exit()
    if winner==2:
        print("Player 2 has won, Congratulations")
        exit()
        
def hit_scan(x,y):
    global turn
    global board2
    global board1
    global hitboard1
    global hitboard2
    if turn == 1:
        if board2[y][x] == '1':
            board2[y][x] = '2'
            hitboard1[y][x]='H'
            return(True)
        elif board2[y][x] == '2':
            print('You already shot there')
            start_game()
        else:
            hitboard1[y][x]='M'
    if turn == 2:
        if board1[y][x] == '1':
            hitboard2[y][x]='H'
            board2[y][x] = '2'
            return(True)
        elif board1[y][x] == '2':
            print('You already shot there')
            start_game()
        else:
            hitboard2[y][x]='M'

archives=False
winner=0
turn=1
main()
    