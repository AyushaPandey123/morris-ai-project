import sys
 
from evaluation import improved_opening
from runner import run
from search import minimax
 
if __name__ == "__main__":
    run(minimax, "opening", "W", improved_opening, sys.argv)
