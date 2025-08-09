from manim import *
import random
import util.get_options as opts


config.background_color = opts.BACKGROUND
config.pixel_width = opts.WIDTH
config.pixel_height = opts.HEIGHT
config.frame_width /= opts.SCALE


class Tree(Scene):
    def construct(self):
        self.left_angle = random.randint(10, 60) * DEGREES
        self.right_angle = random.randint(10, 60) * DEGREES
        self.initial_r = self.camera.frame_height // 4
        self.threshold = self.initial_r / 20
        self.tree_path(ORIGIN - np.array([0, self.camera.frame_height * 3 / 8, 0]), 90 * DEGREES, self.initial_r)


    def tree_path(self, point, angle, r):
        if r < self.threshold:
            return

        p = np.array([
            point[0] + r * np.cos(angle),
            point[1] + r * np.sin(angle),
            0,
        ])

        self.add(Line(point, p, color=random.choice(opts.PALETTE)))

        self.tree_path(p, angle + self.left_angle, r * 0.75)
        self.tree_path(p, angle - self.right_angle, r * 0.75)

