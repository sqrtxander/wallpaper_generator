import argparse
import random
import sys
from .wallpaper_generator import WallpaperGenerator, generate_wallpaper
from .wallpapers import Delaunay, FilledDelaunay, Rects, Sierpinski, Tetris, Tree, Walk


WALLPAPERS = [Delaunay, FilledDelaunay, Rects, Sierpinski, Tetris, Tree, Walk]


def main() -> None:
    generate_wallpaper(random.choice(WALLPAPERS))


if __name__ == "__main__":
    main()
