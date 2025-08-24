from scipy.spatial import Delaunay as DelaunayHelper
from typing import override
from PIL import Image, ImageDraw
import random
from util.wallpaper_generator import WallpaperGenerator
import argparse


class Delaunay(WallpaperGenerator):
    @override
    def generate(self):
        img = Image.new(
            "RGB",
            (self.opts.WIDTH, self.opts.HEIGHT),
            self.opts.BACKGROUND,
        )
        draw = ImageDraw.Draw(img)

        dot_count = int(self.opts.WIDTH * self.opts.HEIGHT / (self.SCREEN_SCALE * self.SCREEN_SCALE))
        vertices: tuple[tuple[float, float], ...] = tuple(
            (random.uniform(0, self.opts.WIDTH), random.uniform(0, self.opts.HEIGHT))
            for _ in range(dot_count)
        )

        edges = create_delaunay(vertices)

        for edge in edges:
            draw.line(edge, fill=random.choice(self.opts.PALETTE), width=self.LINE_WIDTH)

        for vertex in vertices:
            draw.circle(vertex, radius=self.CIRCLE_RADIUS, fill=self.opts.FOREGROUND)

        img.save(self.out_path)

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
    parser.add_argument("-o", "--output", type=str, required=True)
    parser.add_argument("-c", "--config", type=str, default="config.json")
    args = parser.parse_args()
    Delaunay(args.output, args.config).generate()
