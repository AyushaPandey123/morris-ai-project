# Morris AI Project

This is our CS4346 project for the Morris Game, Variant. We are building the AI in Python and using this repo to keep our work together.

Right now we have the starter files. We still need to implement the functions and test everything.

## How we divided the work

| Who | Work |
| --- | --- |
| Me (Ayusha) | All the Generate functions in moves.py, plus neighbors, closeMill, and color swapping |
| Sajja | MINIMAX and ALPHA-BETA in search.py, the original evaluation functions in evaluation.py, and the programs that run them |
| Both of us | Playing as Black, improving the evaluation, combining our code, testing, and preparing the tournament agent |

This is how we split the work between us. The assignment has five parts, and we need to finish all of them.

## Working together

I will invite Sajja to this private repo through Settings > Collaborators > Add people. Once she accepts the invitation, we can both work here.

We will use separate branches for our work, like ayusha-moves and sajja-search. After finishing a small section, we will commit it and open a pull request to add it to main. Before starting more work, we will pull the latest changes. If we need to change something in each other's files, we will talk about it first.

## How our files connect

Our board will be a string with 23 characters:

- W = White piece
- B = Black piece
- x = empty spot

We will follow the position numbers in the Morris handout. The Generate functions will return a list of possible new boards and leave the original board unchanged.

GenerateRemove(board, positions) will add the boards after removing eligible Black pieces to the positions list. neighbors(location) will give us the connected spots, and closeMill(location, board) will tell us whether that spot is part of a mill. For Black's moves, we will swap the colors, use White's move generator, and swap them back.

The search will return the best next board, its estimate, and how many positions were evaluated. For the original White programs, a higher score means better for White. Each level of the search switches whose turn it is. We will use the same move order and choose the first best move when scores tie, so MINIMAX and ALPHA-BETA give the same result.

We also need to count placement turns separately. A piece being captured does not mean that player gets another opening placement.

## Files we need to submit

- MiniMaxOpening.py
- MiniMaxGame.py
- ABOpening.py
- ABGame.py
- MiniMaxOpeningBlack.py
- MiniMaxGameBlack.py
- MiniMaxOpeningImproved.py
- MiniMaxGameImproved.py
- Examples.txt
- MyStaticEstimation.txt
- TournamentAgent.py, if we make a separate tournament program

Examples.txt needs at least two examples where ALPHA-BETA evaluates fewer positions than MINIMAX.

In MyStaticEstimation.txt, we need to explain what our improved evaluation checks, why we chose those features, and how we combine them. We also need at least two board positions where it chooses a different move from the original evaluation, with an explanation of why we prefer that move.

We will submit one ZIP and include any helper files that our programs import, so everything runs after extracting it.

Example command:

~~~sh
python MiniMaxOpening.py board1.txt board2.txt 2
~~~

The program reads board1.txt, searches to depth 2, and writes the chosen board to board2.txt. It also needs to print:

~~~text
Board Position: ...
Positions evaluated by static estimation: ...
MINIMAX estimate: ...
~~~

## Our plan

1. I will start with neighbors and closeMill, then do GenerateAdd and GenerateRemove, followed by moving and hopping.
2. Sajja will work on the original evaluation functions and MINIMAX.
3. We will connect our code and get the opening program working first.
4. Then we will finish ALPHA-BETA, Black support, and the improved evaluation.
5. Finally, we will test full games and prepare our ZIP.

## Things we need to test

We want a strong agent for the competition, so we need to check more than whether the code runs.

- Our neighbors and mills match the variant board in the handout.
- Placing, moving, hopping, and capturing all produce legal boards.
- Hopping happens only when the player has exactly three pieces.
- If all opponent pieces are in mills, we follow the handout's rule and leave the board unchanged instead of removing a piece.
- Swapping colors twice gives us the original board.
- MINIMAX and ALPHA-BETA choose the same move and estimate at the same depth.
- We handle a player having only two pieces or no legal moves during the game phase.
- We test our improved evaluation in practice games before deciding which features to keep.
- Our agent works for both White and Black.
- We finish the search early enough to post within the four-minute limit.

Once the basic search works, we can try better move ordering and increasing the search depth gradually with ALPHA-BETA. We need to keep the best move from the last completed search in case time runs out, and stay within the algorithms allowed in class.

During games, we will keep track of the turn, move number, the 18 opening placements, and repeated positions. The same board with the same player to move three times is a draw. We will also check that the other team's move is legal.

## Deadlines

- Project submission: October 8, 2026
- Schedule official matches by: October 8, 2026
- Finish official tournament games by: October 15, 2026

We will use the Teams chat as the official game record and choose one person to post our moves for each game.
