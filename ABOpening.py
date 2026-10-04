import sys
 
from evaluation import static_opening
from runner import run
from search import alphabeta
 
if __name__ == "__main__":
    run(alphabeta, "opening", "W", static_opening, sys.argv)
