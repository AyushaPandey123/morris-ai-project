"""Ayusha's move-generation module. Starter interfaces; implement one at a time.
Boards are immutable strings of 23 characters: W, B, x.
"""


def neighbors(location: int) -> list[int]:
    """Return adjacent indices from the VARIANT board diagram."""
    raise NotImplementedError("Ayusha: map the board neighbors")


def closeMill(location: int, board: str) -> bool:
    """Check whether W or B at location belongs to a completed mill; x is false."""
    raise NotImplementedError("Ayusha: check mills through this location")


def GenerateRemove(board: str, positions: list[str]) -> None:
    """Append one board per removable isolated Black piece.
    If none can be removed, append the unchanged board, per the handout.
    """
    raise NotImplementedError("Ayusha: generate captures")


def GenerateAdd(board: str) -> list[str]:
    """Place White on each empty point; resolve captures after a mill."""
    raise NotImplementedError("Ayusha: generate opening placements")


def GenerateMove(board: str) -> list[str]:
    """Move each White piece to each adjacent empty point; resolve captures."""
    raise NotImplementedError("Ayusha: generate adjacent moves")


def GenerateHopping(board: str) -> list[str]:
    """Move each White piece to each empty point; resolve captures."""
    raise NotImplementedError("Ayusha: generate hopping moves")


def GenerateMovesOpening(board: str) -> list[str]:
    """Opening dispatcher: use GenerateAdd."""
    raise NotImplementedError("Ayusha: connect opening generation")


def GenerateMovesMidgameEndgame(board: str) -> list[str]:
    """Use hopping at exactly 3 White pieces, otherwise adjacent moves.
    Search must handle terminal positions before expanding them.
    """
    raise NotImplementedError("Ayusha: connect movement generation")


def swap_colors(board: str) -> str:
    """Exchange W and B, preserving x and the order of locations."""
    raise NotImplementedError("Ayusha: support Black through color swapping")
