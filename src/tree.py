from manim import *
import random

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
class MyTree(Scene):
    def construct(self):
        self.left_angle = random.randint(10, 60) * DEGREES
        self.right_angle = random.randint(10, 60) * DEGREES
        self.initial_r = self.camera.frame_width // 4 - 1
        self.tree_path(self.camera.frame_height / 2 * DOWN + UP, 90 * DEGREES, self.initial_r)


    def tree_path(self, point, angle, r):
        if r < 0.1:
            return

        p = np.array([
            point[0] + r * np.cos(angle),
            point[1] + r * np.sin(angle),
            0,
        ])

        self.add(Line(point, p, color=random.choice(CYBERDREAM)))

        self.tree_path(p, angle + self.left_angle, r * 0.75)
        self.tree_path(p, angle - self.right_angle, r * 0.75)

