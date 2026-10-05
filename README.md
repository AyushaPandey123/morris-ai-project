# Morris AI Project

CS4346: Introduction to Artificial Intelligence

A Python program that plays the Morris Game, Variant, a 23-spot cousin of Nine Men's Morris. It generates legal moves, searches with MINIMAX or ALPHA-BETA, scores positions with a static evaluation, and can play either color as a tournament agent.

## Team Contributions

| Team member | Components |
| --- | --- |
| Ayusha Pandey | All Generate functions, neighbors, closeMill, and color swapping in moves.py |
| Sajja Regmi| MINIMAX and ALPHA-BETA in search.py, original evaluation in evaluation.py, and command-line programs |
| Both members | Black-player support, improved evaluation, integration, examples, testing, and tournament agent |

We worked on separate branches for our components, merged small commits into main, and reviewed shared changes together.

## The Game

Two players, White and Black, each have 9 pieces. The goal is to reduce the opponent to 2 pieces or leave them with no legal move.

- **Opening:** players take turns placing pieces on empty spots.
- **Midgame:** players move one piece to an adjacent empty spot.
- **Endgame:** a player with exactly three pieces may hop to any empty spot.
- **Mills:** three of your pieces on one line is a mill. Closing a mill removes one opponent piece that is not itself in a mill. If every opponent piece is in a mill, nothing is removed.

The board has no d2 spot, so c2 and e2 are neighbors, d1 has three neighbors, and no mill crosses the center. There are 18 mill lines: seven horizontal, seven vertical, and four diagonal.

## Board Representation

A position is a 23-character string. Indices follow the Morris Variant handout (0 is a0, 1 is d0, 2 is g0, and so on up to 22 for g6).

| Character | Meaning |
| --- | --- |
| W | White piece |
| B | Black piece |
| x | Empty location |

## Setup

Python 3.9 or newer, standard library only.

~~~sh
git clone <repository-url>
cd morris-ai-project
~~~

## Usage

Each program takes an input board file, an output board file, and a search depth:

~~~sh
echo WxxxxBxxxxxxxxxxxxxxxxx > board1.txt
python MiniMaxOpening.py board1.txt board2.txt 2
~~~

The input file holds one 23-character board. The chosen board is written to the output file, which is overwritten on each run. Console output:

~~~text
Board Position: WWxxxBxxxxxxxxxxxxxxxxx
Positions evaluated by static estimation: 420
MINIMAX estimate: 0
~~~

| Program | What it does |
| --- | --- |
| MiniMaxOpening.py | White, opening phase, MINIMAX |
| MiniMaxGame.py | White, midgame/endgame, MINIMAX |
| ABOpening.py | White, opening phase, ALPHA-BETA |
| ABGame.py | White, midgame/endgame, ALPHA-BETA |
| MiniMaxOpeningBlack.py | Black, opening phase, MINIMAX |
| MiniMaxGameBlack.py | Black, midgame/endgame, MINIMAX |
| MiniMaxOpeningImproved.py | White, opening phase, improved evaluation |
| MiniMaxGameImproved.py | White, midgame/endgame, improved evaluation |
| TournamentAgent.py | Full agent for either color and any phase |

ALPHA-BETA returns the same board and estimate as MINIMAX with fewer evaluations. On the board above at depth 2, MiniMaxOpening.py evaluates 420 positions and ABOpening.py evaluates 40. More comparisons are in Examples.txt.

## Tournament Agent

TournamentAgent.py uses ALPHA-BETA with the improved evaluation and iterative deepening. It searches depth 1, 2, 3, and so on, keeps the last completed result, and stops when the next depth would not fit in its 120-second budget or when a win or loss is forced. During the opening it never searches past the last placement.

~~~sh
python TournamentAgent.py in.txt out.txt W 1
~~~

Arguments: input board file, output board file, the color to play (W or B), and the move number of the move being made. White plays odd move numbers and Black plays even ones. Moves 1 to 18 are placements, and later moves move pieces. The agent prints the line to post:

~~~text
Move 1 - White
Wxxxxxxxxxxxxxxxxxxxxxx
~~~

The agent does not check the opponent's moves or detect repeated positions.

### Practice helpers

| Command | Purpose |
| --- | --- |
| python selfplay.py | Agent plays both colors and prints every move |
| python practice.py B 20 | Play against the agent (agent is Black, 20 seconds per move) |
| python check_move.py PREVIOUS_BOARD NEW_BOARD MOVE_NUMBER | Report whether a move is legal |

## How It Works

### Project layout

| File | Responsibility |
| --- | --- |
| moves.py | Neighbors, mills, move generation, captures, color swapping |
| evaluation.py | Static estimates, original and improved |
| search.py | MINIMAX and ALPHA-BETA |
| runner.py | Read and write board files, print results |
| Program files | Combine an algorithm, phase, player, and evaluator |
| TournamentAgent.py | Chooses a move within a time budget |

### Move generation

Generators return new boards without changing the input. When a move closes a mill, one board is generated for each removable opponent piece, and search picks among them. Black moves reuse White generation by swapping colors, generating, and swapping back.

### Search

Both algorithms share one interface:

~~~python
minimax(board, depth, phase, player, evaluator) -> SearchResult(board, estimate, positions_evaluated)
alphabeta(board, depth, phase, player, evaluator) -> SearchResult(board, estimate, positions_evaluated)
~~~

- `phase` is "opening" or "game" and stays fixed during one search.
- `player` is the side to move. White maximizes and Black minimizes.
- Evaluators take a board and return an int scored from White's perspective.
- Ties go to the first child with a strictly better value, so both algorithms choose the same move.
- `positions_evaluated` counts actual evaluator calls.
- A game-phase position where either side has 2 or fewer pieces is not expanded. A player with no legal move loses.

### Static evaluation

Original estimates:

- Opening: white pieces minus black pieces.
- Midgame/endgame: 10000 if Black has 2 or fewer pieces or no moves, -10000 if White has 2 or fewer pieces, otherwise 1000 times the piece difference minus Black's number of moves.

Improved estimates (rationale and example positions in MyStaticEstimation.txt):

- Opening: 10 * pieces + 100 * mills + 40 * threats.
- Midgame/endgame: 1000 * pieces + 150 * mills + 60 * threats + 20 * mobility.
- Every feature is White minus Black. A threat is a line with two own pieces and one empty spot. Terminal positions match the original estimate.
