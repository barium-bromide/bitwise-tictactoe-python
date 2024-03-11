boardState = 0
PlayerX = 0
PlayerO = 0
input_position = 0
player_turn_and_win_is_2 = 1 if input("X or O first?: ").lower() == "x" else 0

while boardState != 511:
    print(("-" if boardState & 1 != 1 else "X" if PlayerX & 1 == 1 else "O")
           + ("-" if boardState & 2 != 2 else "X" if PlayerX & 2 == 2 else "O") 
           + ("-" if boardState & 4 != 4 else "X" if PlayerX & 4 == 4 else "O") 
           + "\n"
           + ("-" if boardState & 8 != 8 else "X" if PlayerX & 8 == 8 else "O") 
           + ("-" if boardState & 16 != 16 else "X" if PlayerX & 16 == 16 else "O") 
           + ("-" if boardState & 32 != 32 else "X" if PlayerX & 32 == 32 else "O") 
           + "\n" 
           + ("-" if boardState & 64 != 64 else "X" if PlayerX & 64 == 64 else "O") 
           + ("-" if boardState & 128 != 128 else "X" if PlayerX & 128 == 128 else "O")
           + ("-" if boardState & 256 != 256 else "X" if PlayerX & 256 == 256 else "O"))
    while (input_position := 2 ** (int(input("Key in the place you want to put (1 - 9): ")) - 1)) not in (1,2,4,8,16,32,64,128,256) or boardState & input_position > 0:
        print("invalid move")

    boardState |= input_position
    match player_turn_and_win_is_2:
        case 0:
            PlayerO |= input_position
            if PlayerO & 448 == 448 or PlayerO & 56 == 56 or PlayerO & 7 == 7 or PlayerO & 292 == 292 or PlayerO & 146 == 146 or PlayerO & 73 == 73 or PlayerO & 84 == 84 or PlayerO & 273 == 273:
                print(("-" if boardState & 1 != 1 else "X" if PlayerX & 1 == 1 else "O")
           + ("-" if boardState & 2 != 2 else "X" if PlayerX & 2 == 2 else "O") 
           + ("-" if boardState & 4 != 4 else "X" if PlayerX & 4 == 4 else "O") 
           + "\n"
           + ("-" if boardState & 8 != 8 else "X" if PlayerX & 8 == 8 else "O") 
           + ("-" if boardState & 16 != 16 else "X" if PlayerX & 16 == 16 else "O") 
           + ("-" if boardState & 32 != 32 else "X" if PlayerX & 32 == 32 else "O") 
           + "\n" 
           + ("-" if boardState & 64 != 64 else "X" if PlayerX & 64 == 64 else "O") 
           + ("-" if boardState & 128 != 128 else "X" if PlayerX & 128 == 128 else "O")
           + ("-" if boardState & 256 != 256 else "X" if PlayerX & 256 == 256 else "O"))
                print("Player O won")
                player_turn_and_win_is_2 = 2
                break
        case 1:
            PlayerX |= input_position
            if PlayerX & 448 == 448 or PlayerX & 56 == 56 or PlayerX & 7 == 7 or PlayerX & 292 == 292 or PlayerX & 146 == 146 or PlayerX & 73 == 73 or PlayerX & 84 == 84 or PlayerX & 273 == 273:
                print(("-" if boardState & 1 != 1 else "X" if PlayerX & 1 == 1 else "O")
           + ("-" if boardState & 2 != 2 else "X" if PlayerX & 2 == 2 else "O") 
           + ("-" if boardState & 4 != 4 else "X" if PlayerX & 4 == 4 else "O") 
           + "\n"
           + ("-" if boardState & 8 != 8 else "X" if PlayerX & 8 == 8 else "O") 
           + ("-" if boardState & 16 != 16 else "X" if PlayerX & 16 == 16 else "O") 
           + ("-" if boardState & 32 != 32 else "X" if PlayerX & 32 == 32 else "O") 
           + "\n" 
           + ("-" if boardState & 64 != 64 else "X" if PlayerX & 64 == 64 else "O") 
           + ("-" if boardState & 128 != 128 else "X" if PlayerX & 128 == 128 else "O")
           + ("-" if boardState & 256 != 256 else "X" if PlayerX & 256 == 256 else "O"))
                print("Player X won")
                player_turn_and_win_is_2 = 2
                break

    player_turn_and_win_is_2 = 1 - player_turn_and_win_is_2

if player_turn_and_win_is_2 < 2:
    print("draw")