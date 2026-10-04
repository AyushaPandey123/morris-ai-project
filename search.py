from dataclasses import dataclass
from typing import Callable
 
from moves import generate_moves
 
WIN = 10000
 
 
@dataclass(frozen=True)
class SearchResult:
    board: str  # Best next board
    estimate: int  # White score
    positions_evaluated: int  # Evaluation count
 
 
def other(player: str) -> str:
    return "B" if player == "W" else "W"
 
 
def is_leaf(board: str, depth: int, phase: str) -> bool:
    if depth == 0:
        return True
    return phase == "game" and min(board.count("W"), board.count("B")) <= 2
 
 
def stuck_score(player: str) -> int:
    return -WIN if player == "W" else WIN
 
 
def better(player: str, new: int, best: int) -> bool:
    return new > best if player == "W" else new < best
