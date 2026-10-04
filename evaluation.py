from moves import generate_moves


def count(board: str, color: str) -> int:
    return board.count(color)


def static_opening(board: str) -> int:
    return count(board, "W") - count(board, "B")


def black_moves(board: str) -> int:
    return len(generate_moves(board, "game", "B"))


def static_game(board: str) -> int:
    white, black = count(board, "W"), count(board, "B")
    if black <= 2:
        return 10000
    if white <= 2:
        return -10000
    moves = black_moves(board)
    if moves == 0:
        return 10000
    return 1000 * (white - black) - moves


def improved_opening(board: str) -> int:
    raise NotImplementedError("improved opening estimate")


def improved_game(board: str) -> int:
    raise NotImplementedError("improved game estimate")