import random
import math
import argparse
from typing import override
import os
from PIL import Image, ImageDraw
import util.get_opts as opts
from util.wallpaper_generator import WallpaperGenerator


class Tree(WallpaperGenerator):
    def __init__(self, base: str):
        super().__init__()
        self.out_base: str = base or "tree.png"

    @override
    def generate(self):
        def tree_path(point: tuple[float, float], angle: float, r: float):
            if r < threshold:
                return

            p = (
                point[0] + r * math.cos(math.radians(angle)),
                point[1] + -r * math.sin(math.radians(angle)),
            )

            draw.line(
                (point, p),
                width = int(self.LINE_WIDTH * opts.SCALE),
                fill=random.choice(opts.PALETTE)
            )

            tree_path(p, angle + left_angle, r * 0.75)
            tree_path(p, angle - right_angle, r * 0.75)

        img = Image.new(
            "RGB",
            (opts.WIDTH, opts.HEIGHT),
            opts.BACKGROUND,
        )
        draw = ImageDraw.Draw(img)
        left_angle: float = random.randint(10, 60)
        right_angle: float = random.randint(10, 60)
        initial_r = opts.HEIGHT // 4
        initial_p = (opts.WIDTH // 2, opts.HEIGHT * 7 // 8)
        threshold: float = opts.SCALE * initial_r / 20
        tree_path(initial_p, 90, initial_r)

        img.save(os.path.join(self.out_dir, self.out_base))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-o", "--output")
    args = parser.parse_args()
    Tree(args.output).generate()
