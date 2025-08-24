from scipy.spatial import Delaunay as DelaunayHelper
from typing import override
import os
from PIL import Image, ImageDraw
import random
from util.wallpaper_generator import WallpaperGenerator
import util.get_opts as opts
import argparse


class Delaunay(WallpaperGenerator):
    def __init__(self, base: str):
        super().__init__()
        self.out_base: str = base or "delaunay.png"

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

        edges = create_delaunay(vertices)

        for edge in edges:
            draw.line(edge, fill=random.choice(opts.PALETTE), width=self.LINE_WIDTH)

        for vertex in vertices:
            draw.circle(vertex, radius=self.CIRCLE_RADIUS, fill=opts.FOREGROUND)

        img.save(os.path.join(self.out_dir, self.out_base))

def create_delaunay(points: tuple[tuple[float, float], ...]) -> set[tuple[tuple[float, float], tuple[float, float]]]:
    tri = DelaunayHelper(points)
    edges: set[tuple[tuple[float, float], tuple[float, float]]] = set()

    for simplex in tri.simplices:
        for i in range(3):
            edge = tuple(sorted((tuple(points[simplex[i]]), tuple(points[simplex[(i+1) % 3]]))))
            edges.add(edge)

    return edges


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-o", "--output")
    args = parser.parse_args()
    Delaunay(args.output).generate()
