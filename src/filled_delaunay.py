from scipy.spatial import Delaunay as DelaunayHelper
from typing import override
import os
from PIL import Image, ImageDraw
import random
from util.wallpaper_generator import WallpaperGenerator
import util.get_opts as opts
import argparse

class FilledDelaunay(WallpaperGenerator):
    def __init__(self, base: str):
        super().__init__()
        self.out_base: str = base or "filled_delaunay.png"

    @override
    def generate(self):
        img = Image.new(
            "RGB",
            (opts.WIDTH, opts.HEIGHT),
            opts.BACKGROUND,
        )
        draw = ImageDraw.Draw(img)

        scale = 150 * opts.SCALE

        dot_count = int(opts.WIDTH * opts.HEIGHT / (scale * scale))
        vertices: tuple[tuple[float, float], ...] = tuple(
            (random.uniform(0, opts.WIDTH), random.uniform(0, opts.HEIGHT))
            for _ in range(dot_count)
        )
        edge_pairs = DelaunayHelper(vertices)

        for edge_pair in edge_pairs.simplices:
            draw.polygon(
                tuple(vertices[i] for i in edge_pair),
                outline=opts.BACKGROUND,
                width=self.LINE_WIDTH // 2,
                fill=random.choice(opts.PALETTE),
            )

        img.save(os.path.join(self.out_dir, self.out_base))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-o", "--output")
    args = parser.parse_args()
    FilledDelaunay(args.output).generate()

