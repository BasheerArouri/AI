# “We certify that this submission is the original work of members of the group and meets
# the Faculty's Expectations of Originality"
#Momen Salem 1200034
#Basheer Arouri 1201141
import copy

from anytree import Node, RenderTree


def printBoard(board):
    print('\tA\tB\tC\tD\tE\tF\tG\tH\t')
    for row in range(8):
        print(8 - row, '\t', end='')
        for column in range(8):
            if board[row][column] == 0:
                print("\t", end='')
            elif board[row][column] == 1:  # if 1 then there is a black stone
                print('□\t', end='')
            elif board[row][column] == 2:
                print('■\t', end='')
        print(8 - row)
    print('\tA\tB\tC\tD\tE\tF\tG\tH\t')


def check_if_legal_position(board, position, turn):
    row_for_this_position = check_and_get_row(position)
    column_for_this_position = check_and_get_column(position)
    if row_for_this_position == -1 or column_for_this_position == -1:
        # the number of argument for move is not valid
        return 0
    if board[row_for_this_position][column_for_this_position] == 2 or board[row_for_this_position][
        column_for_this_position] == 1:
        print("There is a brick in this position (" + position + ") please choose another legal move.")
        return 0
    elif column_for_this_position != 0 and column_for_this_position != 7:
        if not board[row_for_this_position][column_for_this_position - 1] \
                and not board[row_for_this_position][column_for_this_position + 1]:
            print("You entered invalid position (" + position + "), Please enter a valid position.")
            return 0
    if turn == 1:
        board[row_for_this_position][column_for_this_position] = 1
    else:
        board[row_for_this_position][column_for_this_position] = 2
    check_win = goal_test(Board, turn, row_for_this_position, column_for_this_position)
    if check_win == 1:
        return 2  # 2 means that the game is completed and there is a winner
    else:
        return 1


def check_and_get_row(position):
    if 1 <= int(position[1]) <= 8:
        row_for_this_position = 8 - int(position[1])
    else:
        print("You entered invalid position, Please enter a valid position.")
        return -1  # mean there is an error in move
        # Here entering again.
    return row_for_this_position


def check_and_get_column(position):
    if len(position) > 2:
        print("You entered invalid position, Please enter a valid position.")
        return -1
    if 'A' <= position[0] <= 'H':
        column_for_this_position = ord(position[0]) - 65
    else:
        print("You entered invalid position, Please enter a valid position, must be like this (A-H)(1-8).")
        # Here entering again.
        return -1
    return column_for_this_position


def goal_test(board, turn, current_row, current_column):
    # check if any row has 5 consecutive bricks
    number_of_bricks_to_check = 0
    for column in range((current_column + 1), 8):  # loop from current column to the highest one
        if board[current_row][column] == turn:
            number_of_bricks_to_check += 1
        else:
            break
    for column in range(current_column, -1, -1):  # decremental loop start from current column to the first one
        if board[current_row][column] == turn:
            number_of_bricks_to_check += 1
        else:
            break

    # check if any column has 5 consecutive bricks
    column_count = 0
    for row in range((current_row + 1), 8):  # loop from current column to the highest one
        if board[row][current_column] == turn:
            column_count += 1
        else:
            break
    for row in range(current_row, -1, -1):  # decremental loop start from current column to the first one
        if board[row][current_column] == turn:
            column_count += 1
        else:
            break
    # check if any right diagonal has 5 consecutive bricks
    right_diagonal_count = -1
    row = current_row
    column = current_column
    while 0 <= row <= 7 and 0 <= column <= 7:
        if board[row][column] == turn:
            right_diagonal_count += 1
        else:
            break
        row -= 1
        column += 1
    row = current_row
    column = current_column
    while 0 <= row <= 7 and 0 <= column <= 7:
        if board[row][column] == turn:
            right_diagonal_count += 1
        else:
            break
        row += 1
        column -= 1
    left_diagonal_count = -1
    row = current_row
    column = current_column
    while 0 <= row <= 7 and 0 <= column <= 7:
        if board[row][column] == turn:
            left_diagonal_count += 1
        else:
            break
        row -= 1
        column -= 1
    row = current_row
    column = current_column
    while 0 <= row <= 7 and 0 <= column <= 7:
        if board[row][column] == turn:
            left_diagonal_count += 1
        else:
            break
        row += 1
        column += 1
    # print(number_of_bricks_to_check, column_count, right_diagonal_count, left_diagonal_count)
    if number_of_bricks_to_check == 5 or column_count == 5 or right_diagonal_count == 5 or left_diagonal_count == 5:
        printBoard(board)
        print("Player {} Wins!".format(turn))
        return 1


def print_List():
    print("1. Multiple players")
    print("2. Versus computer, You start")
    print("3. Versus computer, Computer start")
    print("4. Quit")


