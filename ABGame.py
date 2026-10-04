import sys
 
from evaluation import static_game
from runner import run
from search import alphabeta
 
if __name__ == "__main__":
    run(alphabeta, "game", "W", static_game, sys.argv)
