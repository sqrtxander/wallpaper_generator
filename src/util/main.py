import argparse
from util.wallpaper_generator import WallpaperGenerator


def main(Cls: type[WallpaperGenerator]):
    parser = argparse.ArgumentParser()
    parser.add_argument("-o", "--output", type=str, required=True)
    parser.add_argument("-c", "--config", type=str, default="config.json")
    parser.add_argument("-s", "--seed", type=int, default=None)
    args = parser.parse_args()
    Cls(args.output, args.config, args.seed).generate()
