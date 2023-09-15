from game_helper import PipToken, Piece, Board, tarot_decorator

# Define Tarot-Mapped Chess Pieces
@tarot_decorator("The Fool", point_value=10)
class ChessKing(Piece):
    pass

@tarot_decorator("The Magician", point_value=9)
class ChessQueen(Piece):
    pass

@tarot_decorator("The Chariot", point_value=5)
class ChessRook(Piece):
    pass

@tarot_decorator("The Hermit", point_value=3)
class ChessBishop(Piece):
    pass

@tarot_decorator("Strength", point_value=3)
class ChessKnight(Piece):
    pass

@tarot_decorator("The Wheel of Fortune", point_value=1)
class ChessPawn(Piece):
    pass

def main():
    # Create Tokens
    token1 = PipToken(value=1, type='pawn')
    token2 = PipToken(value=2, type='knight')
    token3 = PipToken(value=3, type='bishop')

    # Create Pieces
    king = ChessKing(tokens=[token1])
    queen = ChessQueen(tokens=[token2])
    bishop = ChessBishop(tokens=[token3])

    # Create Board
    board = Board(rows=8, cols=8)

    # Place Pieces
    board.place_piece(king, (0, 0))
    board.place_piece(queen, (0, 1))
    board.place_piece(bishop, (0, 2))

    # Perform Actions
    king.place((0, 0))
    queen.move((1, 1))
    king.capture(queen)
    bishop.teleport((4, 4))
    bishop.heal()

    # Calculate Score and Check Board State
    board.calculate_score()
    state = board.check_state()
    print(f"Board State: {state}")

if __name__ == "__main__":
    main()
  
