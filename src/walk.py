from typing import override
from PIL import Image, ImageDraw
import random
from util.wallpaper_generator import WallpaperGenerator
import argparse


class Walk(WallpaperGenerator):
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
        walls: set[tuple[tuple[int, int], tuple[int, int]]] = get_walls(cols, rows)

        def point_to_coord(p: tuple[int, int]) -> tuple[int, int]:
            x, y = p
            mx, my = self.opts.WIDTH // 2, self.opts.HEIGHT // 2
            return (
                int(mx - (x - cols / 2 + 0.5) * self.SCREEN_SCALE),
                int(my - (y - rows / 2 + 0.5) * self.SCREEN_SCALE),
            )

        for p1, p2 in walls:
            draw.line(
                (point_to_coord(p1), point_to_coord(p2)),
                width=self.LINE_WIDTH,
                fill=random.choice(self.opts.PALETTE),
            )

        for x in range(cols):
            for y in range(rows):
                draw.circle(
                    point_to_coord((x, y)),
                    radius=self.CIRCLE_RADIUS,
                    fill=self.opts.FOREGROUND,
                )

        img.save(self.out_path)


def get_walls(cols: int, rows: int) -> set[tuple[tuple[int, int], tuple[int, int]]]:
    def rec(x: int, y: int) -> None:
        seen.add((x, y))
        neighbours = [(nx, ny) for nx, ny in (
            (x - 1, y),
            (x + 1, y),
            (x, y - 1),
            (x, y + 1),
        ) if 0 <= nx < cols - 1 and 0 <= ny < rows - 1 and (nx, ny) not in seen]

        random.shuffle(neighbours)
        for nx, ny in neighbours:
            if (nx, ny) in seen:
                continue

            # remove wall crossed over in the walk
            if nx == x:
                walls.remove((
                    (x, max(y, ny)),
                    (x + 1, max(y, ny))
                ))
            elif ny == y:
                walls.remove((
                    (max(x, nx), y),
                    (max(x, nx), y + 1)
                ))
            rec(nx, ny)

    # intiialse all walls as up
    walls: set[tuple[tuple[int, int], tuple[int, int]]] = set()
    for x in range(cols):
        for y in range(rows):
            if x < cols - 1:
                walls.add(((x, y), (x + 1, y)))
            if y < rows - 1:
                walls.add(((x, y), (x ,y + 1)))

    seen: set[tuple[int, int]] = set()
    rec(0, 0)

    return walls


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-o", "--output", type=str, required=True)
    parser.add_argument("-c", "--config", type=str, default="config.json")
    args = parser.parse_args()
    Walk(args.output, args.config).generate()
