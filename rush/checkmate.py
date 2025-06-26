def is_king_in_check(board_str):
    board = [list(row) for row in board_str.strip().split('\n')]
    size = len(board)
    
    # Find King
    king_position = None
    for row in range(size):
        for col in range(size):
            if board[row][col] == 'K':
                king_position = (row, col)
                break
        if king_position:
            break
    if not king_position:
        return "Fail"
    
    king_row, king_col = king_position
    
    # For Queen/Bishop
    diagonals = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
    # For Queen/Rook
    lines = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    # Pawn 
    pawn_attacks = [(1, -1), (1, 1)]
    for dr, dc in pawn_attacks:
        row, col = king_row + dr, king_col + dc
        if 0 <= row < size and 0 <= col < size and board[row][col] == 'P':
            return "Success"

    # Check for Pawn threats
    for dr, dc in pawn_attacks:
        row, col = king_row + dr, king_col + dc
        if 0 <= row < size and 0 <= col < size and board[row][col] == 'P':
            return "Success"

    # Check for Queen/Bishop
    for dr, dc in diagonals:
        row, col = king_row + dr, king_col + dc
        while 0 <= row < size and 0 <= col < size:
            piece = board[row][col]
            if piece != '.':
                if piece == 'B' or piece == 'Q':
                    return "Success"
                break
            row += dr
            col += dc

    # Check for Queen/Rook
    for dr, dc in lines:
        row, col = king_row + dr, king_col + dc
        while 0 <= row < size and 0 <= col < size:
            piece = board[row][col]
            if piece != '.':
                if piece == 'R' or piece == 'Q':
                    return "Success"
                break
            row += dr
            col += dc

    return "Fail"


def main():
    board = """
.......
.......
....K..
.......
..P....
.......
.......
"""
    print(is_king_in_check(board))

if __name__ == "__main__":
    main()