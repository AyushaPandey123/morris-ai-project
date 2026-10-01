"""Teammate's search module. Starter interfaces, not a working agent.
Implement class MINIMAX first, then ALPHA-BETA with the same tie breaking.
"""
from dataclasses import dataclass
from typing import Callable


@dataclass(frozen=True)
class SearchResult:
    board: str  # selected immediate child of the input board
    estimate: int  # White-perspective evaluation
    positions_evaluated: int  # actual calls to static estimation


def minimax(board: str, depth: int, phase: str, player: str,
            evaluator: Callable[[str], int]) -> SearchResult:
    """phase is opening or game; player is W or B.
    Alternate colors; White maximizes and Black minimizes.
    Handle terminal states before expansion and return the first best child.
    Use Ayusha's moves.py; do not duplicate the move rules here.
    """
    raise NotImplementedError("Teammate: implement MINIMAX")


def alphabeta(board: str, depth: int, phase: str, player: str,
              evaluator: Callable[[str], int]) -> SearchResult:
    """Same contract as minimax; prune using class ALPHA-BETA rules."""
    raise NotImplementedError("Teammate: implement ALPHA-BETA")
