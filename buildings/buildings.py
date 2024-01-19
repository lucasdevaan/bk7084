from bk7084.math import *
from components import *

from bk7084.math import *
from components import *

class Building:

    def __init__(self, app, max_width, grid_config):
        self.building = app.spawn_building()
        self.building.set_visible(True)
        
        for n in range(1):
            for i, row in enumerate(grid_config):
                for j, cell in enumerate(row):
                    if cell == '1':
                        floor = app.add_mesh(BasicFloor(max_width, max_width), parent=self.building)
                        translation = Vec3(max_width * -5 + j * max_width, max_width * n, max_width * -5 + i * max_width)
                        floor.set_transform(Mat4.from_translation(translation))
                        floor.set_visible(True)

                        for k in range(4):
                            wall = app.add_mesh(BasicWall(max_width, max_width), parent=floor)
                            rotation_angle = k * 90

                            if k == 0:
                                translation = Vec3(0, max_width / 2, max_width / 2)
                            elif k == 1:
                                translation = Vec3(max_width / 2, max_width / 2, 0)
                            elif k == 2:
                                translation = Vec3(0, max_width / 2, -max_width / 2)
                            else:
                                translation = Vec3(-max_width / 2, max_width / 2, 0)

                            wall.set_transform(Mat4.from_translation(translation) * Mat4.from_rotation_y(rotation_angle, True))
                            wall.set_visible(True)

                        roof = app.add_mesh(BasicRoof(max_width, max_width), parent=floor)
                        roof.set_transform(Mat4.from_translation(Vec3(0, max_width, 0)))
                        roof.set_visible(True)
        
        for n in range(2):
            for i, row in enumerate(grid_config):
                for j, cell in enumerate(row):
                    if cell == '2':
                        floor = app.add_mesh(BasicFloor(max_width, max_width), parent=self.building)
                        translation = Vec3(max_width * -5 + j * max_width, max_width * n, max_width * -5 + i * max_width)
                        floor.set_transform(Mat4.from_translation(translation))
                        floor.set_visible(True)

                        for k in range(4):
                            wall = app.add_mesh(BasicWall(max_width, max_width), parent=floor)
                            rotation_angle = k * 90

                            if k == 0:
                                translation = Vec3(0, max_width / 2, max_width / 2)
                            elif k == 1:
                                translation = Vec3(max_width / 2, max_width / 2, 0)
                            elif k == 2:
                                translation = Vec3(0, max_width / 2, -max_width / 2)
                            else:
                                translation = Vec3(-max_width / 2, max_width / 2, 0)

                            wall.set_transform(Mat4.from_translation(translation) * Mat4.from_rotation_y(rotation_angle, True))
                            wall.set_visible(True)

                        roof = app.add_mesh(BasicRoof(max_width, max_width), parent=floor)
                        roof.set_transform(Mat4.from_translation(Vec3(0, max_width, 0)))
                        roof.set_visible(True)

        for n in range(3):
            for i, row in enumerate(grid_config):
                for j, cell in enumerate(row):
                    if cell == '3':
                        floor = app.add_mesh(BasicFloor(max_width, max_width), parent=self.building)
                        translation = Vec3(max_width * -5 + j * max_width, max_width * n, max_width * -5 + i * max_width)
                        floor.set_transform(Mat4.from_translation(translation))
                        floor.set_visible(True)

                        for k in range(4):
                            wall = app.add_mesh(WindowWall(max_width, max_width), parent=floor)
                            rotation_angle = k * 90

                            if k == 0:
                                translation = Vec3(0, max_width / 2, max_width / 2)
                            elif k == 1:
                                translation = Vec3(max_width / 2, max_width / 2, 0)
                            elif k == 2:
                                translation = Vec3(0, max_width / 2, -max_width / 2)
                            else:
                                translation = Vec3(-max_width / 2, max_width / 2, 0)

                            wall.set_transform(Mat4.from_translation(translation) * Mat4.from_rotation_y(rotation_angle, True))
                            wall.set_visible(True)

                        roof = app.add_mesh(BasicRoof(max_width, max_width), parent=floor)
                        roof.set_transform(Mat4.from_translation(Vec3(0, max_width, 0)))
                        roof.set_visible(True)