from bk7084.math import *
from components import *

class Office:

    def __init__(self, app, max_width, grid_config):
        self.building = app.spawn_building()
        self.building.set_visible(True)
        
        for n in range(1):
            for i, row in enumerate(grid_config):
                for j, cell in enumerate(row):
                    if cell == '1':
                        floor = app.add_mesh(ConcreteFloor(max_width, max_width), parent=self.building)
                        translation = Vec3(max_width * -5 + j * max_width, max_width * n, max_width * -5 + i * max_width)
                        floor.set_transform(Mat4.from_translation(translation))
                        floor.set_visible(True)

                        for k in range(4):
                            wall = app.add_mesh(GlassWall(max_width, max_width), parent=floor)
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

                        roof = app.add_mesh(GlassRoof(max_width, max_width), parent=floor)
                        roof.set_transform(Mat4.from_translation(Vec3(0, max_width, 0)))
                        roof.set_visible(True)
        
        for n in range(2):
            for i, row in enumerate(grid_config):
                for j, cell in enumerate(row):
                    if cell == '2':
                        floor = app.add_mesh(ConcreteFloor(max_width, max_width), parent=self.building)
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

                        roof = app.add_mesh(ConcreteRoof(max_width, max_width), parent=floor)
                        roof.set_transform(Mat4.from_translation(Vec3(0, max_width, 0)))
                        roof.set_visible(True)

        for n in range(3):
            for i, row in enumerate(grid_config):
                for j, cell in enumerate(row):
                    if cell == '3':
                        floor = app.add_mesh(ConcreteFloor(max_width, max_width), parent=self.building)
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

                        roof = app.add_mesh(ConcreteRoof(max_width, max_width), parent=floor)
                        roof.set_transform(Mat4.from_translation(Vec3(0, max_width, 0)))
                        roof.set_visible(True)

class Skyscraper:

    def __init__(self, app, num_floors, max_width):
        self.num_floors = num_floors
        # Spawn the building and save the reference to the building
        self.building = app.spawn_building()
        self.building.set_visible(True)
        for i in range(self.num_floors):
            floor1 = app.add_mesh(ConcreteFloor(max_width, max_width), parent=self.building)
            floor1.set_transform(Mat4.from_translation(Vec3(0, max_width * i, 0)))
            floor1.set_visible(True)
            floor2 = app.add_mesh(ConcreteRoof(max_width, max_width), parent=floor1)
            floor2.set_transform(Mat4.from_translation(Vec3(0, max_width, 0)))
            floor2.set_visible(True)
            wall1 = app.add_mesh(WindowWall(max_width, max_width), parent=floor1)
            wall1.set_transform(Mat4.from_translation(Vec3(0, max_width / 2, max_width / 2)))
            wall1.set_visible(True)
            wall2 = app.add_mesh(ConcreteWall(max_width, max_width), parent=floor1)
            wall2.set_transform(Mat4.from_translation(Vec3(max_width / 2, max_width / 2, 0)) * Mat4.from_rotation_y(90, True))
            wall2.set_visible(True)
            wall3 = app.add_mesh(ConcreteWall(max_width, max_width), parent=floor1)
            wall3.set_transform(Mat4.from_translation(Vec3(0, max_width / 2, -max_width / 2)) * Mat4.from_rotation_y(180, True))
            wall3.set_visible(True)
            wall4 = app.add_mesh(ConcreteWall(max_width, max_width), parent=floor1)
            wall4.set_transform(Mat4.from_translation(Vec3(-max_width / 2, max_width / 2, 0)) * Mat4.from_rotation_y(-90, True))
            wall4.set_visible(True)