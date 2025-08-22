import random
import math
import argparse
from typing import override
import os
from PIL import Image, ImageDraw
import util.get_opts as opts
from util.wallpaper_generator import WallpaperGenerator


class Sierpinski(WallpaperGenerator):
    def __init__(self, base: str):
        super().__init__()
        self.out_base: str = base or "sierpinski.png"

    @override
    def generate(self):
        def midpoint(p1: tuple[float, float], p2: tuple[float, float]) -> tuple[float, float]:
            x1, y1 = p1
            x2, y2 = p2
            return (x1 + x2) / 2, (y1 + y2) / 2
        def sierpinsify(points: tuple[tuple[float, float], tuple[float, float], tuple[float, float]]):
            if math.dist(points[1], points[2]) < threshold:
                return

            midpoints: tuple[tuple[float, float], tuple[float, float], tuple[float, float]] = (
                midpoint(points[0], points[1]),
                midpoint(points[1], points[2]),
                midpoint(points[2], points[0]),
            )

            draw.line(
                (midpoints[0], midpoints[1]),
                fill=random.choice(opts.PALETTE),
                width=self.LINE_WIDTH,
            )
            draw.line(
                (midpoints[1], midpoints[2]),
                fill=random.choice(opts.PALETTE),
                width=self.LINE_WIDTH,
            )
            draw.line(
                (midpoints[2], midpoints[0]),
                fill=random.choice(opts.PALETTE),
                width=self.LINE_WIDTH,
            )

            sierpinsify((points[0], midpoints[0], midpoints[2]))
            sierpinsify((midpoints[0], points[1],  midpoints[1]))
            sierpinsify((midpoints[2], midpoints[1],  points[2]))

        img = Image.new(
            "RGB",
            (opts.WIDTH, opts.HEIGHT),
            opts.BACKGROUND,
        )
        draw = ImageDraw.Draw(img)

        threshold = 50 * opts.SCALE
        s = min(
            opts.HEIGHT * 2 / math.sqrt(3),
            opts.WIDTH,
        ) * 0.8

        points: tuple[
            tuple[float, float],
            tuple[float, float],
            tuple[float, float]
        ] = (
            (
                (opts.WIDTH - s) / 2,
                opts.HEIGHT / 2 + s * math.sqrt(3) / 4
            ),
            (
                (opts.WIDTH + s) / 2,
                opts.HEIGHT / 2 + s * math.sqrt(3) / 4
            ),
            (
                opts.WIDTH / 2,
                opts.HEIGHT / 2 - s * math.sqrt(3) / 4
            ),
        )


        draw.line(
            (points[0], points[1]),
            fill=random.choice(opts.PALETTE),
            width=self.LINE_WIDTH,
        )
        draw.line(
            (points[1], points[2]),
            fill=random.choice(opts.PALETTE),
            width=self.LINE_WIDTH,
        )
        draw.line(
            (points[2], points[0]),
            fill=random.choice(opts.PALETTE),
            width=self.LINE_WIDTH,
        )

        sierpinsify(points)

        img.save(os.path.join(self.out_dir, self.out_base))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-o", "--output")
    args = parser.parse_args()
    Sierpinski(args.output).generate()
