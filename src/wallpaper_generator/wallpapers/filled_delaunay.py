import random
from PIL import Image, ImageDraw
from typing import override
from wallpaper_generator import WallpaperGenerator, generate_wallpaper
from scipy.spatial import Delaunay as DelaunayHelper


class FilledDelaunay(WallpaperGenerator):
    @override
    def generate(self):
        img = Image.new(
            "RGB",
            (self.opts.WIDTH, self.opts.HEIGHT),
            self.opts.BACKGROUND,
        )
        draw = ImageDraw.Draw(img)

        dot_count = int(
            self.opts.WIDTH * self.opts.HEIGHT / (self.SCREEN_SCALE * self.SCREEN_SCALE)
        )
        vertices: tuple[tuple[float, float], ...] = tuple(
            (random.uniform(0, self.opts.WIDTH), random.uniform(0, self.opts.HEIGHT))
            for _ in range(dot_count)
        )
        edge_pairs = DelaunayHelper(vertices)

        for edge_pair in edge_pairs.simplices:
            draw.polygon(
                tuple(vertices[i] for i in edge_pair),
                outline=self.opts.BACKGROUND,
                width=self.LINE_WIDTH // 2,
                fill=random.choice(self.opts.PALETTE),
            )

        img.save(self.out_path)


if __name__ == "__main__":
    generate_wallpaper(FilledDelaunay)
