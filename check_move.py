"""Check a move. Usage: python check_move.py <previous_board> <new_board> <move_number>
Move numbers: odd = White, even = Black. Moves 1-18 are placements."""
import sys

from moves import generate_moves, validate_board
from TournamentAgent import phase_of

if len(sys.argv) != 4:
    sys.exit(__doc__)
prev, new, number = sys.argv[1], sys.argv[2], int(sys.argv[3])
mover, phase = ("W" if number % 2 else "B"), phase_of(number)
try:
    validate_board(prev)
    validate_board(new)
except ValueError as error:
    sys.exit(f"ILLEGAL: {error} (check length is 23 and only W, B, x)")
if new in generate_moves(prev, phase, mover):
    print(f"LEGAL: valid {phase} move for {mover}")
else:
    diff = [f"spot {i}: {prev[i]} -> {new[i]}" for i in range(23) if prev[i] != new[i]]
    print(f"ILLEGAL for {mover} in the {phase} phase. Changed spots:")
    print("\n".join(diff) if diff else "none (board unchanged)")
    print("Hint: closing a mill also requires removing one opponent piece that is not in a mill.")