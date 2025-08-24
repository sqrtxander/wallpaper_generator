from scipy.spatial import Delaunay as DelaunayHelper
from typing import override
from PIL import Image, ImageDraw
import random
from util.wallpaper_generator import WallpaperGenerator
import util.get_opts as opts
import argparse

class FilledDelaunay(WallpaperGenerator):
    @override
    def generate(self):
        img = Image.new(
            "RGB",
            (opts.WIDTH, opts.HEIGHT),
            opts.BACKGROUND,
        )
        draw = ImageDraw.Draw(img)

        dot_count = int(opts.WIDTH * opts.HEIGHT / (self.SCREEN_SCALE * self.SCREEN_SCALE))
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

        img.save(self.out_path)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-o", "--output", required=True)
    args = parser.parse_args()
    FilledDelaunay(args.output).generate()

