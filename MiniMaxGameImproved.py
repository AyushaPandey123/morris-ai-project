import sys
 
from evaluation import improved_game
from runner import run
from search import minimax
 
if __name__ == "__main__":
    run(minimax, "game", "W", improved_game, sys.argv)
