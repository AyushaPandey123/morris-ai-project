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

def _minimax(board, depth, phase, player, evaluator, count):
    if is_leaf(board, depth, phase):
        count[0] += 1
        return evaluator(board), board
    children = generate_moves(board, phase, player)
    if not children:
        return stuck_score(player), board
    best_score, best_child = None, None
    for child in children:
        score, _ = _minimax(child, depth - 1, phase, other(player), evaluator, count)
        if best_child is None or better(player, score, best_score):
            best_score, best_child = score, child
    return best_score, best_child


def minimax(board: str, depth: int, phase: str, player: str,
            evaluator: Callable[[str], int]) -> SearchResult:
    count = [0]
    score, child = _minimax(board, depth, phase, player, evaluator, count)
    return SearchResult(child, score, count[0])


def _alphabeta(board, depth, phase, player, evaluator, count, alpha, beta):
    if is_leaf(board, depth, phase):
        count[0] += 1
        return evaluator(board), board
    children = generate_moves(board, phase, player)
    if not children:
        return stuck_score(player), board
    best_score, best_child = None, None
    for child in children:
        score, _ = _alphabeta(child, depth - 1, phase, other(player),
                              evaluator, count, alpha, beta)
        if best_child is None or better(player, score, best_score):
            best_score, best_child = score, child
        if player == "W":
            alpha = max(alpha, best_score)
        else:
            beta = min(beta, best_score)
        if alpha >= beta:
            break
    return best_score, best_child

def alphabeta(board: str, depth: int, phase: str, player: str,
              evaluator: Callable[[str], int]) -> SearchResult:
    count = [0]
    score, child = _alphabeta(board, depth, phase, player, evaluator,
                              count, float("-inf"), float("inf"))
    return SearchResult(child, score, count[0])

