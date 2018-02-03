import graphixhandler
import numberlist
import pygame
from Algorithms.quicksort import quick_sort


NUM_AMOUNT = 200
sort_func = quick_sort
def main():
    pygame.init()
    numarray = numberlist.Numbers(NUM_AMOUNT)
    handler = graphixhandler.GraphicHandler(numarray)
    handler.set_display_text((sort_func.__name__.replace("_", " ").title()))
    while True:
        sort_func(numarray,handler)
        pygame.time.wait(1000)
        numarray.reshuffle()


if __name__ == "__main__":
    main()