import numpy as np
import random
import time

MOVES = []
ROW_COUNT = 6
COLUMN_COUNT = 7
PLAYER = 1
AI = 2
def creat_board():
    board = np.zeros((ROW_COUNT,COLUMN_COUNT))
    return board

def select(board):
    while True:
            try:
                col = int(input("Enter a valid position(0,6): "))
                if col in range(COLUMN_COUNT) and board[5][col] == 0:
                    return col
                else:
                    print("Invalid position")
            except ValueError or IndexError:
                print("Invali position")

def is_valid_col(board,col):
    if board[5][col] == 0:
        return True

def get_valid_col(board):
    valid_col = []
    for col in range(COLUMN_COUNT):
        if is_valid_col(board,col):
            valid_col.append(col)
    return valid_col

def next_row(board,col):
    for r in range(ROW_COUNT):
        if board[r][col] == 0:
            return r

def add_piece(board,row,col,piece):
    board[row][col] = piece

def print_board(board):
    return np.flip(board,0)



def is_terminal_node(board):
    return winning_move(board, PLAYER) or winning_move(board, AI) or len(get_valid_col(board)) == 0

def score_position(board,piece):
    score = 0
    centre_array = [int(i) for i in list(board[:,3])]
    centre_count = centre_array.count(piece)
    score += centre_count * 4
    for r in range(ROW_COUNT):
        for c in range(COLUMN_COUNT - 3):
            window = [int(board[r][c+i]) for i in range(4)]
            score += window_value(window,piece)

    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT - 3):
            window = [int(board[r+i][c]) for i in range(4)]
            score += window_value(window,piece)

    for r in range(ROW_COUNT - 3):
        for c in range(COLUMN_COUNT - 3):
            window = [int(board[r+i][c+i]) for i in range(4)]
            score += window_value(window, piece)

    for r in range(3, ROW_COUNT):
        for c in range(COLUMN_COUNT - 3):
            window = [int(board[r-i][c+i]) for i in range(4)]
            score += window_value(window, piece)

    return score

def window_value(window,piece):
    score = 0
    opp_piece = PLAYER
    if piece == PLAYER:
        opp_piece = AI
    if window.count(piece) == 4:
        score += 100
    elif window.count(piece) == 3 and window.count(0) == 1:
        score += 5
    elif window.count(piece) == 2 and window.count(0) == 2:
        score += 3
    if window.count(opp_piece) == 3 and window.count(0) == 1:
        score -= 90
    return score





def minimax(board, depth, maximisingPlayer):
    valid_locations = get_valid_col(board)

    is_terminal = is_terminal_node(board)
    if depth == 0 or is_terminal:
        if is_terminal:
            if winning_move(board, AI):
                return (None, 9999999)
            elif winning_move(board, PLAYER):
                return (None, -9999999)
            else:
                return (None, 0)
        else:
            return (None, score_position(board, AI))

    if maximisingPlayer:
        value = -9999999
        column = random.choice(valid_locations)
        for col in valid_locations:
            row = next_row(board, col)
            b_copy = board.copy()
            add_piece(b_copy, row, col, AI)
            new_score = minimax(b_copy, depth - 1, False)[1]
            if new_score > value:
                value = new_score
                column = col
        return column, value

    else:
        value = 9999999
        column = random.choice(valid_locations)
        for col in valid_locations:
            row = next_row(board, col)
            b_copy = board.copy()
            add_piece(b_copy, row, col, PLAYER)
            new_score = minimax(b_copy, depth - 1, True)[1]
            if new_score < value:
                value = new_score
                column = col
            
        return column, value




def minimax_with_alpha_beta(board, depth, alpha, beta, maximisingPlayer):
    valid_locations = get_valid_col(board)

    is_terminal = is_terminal_node(board)
    if depth == 0 or is_terminal:
        if is_terminal:
            if winning_move(board, AI):
                return (None, 9999999)
            elif winning_move(board, PLAYER):
                return (None, -9999999)
            else:
                return (None, 0)
        else:
            return (None, score_position(board, AI))

    if maximisingPlayer:
        value = -9999999
        column = random.choice(valid_locations)
        for col in valid_locations:
            row = next_row(board, col)
            b_copy = board.copy()
            add_piece(b_copy, row, col, AI)
            new_score = minimax_with_alpha_beta(b_copy, depth - 1, alpha, beta, False)[1]
            if new_score > value:
                value = new_score
                column = col
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return column, value

    else:
        value = 9999999
        column = random.choice(valid_locations)
        for col in valid_locations:
            row = next_row(board, col)
            b_copy = board.copy()
            add_piece(b_copy, row, col, PLAYER)
            new_score = minimax_with_alpha_beta(b_copy, depth - 1, alpha, beta, True)[1]
            if new_score < value:
                value = new_score
                column = col
            beta = min(beta, value)
            if alpha >= beta:
                break
        return column, value

