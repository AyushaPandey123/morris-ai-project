import sys
 
 
def read_board(path: str) -> str:
    with open(path) as f:
        return f.read().strip()
 
 
def write_board(path: str, board: str) -> None:
    with open(path, "w") as f:
        f.write(board + "\n")
 
 
def report(result) -> None:
    print(f"Board Position: {result.board}")
    print(f"Positions evaluated by static estimation: {result.positions_evaluated}")
    print(f"MINIMAX estimate: {result.estimate}")
 
 
def run(algorithm, phase, player, evaluator, argv) -> None:
    if len(argv) != 4:
        sys.exit(f"Usage: python {argv[0]} <input_board> <output_board> <depth>")
    board = read_board(argv[1])
    result = algorithm(board, int(argv[3]), phase, player, evaluator)
    write_board(argv[2], result.board)
    report(result)
