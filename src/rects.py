from typing import override
from PIL import Image, ImageDraw
import random
from util.wallpaper_generator import WallpaperGenerator
import argparse


class Rects(WallpaperGenerator):
    @override
    def generate(self):
        img = Image.new(
            "RGB",
            (self.opts.WIDTH, self.opts.HEIGHT),
            self.opts.BACKGROUND,
        )
        draw = ImageDraw.Draw(img)
        # can't use integer division because SCREEN_SCALE can be a float
        rows = int(self.opts.HEIGHT / self.SCREEN_SCALE)
        cols = int(self.opts.WIDTH / self.SCREEN_SCALE)

        def point_to_coord(p: tuple[int, int]) -> tuple[int, int]:
            x, y = p
            mx, my = self.opts.WIDTH / 2, self.opts.HEIGHT / 2
            return (
                int(mx + (x - cols / 2) * self.SCREEN_SCALE),
                int(my + (y - rows / 2) * self.SCREEN_SCALE),
            )

        rects = get_rects(cols, rows, 0, 1, 6)

        for p1, p2 in rects:
            draw.rectangle(
                (point_to_coord(p1), point_to_coord(p2)),
                outline=self.opts.BACKGROUND,
                width=self.LINE_WIDTH,
                fill=random.choice(self.opts.PALETTE),
            )

        img.save(self.out_path)


def get_rects(cols: int, rows: int, holes: int, min_area: int, max_area: int) -> set[tuple[tuple[int, int], tuple[int, int]]]:
    def split(x1: int, y1: int, x2: int, y2: int) -> set[tuple[tuple[int, int], tuple[int, int]]]:
        height = y2 - y1
        width = x2 - x1
        if width * height <= min_area:
            return set((((x1, y1), (x2, y2)),))

        if width * height <= max_area and random.random() < 0.25:
            return set((((x1, y1), (x2, y2)),))

        horizontal = random.random() < 0.5

        if horizontal:
            y_split = random.randint(y1, y2)
            return split(x1, y1, x2, y_split) | split(x1, y_split, x2, y2)
        else:
            x_split = random.randint(x1, x2)
            return split(x1, y1, x_split, y2) | split(x_split, y1, x2, y2)

    min_area = min(min_area, rows * cols)
    max_area = min(max_area, rows * cols)
    rects: set[tuple[tuple[int, int], tuple[int, int]]] = split(0, 0, cols, rows)
    for _ in range(holes):
        rects.pop()
    return rects

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-o", "--output", type=str, required=True)
    parser.add_argument("-c", "--config", type=str, default="config.json")
    args = parser.parse_args()
    Rects(args.output, args.config).generate()
