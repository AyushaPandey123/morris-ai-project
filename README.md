# Morris AI Project

CS4346: Introduction to Artificial Intelligence

A Python project for the Morris Game, Variant, covering move generation, MINIMAX, ALPHA-BETA pruning, static evaluation, and tournament play.

## Team Contributions

We divided the project into move generation, search, and joint integration work.

| Team member | Assigned components |
| --- | --- |
| Ayusha Pandey | All Generate functions, neighbors, closeMill, and color swapping in moves.py |
| Sajja | MINIMAX and ALPHA-BETA in search.py, original evaluation in evaluation.py, and command-line programs |
| Both members | Black-player support, improved evaluation, integration, examples, testing, and tournament preparation |

## Collaboration

We worked on separate branches for our respective components and used the shared repository to coordinate our work. Small commits and pull requests were used to combine changes in main. Changes affecting both components were reviewed together.

## Current Status

Starter interfaces have been added in moves.py, search.py, and evaluation.py. Algorithm implementation and testing are still pending.

## Board Representation

Board positions use 23-character strings, with indices matching the Morris Variant handout.

| Character | Meaning |
| --- | --- |
| W | White piece |
| B | Black piece |
| x | Empty location |

Opening moves place nine pieces per player. Midgame moves use adjacent empty locations. A player with exactly three pieces can hop to any empty location. Placement turns are tracked separately from remaining piece counts after captures.

## Module Interfaces

Move generators return lists of new board strings without changing the input. GenerateRemove(board, positions) appends capture results. neighbors(location) returns adjacent indices, and closeMill(location, board) checks for a completed mill. Black moves reuse White generation through color swapping.

Search returns the selected immediate successor, estimate, and static evaluation count. Original evaluation uses White's perspective. Search alternates players and uses consistent move ordering and first-best tie breaking.

## Required Programs

| File | Purpose |
| --- | --- |
| MiniMaxOpening.py | White opening MINIMAX |
| MiniMaxGame.py | White midgame/endgame MINIMAX |
| ABOpening.py | Opening ALPHA-BETA |
| ABGame.py | Midgame/endgame ALPHA-BETA |
| MiniMaxOpeningBlack.py | Black opening MINIMAX |
| MiniMaxGameBlack.py | Black midgame/endgame MINIMAX |
| MiniMaxOpeningImproved.py | Opening with improved evaluation |
| MiniMaxGameImproved.py | Midgame/endgame with improved evaluation |
| TournamentAgent.py | Optional separate tournament agent |

These programs remain to be implemented.

## Usage

Required command format:

~~~sh
python MiniMaxOpening.py board1.txt board2.txt 2
~~~

Arguments specify the input board file, output board file, and search depth. The selected board is written to the output file. Required console output:

~~~text
Board Position: ...
Positions evaluated by static estimation: ...
MINIMAX estimate: ...
~~~

## Testing Requirements

- Verify neighbors and mills against the variant board.
- Check placement, adjacent movement, hopping at exactly three pieces, and captures.
- Follow the handout's unchanged-board case when all opponent pieces are in mills.
- Verify both colors and confirm that swapping colors twice restores the board.
- Compare MINIMAX and ALPHA-BETA at equal depth with identical tie breaking.
- Count actual static evaluation calls and handle terminal game positions.
- Compare improved evaluation features using practice games.
- Test full games and search time before tournament use.

## Documentation

Examples.txt must include at least two cases where ALPHA-BETA evaluates fewer positions than MINIMAX.

MyStaticEstimation.txt must explain the improved evaluation's features, rationale, and combination. It must include at least two board positions where the improved evaluation selects a different move, with an explanation of the preferred move.

## Tournament

The agent must support both colors and all game phases, use the class MINIMAX or ALPHA-BETA algorithms, and respond within four minutes. Move ordering and iterative deepening with ALPHA-BETA are potential improvements, subject to course requirements.

Game records include the move number, player, and board position. Three repetitions of the same board with the same player to move result in a draw. Teams chat serves as the official record, with one designated communicator per team per game.

## Submission and Deadlines

Submit one ZIP containing all required programs, Examples.txt, MyStaticEstimation.txt, and imported helper modules. Include TournamentAgent.py if a separate tournament program is used.

| Deadline | Date |
| --- | --- |
| Final project submission | October 8, 2026 |
| Official match scheduling | October 8, 2026 |
| Official tournament completion | October 15, 2026 |
