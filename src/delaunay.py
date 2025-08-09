from manim import *
import random
from scipy.spatial import Delaunay

CYBERDREAM = (
    # RGBA.from_hex("#16181a"),
    # RGBA.from_hex("#1e2124"),
    # RGBA.from_hex("#3c4048"),
    # RGBA.from_hex("#ffffff"),
    # RGBA.from_hex("#7b8496"),
    RGBA.from_hex("#5ea1ff"),
    RGBA.from_hex("#5eff6c"),
    RGBA.from_hex("#5ef1ff"),
    RGBA.from_hex("#ff6e5e"),
    RGBA.from_hex("#f1ff5e"),
    RGBA.from_hex("#ff5ef1"),
    RGBA.from_hex("#ff5ea0"),
    RGBA.from_hex("#ffbd5e"),
    RGBA.from_hex("#bd5eff"),
)
class MyDelaunay(Scene):
    def construct(self):
        dot_count = int(self.camera.frame_width * self.camera.frame_height)

        dots = self.get_n_random_dots(dot_count)

        dot_coords = [dot.get_center().tolist()[:-1] for dot in dots]
        delaunay = create_delaunay(dot_coords)
        lines = VGroup(Line((x1, y1, 0), (x2, y2, 0), color=random.choice(CYBERDREAM))
                            for (x1, y1), (x2, y2) in delaunay)
        self.add(lines)
        self.add(dots)

    def get_n_random_dots(self, n):
        return VGroup(Dot(color=WHITE, radius=0.075).move_to(np.around((
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

