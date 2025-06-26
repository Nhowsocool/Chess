def is_king_in_check(board_str):
    # Convert the board string into a 2D list for easier access
    board = [list(row) for row in board_str.strip().split('\n')]
    size = len(board)
    
    # Find the coordinates of the King ('K') on the board
    king_position = None
    for row in range(size):
        for col in range(size):
            if board[row][col] == 'K':
                king_position = (row, col)
                break
        if king_position:
            break
    # If there is no King found, return "Fail"
    if not king_position:
        return "Fail"
    
    king_row, king_col = king_position
    
    # Directions for diagonal movement (for Bishop and Queen)
    diagonals = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
    # Directions for horizontal & vertical movement (for Rook and Queen)
    lines = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    # Relative positions where a Pawn (assuming from bottom upwards) can attack the King
    pawn_attacks = [(1, -1), (1, 1)]
    # Check if any Pawn threatens the King from these positions
    for dr, dc in pawn_attacks:
        row, col = king_row + dr, king_col + dc
        if 0 <= row < size and 0 <= col < size and board[row][col] == 'P':
            return "Success"

    # Check for Pawn threats (duplicated, can be removed)
    for dr, dc in pawn_attacks:
        row, col = king_row + dr, king_col + dc
        if 0 <= row < size and 0 <= col < size and board[row][col] == 'P':
            return "Success"

    # Check for diagonal threats from Bishops or Queens
    for dr, dc in diagonals:
        row, col = king_row + dr, king_col + dc
        while 0 <= row < size and 0 <= col < size:
            piece = board[row][col]
            # If a piece is found, check if it's a Bishop or Queen
            if piece != '.':
                if piece == 'B' or piece == 'Q':
                    return "Success"
                break
            row += dr
            col += dc

    # Check for horizontal and vertical threats from Rooks or Queens
    for dr, dc in lines:
        row, col = king_row + dr, king_col + dc
        while 0 <= row < size and 0 <= col < size:
            piece = board[row][col]
            # If a piece is found, check if it's a Rook or Queen
            if piece != '.':
                if piece == 'R' or piece == 'Q':
                    return "Success"
                break
            row += dr
            col += dc

    # If no threats are found, return "Fail"
    return "Fail"


def main():
    # Define a sample chess board as a multi-line string
    board = """
.......
.......
....K..
.......
..P....
.......
.......
"""
    # Print result of king-in-check detection
    print(is_king_in_check(board))

if __name__ == "__main__":
    # Run the main function if the script is executed directly
    main()
