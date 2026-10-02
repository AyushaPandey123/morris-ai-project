from dataclasses import dataclass
from typing import Callable


@dataclass(frozen=True)
class SearchResult:
    board: str  # Best next board
    estimate: int  # White score
    positions_evaluated: int  # Evaluation count


def minimax(board: str, depth: int, phase: str, player: str,
            evaluator: Callable[[str], int]) -> SearchResult:
    raise NotImplementedError("MINIMAX not implemented")


def alphabeta(board: str, depth: int, phase: str, player: str,
              evaluator: Callable[[str], int]) -> SearchResult:
    raise NotImplementedError("ALPHA-BETA not implemented")
