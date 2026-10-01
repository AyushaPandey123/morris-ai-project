# Morris AI Project

Private CS4346 team workspace for the 23-location Morris Variant.
**Status: starter structure only; the agent is not implemented yet.**

## Our three work groups

These are our team work groups; the assignment itself has Parts I-V.

| Owner | Files and responsibilities |
| --- | --- |
| Ayusha | moves.py: GenerateMovesOpening, GenerateMovesMidgameEndgame, GenerateAdd, GenerateMove, GenerateHopping, GenerateRemove, neighbors, closeMill, and color swapping |
| Teammate | search.py and evaluation.py: MINIMAX, ALPHA-BETA, original static estimators, and command-line programs |
| Together | Black support, improved evaluation, integration, examples, tournament agent, and practice matches |

## Collaborating

The owner invites the teammate through Settings > Collaborators > Add people. The teammate accepts the GitHub invitation; sending the repository link alone does not grant private access.
Both members work in this SAME repository. Use short branches such as ayusha-moves and teammate-search, commit small changes, and open pull requests to main. Review shared interfaces before merging. Pull the newest main before starting a new branch. Do not edit the other person's files without coordinating.

## Shared interfaces

Use immutable 23-character strings containing only W, B, x. Index locations exactly as shown in the Morris handout. Move generators return a list of new board strings and never alter the input. White is the default color for the handout routines. GenerateRemove(board, positions) appends results to positions, matching the handout. neighbors(location) returns neighbor indices; closeMill(location, board) returns bool. Swap colors to reuse White generation for Black.

Search should return the selected immediate child, estimate, and number of static evaluations. Evaluate from White's perspective for the original White programs. Alternate White and Black at every search level. Use consistent move ordering and first-best tie breaking so MINIMAX and ALPHA-BETA agree. Keep opening phase tracking separate from current piece counts: captures do not undo placement turns.

## Required submission files

- MiniMaxOpening.py and MiniMaxGame.py
- ABOpening.py and ABGame.py
- MiniMaxOpeningBlack.py and MiniMaxGameBlack.py
- MiniMaxOpeningImproved.py and MiniMaxGameImproved.py
- Examples.txt (include at least two pruning comparisons)
- MyStaticEstimation.txt (features, rationale, combination, and at least two positions where the improved estimator chooses a different move)
- TournamentAgent.py if we use a separate tournament program

Include all imported helper modules in the ZIP so the programs run after extraction. Follow the instructor's instructions if a particular ZIP layout is required.
Each required CLI receives input file, output file, depth, for example:

~~~sh
python MiniMaxOpening.py board1.txt board2.txt 2
~~~

Print Board Position, Positions evaluated by static estimation, and MINIMAX estimate as specified; write the selected board to the output file.

## Build order

1. Ayusha starts with neighbors and closeMill, then GenerateAdd and GenerateRemove, then adjacent moves and hopping.
2. Teammate implements the original evaluators and MINIMAX against the shared interfaces.
3. Connect one complete opening program before adding ALPHA-BETA and the remaining entry points.
4. Add Black support and improved evaluation together.
5. Run practice games, compare candidate heuristics, and prepare the submission ZIP.

## Tournament strength checklist

- Validate adjacency and mills against the VARIANT board, not a standard Nine Men's Morris board.
- Verify placement, movement, hopping at exactly three pieces, captures, no isolated Black pieces, and terminal positions. Follow the handout's no-removal case when all opponent pieces are in mills.
- Confirm color swapping twice restores the board, and Black generation mirrors White correctly.
- Confirm equal-depth MINIMAX and ALPHA-BETA agree on estimate and move; count evaluated leaves correctly.
- Handle reduced-to-two and blocked-player terminal cases in the proper phase.
- Compare mobility, mill threats, completed mills, and blocked pieces using actual practice results. A complicated heuristic is not automatically stronger.
- After correctness, consider move ordering and iterative deepening WITH ALPHA-BETA; retain the last completed legal move and stop comfortably before the 4-minute posting deadline. Keep enhancements consistent with class rules.
- Track placement turns (18 total), player to move, move number, repetition, search time, depth, and evaluation counts. Three identical positions with the same player to move are a draw.
- Test both colors, multiple positions, and complete games. Check every opponent move against our legal successors.

## Dates from the project handout

Final submission and official match scheduling: October 8, 2026.
Official tournament games complete: October 15, 2026.
Teams chat is the official game record; assign one communicator per team per game.

Winning cannot be guaranteed. Our priorities are legal moves, correct search, a tested evaluator, and reliable time control.