def winning_move(board,piece):
    for r in range(ROW_COUNT):
        for c in range(COLUMN_COUNT - 3):
            if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
                return True
    for r in range(ROW_COUNT - 3):
        for c in range(COLUMN_COUNT):
            if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
                return True
    for r in range(ROW_COUNT - 3):
        for c in range(COLUMN_COUNT - 3):
            if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
                return True
    for r in range(3, ROW_COUNT):
        for c in range(COLUMN_COUNT - 3):
            if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
                return True
def count_future_chances(window, piece):
    opp_piece = PLAYER if piece == AI else PLAYER
    if window.count(opp_piece) == 0:
        return 1
    else:
        return 0
    
def future_chance_score(board, piece):
    score = 0
    centre_array = [int(i) for i in list(board[:,3])]
    centre_count = centre_array.count(piece)
    score += centre_count * 4
    for r in range(ROW_COUNT):
        for c in range(COLUMN_COUNT - 3):
            window = [int(board[r][c+i]) for i in range(4)]
            score += count_future_chances(window,piece)

    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT - 3):
            window = [int(board[r+i][c]) for i in range(4)]
            score += count_future_chances(window,piece)

    for r in range(ROW_COUNT - 3):
        for c in range(COLUMN_COUNT - 3):
            window = [int(board[r+i][c+i]) for i in range(4)]
            score += count_future_chances(window, piece)

    for r in range(3, ROW_COUNT):
        for c in range(COLUMN_COUNT - 3):
            window = [int(board[r-i][c+i]) for i in range(4)]
            score += count_future_chances(window, piece)

    return score


def minimax2(board, depth, maximisingPlayer):
    valid_locations = get_valid_col(board)

    is_terminal = is_terminal_node(board)
    if depth == 0 or is_terminal:
        if is_terminal:
            if winning_move(board, AI):
                return (None, 9999999)
            elif winning_move(board, PLAYER):
                return (None, -9999999)
            else:
                return (None, 0)
        else:
            return (None, future_chance_score(board, AI))

    if maximisingPlayer:
        value = -9999999
        column = random.choice(valid_locations)
        for col in valid_locations:
            row = next_row(board, col)
            b_copy = board.copy()
            add_piece(b_copy, row, col, AI)
            new_score = minimax2(b_copy, depth - 1, False)[1]
            if new_score > value:
                value = new_score
                column = col
        return column, value

    else:
        value = 9999999
        column = random.choice(valid_locations)
        for col in valid_locations:
            row = next_row(board, col)
            b_copy = board.copy()
            add_piece(b_copy, row, col, PLAYER)
            new_score = minimax2(b_copy, depth - 1, True)[1]
            if new_score < value:
                value = new_score
                column = col
        return column, value





def minimax2_with_alph_beta(board, depth, alpha, beta, maximisingPlayer):
    valid_locations = get_valid_col(board)

    is_terminal = is_terminal_node(board)
    if depth == 0 or is_terminal:
        if is_terminal:
            if winning_move(board, AI):
                return (None, 9999999)
            elif winning_move(board, PLAYER):
                return (None, -9999999)
            else:
                return (None, 0)
        else:
            return (None, future_chance_score(board, AI))

    if maximisingPlayer:
        value = -9999999
        column = random.choice(valid_locations)
        for col in valid_locations:
            row = next_row(board, col)
            b_copy = board.copy()
            add_piece(b_copy, row, col, AI)
            new_score = minimax2_with_alph_beta(b_copy, depth - 1, alpha, beta, False)[1]
            if new_score > value:
                value = new_score
                column = col
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return column, value

    else:
        value = 9999999
        column = random.choice(valid_locations)
        for col in valid_locations:
            row = next_row(board, col)
            b_copy = board.copy()
            add_piece(b_copy, row, col, PLAYER)
            new_score = minimax2_with_alph_beta(b_copy, depth - 1, alpha, beta, True)[1]
            if new_score < value:
                value = new_score
                column = col
            beta = min(beta, value)
            if alpha >= beta:
                break
        return column, value
    
    
    
    
    
    
    
def hurestic(board,piece):
    best_score = -10000
    valid_col = get_valid_col(board)
    best_col = -1

    for col in valid_col:
        row = next_row(board,col)
        temp_board = board.copy()
        add_piece(temp_board,row,col,piece)
        score = score_position(temp_board,piece)
        if score > best_score:
            best_score = score
            best_col = col

    return best_col


def hurestic2(board,piece):
    best_score = -10000
    valid_col = get_valid_col(board)
    best_col = -1

    for col in valid_col:
        row = next_row(board,col)
        temp_board = board.copy()
        add_piece(temp_board,row,col,piece)
        score = future_chance_score(temp_board,piece)
        if score > best_score:
            best_score = score
            best_col = col

    return best_col
