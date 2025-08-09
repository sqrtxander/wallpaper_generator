from manim import *
import random
import util.get_options as opts


config.background_color = opts.BACKGROUND
config.pixel_width = opts.WIDTH
config.pixel_height = opts.HEIGHT


class Tree(Scene):
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

        self.add(Line(point, p, color=random.choice(opts.PALETTE)))

        self.tree_path(p, angle + self.left_angle, r * 0.75)
        self.tree_path(p, angle - self.right_angle, r * 0.75)

