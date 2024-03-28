boardState = PlayerO = PlayerX = input_position = 0
player_turn_and_win_is_2 = 1 if input("X or O first?: ").lower() == "x" else 0

def print_board(): print(*["".join(map(str,["-" if boardState & n != n else "X" if PlayerX & n == n else "O" for n in (1,2,4,8,16,32,64,128,256)][i: i+3])) for i in range(0,9,3)], sep="\n")
while boardState != 511:
    print_board()
    while (input_position := 2 ** (int(input("Key in the place you want to put (1 - 9): ")) - 1)) not in (1,2,4,8,16,32,64,128,256) or boardState & input_position > 0: print("invalid move")
    boardState |= input_position
    match player_turn_and_win_is_2:
        case 0:
            PlayerO |= input_position
            if any(PlayerO & number == number for number in (448,56,7,292,146,73,84,273)):
                print_board()
                print("Player O won")
                player_turn_and_win_is_2 = 2
                break
        case 1:
            PlayerX |= input_position
            if any(PlayerX & number == number for number in (448,56,7,292,146,73,84,273)):
                print_board()
                print("Player X won")
                player_turn_and_win_is_2 = 2
                break

    player_turn_and_win_is_2 = 1-player_turn_and_win_is_2

if player_turn_and_win_is_2 < 2:print("draw")