def evaluation_function(board, turn):  # define evaluation function by passing the state and who play to decide the
    max_row_bricks_me = 0
    max_row_bricks_comp = 0
    row = 0

    while row < 8:  # count max number of consecutive bricks in row
        my_bricks = 0
        comp_bricks = 0
        for column in range(8):  # count the consecutive bricks for each row

            if board[row][column] == turn:
                for my_row in range(row + 1, 8):
                    if board[my_row][column] == turn:
                        my_bricks += 2
                    elif board[my_row][column] == 0:
                        my_bricks += 1
                    else:
                        max_row_bricks_me = max(my_bricks, max_row_bricks_me)
                        my_bricks = 0
                        break
                max_row_bricks_me = max(my_bricks, max_row_bricks_me)

                for i in range(row - 1, -1, -1):  # decremental loop start from current column to the first one
                    if board[i][column] == turn:
                        my_bricks += 2
                    elif board[i][column] == 0:
                        my_bricks += 1
                    else:
                        max_row_bricks_me = max(my_bricks, max_row_bricks_me)
                        my_bricks = 0
                        break
                max_row_bricks_me = max(my_bricks, max_row_bricks_me)

            elif board[row][column] == 3 - turn:

                for comp_row in range(row + 1, 8):
                    if board[comp_row][column] == 3 - turn:
                        comp_bricks += 2
                    elif board[comp_row][column] == 0:
                        comp_bricks += 1
                    else:
                        max_row_bricks_comp = max(comp_bricks, max_row_bricks_comp)
                        comp_bricks = 0
                        break
                max_row_bricks_comp = max(comp_bricks, max_row_bricks_comp)

                for j in range(row - 1, -1, -1):  # decremental loop start from current column to the first one

                    if board[j][column] == 3 - turn:
                        comp_bricks += 2
                    elif board[j][column] == 0:
                        comp_bricks += 1
                    else:
                        max_row_bricks_comp = max(comp_bricks, max_row_bricks_comp)
                        comp_bricks = 0
                        break
                max_row_bricks_comp = max(comp_bricks, max_row_bricks_comp)
        row += 1
    max_col_bricks_me = 0
    max_col_bricks_comp = 0
    column = 0

    while column < 8:  # count max number of consecutive bricks in row
        my_bricks = 0
        comp_bricks = 0
        for row in range(8):  # count the consecutive bricks for each row

            if board[row][column] == turn:

                for my_col in range(column + 1, 8):
                    if board[row][my_col] == turn:
                        my_bricks += 2
                    elif board[row][my_col] == 0:
                        my_bricks += 1
                    else:
                        max_col_bricks_me = max(my_bricks, max_col_bricks_me)
                        my_bricks = 0
                        break
                max_col_bricks_me = max(my_bricks, max_col_bricks_me)

                for i in range(column - 1, -1, -1):  # decremental loop start from current column to the first one
                    if board[row][i] == turn:
                        my_bricks += 2
                    elif board[row][i] == 0:
                        my_bricks += 1
                    else:
                        max_col_bricks_me = max(my_bricks, max_col_bricks_me)
                        my_bricks = 0
                        break
                max_col_bricks_me = max(my_bricks, max_col_bricks_me)

            elif board[row][column] == 3 - turn:
                for comp_col in range(column + 1, 8):
                    if board[row][comp_col] == 3 - turn:
                        comp_bricks += 2
                    elif board[row][comp_col] == 0:
                        comp_bricks += 1
                    else:
                        max_col_bricks_comp = max(comp_bricks, max_col_bricks_comp)
                        comp_bricks = 0
                        break
                max_col_bricks_comp = max(comp_bricks, max_col_bricks_comp)

                for j in range(column - 1, -1, -1):  # decremental loop start from current column to the first one

                    if board[row][j] == 3 - turn:
                        comp_bricks += 2
                    elif board[row][j] == 0:
                        comp_bricks += 1
                    else:
                        max_col_bricks_comp = max(comp_bricks, max_col_bricks_comp)
                        comp_bricks = 0
                        break
                max_col_bricks_comp = max(comp_bricks, max_col_bricks_comp)
        column += 1

    evaluation_result = min((max_col_bricks_me - max_col_bricks_comp), (max_row_bricks_me - max_row_bricks_comp))
    return evaluation_result


def legalMoves(board):
    moves = []

    for row in range(8):
        for column in range(8):
            if board[row][column] == 0:
                r = 8 - row
                col = chr(65 + column)
                position = col + str(r)
                moves.append(position)
                break
    revers_row = 7
    while revers_row >= 0:
        revers_column = 7
        while revers_column >= 0:
            if board[revers_row][revers_column] == 0:
                revers_r = 8 - revers_row
                revers_col = chr(65 + revers_column)
                revers_position = revers_col + str(revers_r)
                moves.append(revers_position)
                break
            revers_column -= 1
        revers_row -= 1

    return moves


class TreeNode:
    def __init__(self, state):
        self.state = state
        self.children = []
        self.move = None


