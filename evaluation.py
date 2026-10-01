"""Static estimators. Teammate implements original; both design improved.
Return integer scores from White's perspective.
"""


def static_opening(board: str) -> int:
    """Original handout estimator: White count minus Black count."""
    raise NotImplementedError("Teammate: original opening estimate")


def static_game(board: str) -> int:
    """Implement handout terminal values, piece difference and Black move count."""
    raise NotImplementedError("Teammate: original game estimate")


def improved_opening(board: str) -> int:
    """Joint task: design, document, and test an opening heuristic."""
    raise NotImplementedError("Together: improved opening estimate")


def improved_game(board: str) -> int:
    """Joint task: retain terminal handling and test strategic features."""
    raise NotImplementedError("Together: improved game estimate")
