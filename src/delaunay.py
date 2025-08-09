from manim import *
from scipy.spatial import Delaunay
import random
import get_colors as colors


config.background_color = colors.BACKGROUND


class MyDelaunay(Scene):
    def construct(self):
        dot_count = int(self.camera.frame_width * self.camera.frame_height)

        dots = self.get_n_random_dots(dot_count)

        dot_coords = [dot.get_center().tolist()[:-1] for dot in dots]
        delaunay = create_delaunay(dot_coords)
        lines = VGroup(Line((x1, y1, 0), (x2, y2, 0), color=random.choice(colors.PALETTE))
                            for (x1, y1), (x2, y2) in delaunay)
        self.add(lines)
        self.add(dots)

    def get_n_random_dots(self, n):
        return VGroup(Dot(color=colors.FOREGROUND, radius=0.075).move_to(np.around((
            (np.random.rand() - 0.5) * self.camera.frame_width,
            (np.random.rand() - 0.5) * self.camera.frame_height,
            0), 2)) for _ in range(n))


def create_delaunay(points):
    points = np.array(points)
    tri = Delaunay(points)
    edges = set()

    for simplex in tri.simplices:
        for i in range(3):
            edge = tuple(
                sorted((tuple(points[simplex[i]]), tuple(points[simplex[(i+1) % 3]]))))
            edges.add(edge)

    return edges

