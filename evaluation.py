from moves import generate_moves


def count(board: str, color: str) -> int:
    return board.count(color)


def static_opening(board: str) -> int:
    return count(board, "W") - count(board, "B")


def mobility(board: str, color: str) -> int:
    return len(generate_moves(board, "game", color))


def piece_terminal(board: str):
    if count(board, "B") <= 2:
        return 10000
    if count(board, "W") <= 2:
        return -10000
    return None


def static_game(board: str) -> int:
    done = piece_terminal(board)
    if done is not None:
        return done

    moves = mobility(board, "B")

    if moves == 0:
        return 10000

    return 1000 * (count(board, "W") - count(board, "B")) - moves


def improved_opening(board: str) -> int:
    raise NotImplementedError("improved opening estimate")


def improved_game(board: str) -> int:
    raise NotImplementedError("improved game estimate")