import sys
 
from evaluation import static_opening
from runner import run
from search import minimax
 
if __name__ == "__main__":
    run(minimax, "opening", "W", static_opening, sys.argv)
