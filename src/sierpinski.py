import random
import math
import argparse
from typing import override
from PIL import Image, ImageDraw
from util.wallpaper_generator import WallpaperGenerator


class Sierpinski(WallpaperGenerator):
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
                fill=random.choice(self.opts.PALETTE),
                width=self.LINE_WIDTH,
            )
            draw.line(
                (midpoints[1], midpoints[2]),
                fill=random.choice(self.opts.PALETTE),
                width=self.LINE_WIDTH,
            )
            draw.line(
                (midpoints[2], midpoints[0]),
                fill=random.choice(self.opts.PALETTE),
                width=self.LINE_WIDTH,
            )

            sierpinsify((points[0], midpoints[0], midpoints[2]))
            sierpinsify((midpoints[0], points[1],  midpoints[1]))
            sierpinsify((midpoints[2], midpoints[1],  points[2]))

        img = Image.new(
            "RGB",
            (self.opts.WIDTH, self.opts.HEIGHT),
            self.opts.BACKGROUND,
        )
        draw = ImageDraw.Draw(img)

        threshold = 50 * self.opts.SCALE
        s = min(
            self.opts.HEIGHT * 2 / math.sqrt(3),
            self.opts.WIDTH,
        ) * 0.8

        points: tuple[
            tuple[float, float],
            tuple[float, float],
            tuple[float, float]
        ] = (
            (
                (self.opts.WIDTH - s) / 2,
                self.opts.HEIGHT / 2 + s * math.sqrt(3) / 4
            ),
            (
                (self.opts.WIDTH + s) / 2,
                self.opts.HEIGHT / 2 + s * math.sqrt(3) / 4
            ),
            (
                self.opts.WIDTH / 2,
                self.opts.HEIGHT / 2 - s * math.sqrt(3) / 4
            ),
        )


        draw.line(
            (points[0], points[1]),
            fill=random.choice(self.opts.PALETTE),
            width=self.LINE_WIDTH,
        )
        draw.line(
            (points[1], points[2]),
            fill=random.choice(self.opts.PALETTE),
            width=self.LINE_WIDTH,
        )
        draw.line(
            (points[2], points[0]),
            fill=random.choice(self.opts.PALETTE),
            width=self.LINE_WIDTH,
        )

        sierpinsify(points)

        img.save(self.out_path)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-o", "--output", type=str, required=True)
    parser.add_argument("-c", "--config", type=str, default="config.json")
    args = parser.parse_args()
    Sierpinski(args.output, args.config).generate()
