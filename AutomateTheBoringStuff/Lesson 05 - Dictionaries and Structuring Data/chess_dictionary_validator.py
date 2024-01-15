def isValidChessBoard(board: dict):
    valid_names = ["pawn", "knight", "bishop", "rook", "queen", "king"]
    white_pawn = 0
    white_knight = 0
    white_bishop = 0
    white_rook = 0
    white_queen = 0
    white_king = 0
    
    black_pawn = 0
    black_knight = 0
    black_bishop = 0
    black_rook = 0
    black_queen = 0
    black_king = 0
    
    for location, piece in board.items():
        # Check that the first character is a number between 1 and 8
        if location[0] not in "12345678":
            return False
        # Check that the second character is a letter between a and h
        if location[1] not in "abcdefgh":
            return False
        
        # Check that the first letter of the piece is either w or b
        if piece[0] not in "wb":
            return False
        
        # Check that the remaining letters of the piece are valid
        if piece[1:] not in valid_names:
            return False
        
        # Add piece to the appropriate counter
        if piece == "wpawn":
            white_pawn += 1
        elif piece == "wknight":
            white_knight += 1
        elif piece == "wbishop":
            white_bishop += 1
        elif piece == "wrook":
            white_rook += 1
        elif piece == "wqueen":
            white_queen += 1
        elif piece == "wking":
            white_king += 1
        elif piece == "bpawn":
            black_pawn += 1
        elif piece == "bknight":
            black_knight += 1
        elif piece == "bbishop":
            black_bishop += 1
        elif piece == "brook":
            black_rook += 1
        elif piece == "bqueen":
            black_queen += 1
        elif piece == "bking":
            black_king += 1
    
    # Check that there are no more than 8 pawns
    if white_pawn > 8 or black_pawn > 8:
        return False
    
    # Check that there are no more than 2 knights
    if white_knight > 2 or black_knight > 2:
        return False
    
    # Check that there are no more than 2 bishops
    if white_bishop > 2 or black_bishop > 2:
        return False
    
    # Check that there are no more than 2 rooks
    if white_rook > 2 or black_rook > 2:
        return False
    
    # Check that there is only 1 queen
    if white_queen > 1 or black_queen > 1:
        return False
    
    # Check that there is only 1 king
    if white_king > 1 or black_king > 1:
        return False
    
    # Check that there are no more than 16 pieces per color
    if (white_pawn + white_knight + white_bishop + white_rook + white_queen + white_king) > 16:
        return False
    
    if (black_pawn + black_knight + black_bishop + black_rook + black_queen + black_king) > 16:
        return False
    
    return True
