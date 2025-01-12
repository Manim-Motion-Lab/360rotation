from manim import *

class RotationUpdater(Scene):
    def construct(self):
        def updater_forth(mobj, dt):
            mobj.rotate_about_origin(dt)
        def updater_back(mobj, dt):
            mobj.rotate_about_origin(-dt)
        line_reference = Line(ORIGIN, LEFT).set_color(BLUE)
        line_moving = Line(ORIGIN, LEFT).set_color(RED)
        line_moving.add_updater(updater_forth)
        self.add(line_reference, line_moving)
        self.wait(6.3)
        line_moving.remove_updater(updater_forth)
        line_moving.add_updater(updater_back)
        self.wait(6.3)
        line_moving.remove_updater(updater_back)
        self.wait(0.5)