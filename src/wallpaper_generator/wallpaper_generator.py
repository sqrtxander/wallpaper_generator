import random
import argparse
from .opts import Opts


class WallpaperGenerator:
    def __init__(self, out_path: str, config_path: str, seed: int | None) -> None:
        self.out_path: str = out_path
        self.opts = Opts(config_path)
        self.LINE_WIDTH: int = int(8 * self.opts.SCALE)
        self.CIRCLE_RADIUS: int = int(12 * self.opts.SCALE)
        self.SCREEN_SCALE: float = 150 * self.opts.SCALE

        if seed is not None:
            random.seed(seed)

    def generate(self): ...


def generate_wallpaper(Cls: type[WallpaperGenerator]) -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("-o", "--output", type=str, required=True)
    parser.add_argument("-c", "--config", type=str, default="config.json")
    parser.add_argument("-s", "--seed", type=int, default=None)
    args = parser.parse_args()
    Cls(args.output, args.config, args.seed).generate()