def build_tree(Board, depth, turn):
    if depth == 0:
        return
    root = TreeNode(Board)
    moves = legalMoves(Board)

    for position in moves:
        new_board = copy.deepcopy(Board)
        column, row = check_and_get_column(position), check_and_get_row(position)
        new_board[row][column] = turn
        node = TreeNode(new_board)
        node.move = str(chr(65 + column) + str(8 - row))
        root.children.append(node)

        child = build_tree(new_board, depth - 1, (3 - turn))
        node.children.append(child)
    return root


def print_tree(node):
    printBoard(node.state)

    for child in node.children:
        if child is not None:
            print_tree(child)


def minimax(node, depth, maximizing_player, turn):
    if depth == 0:
        return evaluation_function(node.state, turn), node.move

    best_move = None
    if maximizing_player:
        max_eval = float('-inf')
        for child in node.children:
            eval, _ = minimax(child, depth - 1, False, 3 - turn)
            if eval > max_eval:
                max_eval = eval
                best_move = child.move  # Update the best move
        return max_eval, best_move
    else:
        min_eval = float('inf')
        for child in node.children:
            eval, _ = minimax(child, depth - 1, True, turn)
            if eval < min_eval:
                min_eval = eval
                best_move = child.move  # Update the best move
        return min_eval, best_move


print("Wellcome to our magnetic cave game please chose from bellow list to start a game. I hope you will enjoy :)")
choice = 0
global remaining_moves
while choice != 4:
    print_List()
    choice = input("Please choose from above list to start the game")
    if choice.isalpha():
        choice = 5
    else:
        choice = int(choice)
    Board = [[0 for _ in range(9)] for _ in range(9)]  # empty the board from bricks
    remaining_moves = 64  # the overall remaining moves for the whole game if equal zero -> the result of game is draw
    if choice == 1:
        turn = 1  # the first player which is black is his turn to play
        while remaining_moves > 0:

            print("The board is as bellow please enter your move, must be like this (A-H)(1-8)")
            printBoard(Board)
            if turn == 1:
                print("The turn is for Black player")
            else:
                print("The turn is for White player")
            move = input("Enter Your move")
            check_move = check_if_legal_position(Board, move, turn)

            if check_move == 0:
                continue  # the move is illegal so do another legal one
            elif check_move == 1:
                turn = 3 - turn  # now the turn is on your opponent
            elif check_move == 2:
                break  # the game is done and there is a winner
            remaining_moves -= 1  # the board is lost one more move
        if remaining_moves == 0:
            print("The game is done with draw")


    elif choice == 2:

        turn = 1  # the first player which is black is his turn to play
        while remaining_moves > 0:
            print("The board is as bellow please enter your move, must be like this (A-H)(1-8)")
            printBoard(Board)
            depth = 3
            print("The turn is for You")
            move = input("Enter Your move: ")
            check_move = check_if_legal_position(Board, move, turn)
            if check_move == 0:
                continue  # the move is illegal so do another legal one
            elif check_move == 2:
                break  # the game is done and there is a winner
            print("The turn is for Computer")

            turn = 2  # now the turn is on your opponent
            #########Computer turn##############
            # Establish the Tree~~
            tree = build_tree(Board, depth, turn)
            best_move = minimax(tree, depth, True, turn)
            check_move = check_if_legal_position(Board, best_move[1], turn)
            if check_move == 0:
                continue  # the move is illegal so do another legal one
            elif check_move == 2:
                break  # the game is done and there is a winner
            turn = 1
        remaining_moves -= 1  # the board is lost one more movE

        if remaining_moves == 0:
            print("The game is done with draw")


    elif choice == 3:
        turn = 1  # the first player which is black is his turn to play
        user = 0
        while remaining_moves > 0:
            depth = 3
            if user == 0:
                print("The turn is for Computer")
                tree = build_tree(Board, depth, turn)
                best_move = minimax(tree, depth, True, turn)
                check_move = check_if_legal_position(Board, best_move[1], turn)
                if check_move == 0:
                    continue  # the move is illegal so do another legal one
                elif check_move == 2:
                    break  # the game is done and there is a winner
                turn = 2
            print("The board is as bellow please enter your move, must be like this (A-H)(1-8)")
            printBoard(Board)
            print("The turn is for You")
            move = input("Enter Your move: ")
            check_move = check_if_legal_position(Board, move, turn)
            if check_move == 0:
                user = 1
                continue  # the move is illegal so do another legal one
            elif check_move == 2:

                break  # the game is done and there is a winner3
            user = 0
            turn = 1
        remaining_moves -= 1  # the board is lost one more movE

        if remaining_moves == 0:
            print("The game is done with draw")
    elif choice == 4:
        print("I Hope You are enjoyed and be the winner :)")
    else:
        choice = 0
        print("You must choose from bellow list to start the game (1 or 2 or 3)")
