from manim import *
from scipy.spatial import Delaunay as DelaunayHelper
import random
import util.get_options as opts


config.background_color = opts.BACKGROUND
config.pixel_width = opts.WIDTH
config.pixel_height = opts.HEIGHT
config.frame_width /= opts.SCALE


class FilledDelaunay(Scene):
    def construct(self):
        dot_count = int(self.camera.frame_width * self.camera.frame_height)

        points = self.get_n_random_points(dot_count)
        delaunay = DelaunayHelper([p[:2] for p in points])
        triangles = VGroup(
            Polygon(
                *(points[i] for i in triangle_points),
                fill_color=random.choice(opts.PALETTE),
                fill_opacity=1,
                color=None,
                stroke_width=2,
            )
            for triangle_points in delaunay.simplices
        )
        self.add(triangles)

    def get_n_random_points(self, n):
        return [np.around((
            (np.random.rand() - 0.5) * self.camera.frame_width,
            (np.random.rand() - 0.5) * self.camera.frame_height,
            0), 2) for _ in range(n)]

