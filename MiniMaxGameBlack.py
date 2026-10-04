import sys
 
from evaluation import static_game
from runner import run
from search import minimax
 
if __name__ == "__main__":
    run(minimax, "game", "B", static_game, sys.argv)
