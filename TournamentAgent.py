import sys
import time
 
from evaluation import improved_game, improved_opening
from runner import read_board, write_board
from search import WIN, alphabeta
 
OPENING_PLIES = 18
BUDGET = 120  # seconds, well under the 4 minute limit
NAMES = {"W": "White", "B": "Black"}
 
 
def phase_of(move_number: int) -> str:
    return "opening" if move_number <= OPENING_PLIES else "game"
 
 
def max_depth(move_number: int) -> int:
    # Do not search past the last placement; the opening generator only places.
    return OPENING_PLIES - move_number + 1 if move_number <= OPENING_PLIES else 99
 
 
def choose_move(board, player, move_number, budget=BUDGET):
    phase = phase_of(move_number)
    evaluator = improved_opening if phase == "opening" else improved_game
    start, depth, best = time.time(), 1, None
    while depth <= max_depth(move_number):
        tick = time.time()
        best = alphabeta(board, depth, phase, player, evaluator)
        spent = time.time() - tick
        if abs(best.estimate) >= WIN or time.time() - start + 10 * spent > budget:
            break  # forced result, or the next depth would be too slow
        depth += 1
    return best, depth
 
 
def main(argv):
    if len(argv) != 5:
        sys.exit("Usage: python TournamentAgent.py <in> <out> <W|B> <move_number>")
    player, number = argv[3], int(argv[4])
    best, depth = choose_move(read_board(argv[1]), player, number)
    write_board(argv[2], best.board)
    print(f"Searched depth {depth}, estimate {best.estimate}, "
          f"{best.positions_evaluated} positions at the last depth")
    print(f"Move {number} - {NAMES[player]}")
    print(best.board)
 
 
if __name__ == "__main__":
    main(sys.argv)
