def create_game(in_game):
    return [" ".join(in_game[i:i + n]) for i in range(0, len(in_game), n)]


def print_game(game_lay):
    print("---------")
    for line in game_lay:
        print(f"| {line} |")
    print("---------")


def fn_chars(sub_str):
    n_chars = []

    for part in sub_str:
        n_X = 0
        n_O = 0
        n_e = 0

        for i in part:
            if i == "X":
                n_X += 1
            elif i == "O":
                n_O += 1
            else:
                n_e += 1

        n_chars.append([n_X,n_O,n_e])

    return n_chars


def check_win(n_chars_list):
    wins = []

    for counts in n_chars_list:
        wins_part = []
        for part in counts:
            if part == 3:
                wins_part.append(1)
            else:
                wins_part.append(0)

        wins.append(wins_part)

    return wins


def check_game(game, len_game, n):
    lines = [game[i:i+n] for i in range(0, len_game, n)]
    cols = [game[i:len_game:n] for i in range(0, 3)]
    diags = [game[i:len_game-i:4-i] for i in [0, 2]]

    n_chars_line = fn_chars(lines)
    n_chars_col = fn_chars(cols)
    n_chars_diag = fn_chars(diags)

    wins_line = check_win(n_chars_line)
    wins_col = check_win(n_chars_col)
    wins_diag = check_win(n_chars_diag)

    sum_x = sum([item[0] for item in n_chars_line])
    sum_o = sum([item[1] for item in n_chars_line])
    n_chars_empty = sum([part[2] for part in n_chars_line])
    x_wins = [item[0] for wins_list in [wins_line, wins_col, wins_diag] for item in wins_list]
    o_wins = [item[1] for wins_list in [wins_line, wins_col, wins_diag] for item in wins_list]

    if (sum(x_wins) == 1 and sum(o_wins) == 1) or (abs(sum_x - sum_o) >= 2):
        status = "Impossible"
    elif n_chars_empty > 0 and sum(x_wins) == 0 and sum(o_wins) == 0:
        status = "Game not finished"
    elif n_chars_empty == 0 and sum(x_wins) == 0 and sum(o_wins) == 0:
        status = "Draw"
    elif sum(x_wins) == 1 and sum(o_wins) == 0:
        status = "X wins"
    elif sum(x_wins) == 0 and sum(o_wins) == 1:
        status = "O wins"
    else:
        status = "Impossible"

    return status


def game_status(status_check):
    if status_check == "X wins" or status_check == "O wins" or status_check == "Draw":
        return True
    else:
        return False


game = "_________"
len_game = len(game)
n = 3
cord_set = {1, 2, 3}

game_layout = create_game(game)
print_game(game_layout)
counter = 1

while True:
    coordinates = input().replace(" ", "")
    try:
        cords = [int(coordinates[0]), int(coordinates[1])]
    except:
        print("You should enter numbers!")
    else:
        if len(cords) == 2 and cords[0] in cord_set and cords[1] in cord_set:
            position = (cords[1] - 1) + ((cords[0] - 1) * 3)
            if game[position] in {"X", "O"}:
                print("This cell is occupied! Choose another one!")
            else:
                if counter % 2 == 1:
                    game = game[0:position] + "X" + game[position + 1:len_game]
                else:
                    game = game[0:position] + "O" + game[position + 1:len_game]

                game_layout = create_game(game)
                print_game(game_layout)
                counter += 1
                status = check_game(game, len_game, n)
                game_finished = game_status(status)

                if game_finished:
                    print(status)
                    break
                else:
                    continue
        else:
            print("Coordinates should be from 1 to 3!")
