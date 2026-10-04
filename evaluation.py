from moves import MILLS, generate_moves


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


def mills(board: str, color: str) -> int:
    return sum(all(board[i] == color for i in line) for line in MILLS)


def threats(board: str, color: str) -> int:
    return sum(
        sorted(board[i] for i in line) == sorted(color * 2 + "x")
        for line in MILLS
    )


def improved_opening(board: str) -> int:
    return (
        10 * (count(board, "W") - count(board, "B"))
        + 100 * (mills(board, "W") - mills(board, "B"))
        + 40 * (threats(board, "W") - threats(board, "B"))
    )


def improved_game(board: str) -> int:
    raise NotImplementedError("improved game estimate")