"""Move generation for the 23-location Morris Variant.

White generators follow the supplied handout. Black uses color swapping.
Boards are strings; results never modify the input. Order is deterministic.
"""

NEIGHBORS = (
    (1, 3, 8), (0, 4, 2), (1, 5, 13), (0, 4, 6, 9),
    (1, 3, 5), (2, 4, 7, 12), (3, 7, 10), (5, 6, 11),
    (0, 9, 20), (3, 8, 10, 17), (6, 9, 14), (7, 12, 16),
    (5, 11, 13, 19), (2, 12, 22), (10, 15, 17),
    (14, 16, 18), (11, 15, 19), (9, 14, 18, 20),
    (15, 17, 19, 21), (12, 16, 18, 22), (8, 17, 21),
    (18, 20, 22), (13, 19, 21),
)

MILLS = (
    (0, 1, 2), (3, 4, 5), (8, 9, 10), (11, 12, 13),
    (14, 15, 16), (17, 18, 19), (20, 21, 22),
    (0, 8, 20), (3, 9, 17), (6, 10, 14),
    (15, 18, 21), (7, 11, 16), (5, 12, 19), (2, 13, 22),
    (0, 3, 6), (2, 5, 7), (14, 17, 20), (16, 19, 22),
)

# There is no d2 location: the bottom central line has no three-point mill.
MILLS_AT = tuple(tuple(m for m in MILLS if i in m) for i in range(23))


def validate_board(board: str) -> None:
    if not isinstance(board, str) or len(board) != 23:
        raise ValueError("Board must be a string of exactly 23 characters")
    if any(piece not in "WBx" for piece in board):
        raise ValueError("Board may contain only W, B, and x")


def _validate_location(location: int) -> None:
    if not isinstance(location, int) or isinstance(location, bool) or not 0 <= location < 23:
        raise ValueError("Location must be an integer from 0 to 22")


def neighbors(location: int) -> list[int]:
    _validate_location(location)
    return list(NEIGHBORS[location])


def _close_mill(location: int, board: str) -> bool:
    color = board[location]
    return color != "x" and any(all(board[i] == color for i in mill)
                                for mill in MILLS_AT[location])


def closeMill(location: int, board: str) -> bool:
    validate_board(board)
    _validate_location(location)
    return _close_mill(location, board)


def _remove(board: str, positions: list[str]) -> None:
    removed = False
    for location, piece in enumerate(board):
        if piece == "B" and not _close_mill(location, board):
            positions.append(board[:location] + "x" + board[location + 1:])
            removed = True
    if not removed:
        positions.append(board)


def GenerateRemove(board: str, positions: list[str]) -> None:
    """Append captures; if no isolated Black piece exists, append unchanged board."""
    validate_board(board)
    _remove(board, positions)


def _finish(board: str, destination: int, positions: list[str]) -> None:
    if _close_mill(destination, board):
        _remove(board, positions)
    else:
        positions.append(board)


def GenerateAdd(board: str) -> list[str]:
    validate_board(board)
    positions = []
    for location, piece in enumerate(board):
        if piece == "x":
            new_board = board[:location] + "W" + board[location + 1:]
            _finish(new_board, location, positions)
    return positions


def _movement(board: str, hopping: bool) -> list[str]:
    positions = []
    for source, piece in enumerate(board):
        if piece != "W":
            continue
        destinations = range(23) if hopping else NEIGHBORS[source]
        for destination in destinations:
            if board[destination] == "x":
                cells = list(board)
                cells[source] = "x"
                cells[destination] = "W"
                _finish("".join(cells), destination, positions)
    return positions


def GenerateMove(board: str) -> list[str]:
    validate_board(board)
    return _movement(board, False)


def GenerateHopping(board: str) -> list[str]:
    validate_board(board)
    return _movement(board, True)


def GenerateMovesOpening(board: str) -> list[str]:
    return GenerateAdd(board)


def GenerateMovesMidgameEndgame(board: str) -> list[str]:
    validate_board(board)
    if board.count("W") == 3:
        return GenerateHopping(board)
    return GenerateMove(board)


def swap_colors(board: str) -> str:
    validate_board(board)
    return board.translate(str.maketrans("WB", "BW"))


def generate_moves(board: str, phase: str, player: str = "W") -> list[str]:
    """Shared search adapter. phase is opening or game; player is W or B.

    The game dispatcher follows the handout exactly; search handles terminal
    positions before expansion. Opening placement counters belong to the caller.
    """
    validate_board(board)
    if player not in ("W", "B"):
        raise ValueError("Player must be W or B")
    if phase not in ("opening", "game"):
        raise ValueError("Phase must be opening or game")
    generator = GenerateMovesOpening if phase == "opening" else GenerateMovesMidgameEndgame
    if player == "W":
        return generator(board)
    return [swap_colors(result) for result in generator(swap_colors(board))]
