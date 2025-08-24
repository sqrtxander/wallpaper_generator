import random
import math
import argparse
from typing import override
from PIL import Image, ImageDraw
from util.wallpaper_generator import WallpaperGenerator


class Tree(WallpaperGenerator):
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
                width = int(self.LINE_WIDTH * self.opts.SCALE),
                fill=random.choice(self.opts.PALETTE)
            )

            tree_path(p, angle + left_angle, r * 0.75)
            tree_path(p, angle - right_angle, r * 0.75)

        img = Image.new(
            "RGB",
            (self.opts.WIDTH, self.opts.HEIGHT),
            self.opts.BACKGROUND,
        )
        draw = ImageDraw.Draw(img)
        left_angle: float = random.randint(10, 60)
        right_angle: float = random.randint(10, 60)
        initial_r = self.opts.HEIGHT // 4
        initial_p = (self.opts.WIDTH // 2, self.opts.HEIGHT * 7 // 8)
        threshold: float = self.opts.SCALE * initial_r / 20
        tree_path(initial_p, 90, initial_r)

        img.save(self.out_path)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-o", "--output", type=str, required=True)
    parser.add_argument("-c", "--config", type=str, default="config.json")
    args = parser.parse_args()
    Tree(args.output, args.config).generate()
