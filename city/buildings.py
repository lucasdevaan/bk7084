import math
import random

from bk7084.math import *
from components import *

class Skyscraper:

    def __init__(self, app, num_floors, max_width):
        self.num_floors = num_floors
        # Spawn the building and save the reference to the building
        self.building = app.spawn_building()
        self.building.set_visible(True)
        for i in range(self.num_floors):
            angle = i + 2 * math.pi / 4
            height = max_width * i
            floor1 = app.add_mesh(GreenRoof(max_width, max_width), parent=self.building)

            floor1.set_transform(Mat4.from_translation(Vec3(max_width * math.cos(angle), height, max_width * math.sin(angle))) * Mat4.from_rotation_y(angle, True))
            floor1.set_visible(True)
          
            floor2 = app.add_mesh(GreenRoof(max_width, max_width), parent=floor1)
            floor2.set_transform(Mat4.from_translation(Vec3(0, max_width, 0)))
            floor2.set_visible(True)

            floor3 = app.add_mesh(GreenRoof(max_width, max_width), parent=self.building)
            # Place the base component higher each time (i)
            floor3.set_transform(Mat4.from_translation(Vec3(0, max_width * i, 0)))
            floor3.set_visible(True)

            floor4 = app.add_mesh(GreenRoof(max_width, max_width), parent=floor3)
            floor4.set_transform(Mat4.from_translation(Vec3(0, max_width, 0)))
            floor4.set_visible(True)
           
           
            
            def add_walls_to_floor(floor):
                wall1 = app.add_mesh(YellowWindowWall(max_width, max_width), parent=floor)
                wall1.set_transform(Mat4.from_translation(Vec3(0, max_width / 2, max_width / 2)))
                wall1.set_visible(True)
            
                wall2 = app.add_mesh(YellowWall(max_width, max_width), parent=floor)
                wall2.set_transform(Mat4.from_translation(Vec3(max_width / 2, max_width / 2, 0)) * Mat4.from_rotation_y(90, True))
                wall2.set_visible(True)
            
                wall3 = app.add_mesh(YellowWindowWall(max_width, max_width), parent=floor)
                wall3.set_transform(Mat4.from_translation(Vec3(0, max_width / 2, -max_width / 2)) * Mat4.from_rotation_y(180, True))
                wall3.set_visible(True)
            
                wall4 = app.add_mesh(YellowWall(max_width, max_width), parent=floor)
                wall4.set_transform(Mat4.from_translation(Vec3(-max_width / 2, max_width / 2, 0)) * Mat4.from_rotation_y(-90, True))
                wall4.set_visible(True)

            floors = [floor3]
            
            for floor in floors:
                add_walls_to_floor(floor)

            wall1 = app.add_mesh(BlueWindowWall(max_width, max_width), parent=floor1)
            wall1.set_transform(Mat4.from_translation(Vec3(0, max_width / 2, max_width / 2)))
            wall1.set_visible(True)
           
            wall2 = app.add_mesh(BlueWall(max_width, max_width), parent=floor1)
            wall2.set_transform(Mat4.from_translation(Vec3(max_width / 2, max_width / 2, 0)) * Mat4.from_rotation_y(90, True))
            wall2.set_visible(True)
            
            wall3 = app.add_mesh(BlueWindowWall(max_width, max_width), parent=floor1)
            wall3.set_transform(Mat4.from_translation(Vec3(0, max_width / 2, -max_width / 2)) * Mat4.from_rotation_y(180, True))
            wall3.set_visible(True)
            
            wall4 = app.add_mesh(BlueWall(max_width, max_width), parent=floor1)
            wall4.set_transform(Mat4.from_translation(Vec3(-max_width / 2, max_width / 2, 0)) * Mat4.from_rotation_y(-90, True))
            wall4.set_visible(True)

class Highrise:

    def __init__(self, app, num_floors, max_width):
        self.num_floors = num_floors
        # Spawn the building and save the reference to the building
        self.building = app.spawn_building()
        self.building.set_visible(True)
        for i in range(self.num_floors):
            floor1 = app.add_mesh(BasicFloor(max_width, max_width), parent=self.building)
            # Place the base component higher each time (i)
            floor1.set_transform(Mat4.from_translation(Vec3(0, max_width * i, 0)))
            floor1.set_visible(True)
     
     # toren A
        #toren A1       

            floor2 = app.add_mesh(BasicFloor(max_width, max_width), parent=floor1)
            floor2.set_transform(Mat4.from_translation(Vec3(2, max_width * 3, 2)))
            floor2.set_visible(True)


        #toren A2    
            floor3 = app.add_mesh(BasicFloor(max_width, max_width), parent=floor2)
            floor3.set_transform(Mat4.from_translation(Vec3(2, max_width, 2)))
            floor3.set_visible(True)


    # toren C
        #toren C1       
            floor2c = app.add_mesh(BasicFloor(max_width, max_width), parent=floor1)
            floor2c.set_transform(Mat4.from_translation(Vec3(-2, max_width * 2, 2)))
            floor2c.set_visible(True)

            
        #toren C2    
            floor3c = app.add_mesh(BasicFloor(max_width, max_width), parent=floor2c)
            floor3c.set_transform(Mat4.from_translation(Vec3(-2, max_width, 2)))
            floor3c.set_visible(True)

            
    # toren B
        #toren B1
            floor2b = app.add_mesh(BasicFloor(max_width, max_width), parent=floor1)
            floor2b.set_transform(Mat4.from_translation(Vec3(-2, max_width, -2)))
            floor2b.set_visible(True)
    

        #toren B2    
            floor3b = app.add_mesh(BasicFloor(max_width, max_width), parent=floor2b)
            floor3b.set_transform(Mat4.from_translation(Vec3(-2, max_width, -2)))
            floor3b.set_visible(True)  

    # toren D
        #toren D1
            floor2d = app.add_mesh(BasicFloor(max_width, max_width), parent=floor1)
            floor2d.set_transform(Mat4.from_translation(Vec3(2, max_width * 4, -2)))
            floor2d.set_visible(True)

           
        #toren D2    
            floor3d = app.add_mesh(BasicFloor(max_width, max_width), parent=floor2d)
            floor3d.set_transform(Mat4.from_translation(Vec3(2, max_width, -2)))
            floor3d.set_visible(True)

            
            def add_roof_to_floor(floor):
                roof = app.add_mesh(Dakpannen(max_width, max_width), parent=floor)
                roof.set_transform(Mat4.from_translation(Vec3(0, max_width, 0)))
                roof.set_visible(True)

            floors = [floor2, floor2b, floor2c, floor2d, floor3, floor3b, floor3c, floor3d]
            
            for floor in floors:
                add_roof_to_floor(floor)

           
            def add_walls_to_floor(floor):
                wall1 = app.add_mesh(TileWindowWall(max_width, max_width), parent=floor)
                wall1.set_transform(Mat4.from_translation(Vec3(0, max_width / 2, max_width / 2)))
                wall1.set_visible(True)
            
                wall2 = app.add_mesh(TileWall(max_width, max_width), parent=floor)
                wall2.set_transform(Mat4.from_translation(Vec3(max_width / 2, max_width / 2, 0)) * Mat4.from_rotation_y(90, True))
                wall2.set_visible(True)
            
                wall3 = app.add_mesh(TileWindowWall(max_width, max_width), parent=floor)
                wall3.set_transform(Mat4.from_translation(Vec3(0, max_width / 2, -max_width / 2)) * Mat4.from_rotation_y(180, True))
                wall3.set_visible(True)
           
                wall4 = app.add_mesh(TileWall(max_width, max_width), parent=floor)
                wall4.set_transform(Mat4.from_translation(Vec3(-max_width / 2, max_width / 2, 0)) * Mat4.from_rotation_y(-90, True))
                wall4.set_visible(True)

            floors = [floor1, floor2, floor2b, floor2c, floor2d, floor3, floor3b, floor3c, floor3d]
            
            for floor in floors:
                add_walls_to_floor(floor)

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


# pre-loaded park model
park_model = bk.Mesh.load_from(bk.res_path("./assets/park.obj"))


class Park:
    def __init__(self, app):
        self.building = app.add_mesh(park_model)
        self.building.set_visible(True)
        angle = random.randint(0, 3) * 90
        self.pre_transform = (
            Mat4.from_translation(Vec3(0, 1.4, 0))
            * Mat4.from_scale(Vec3(0.5))
            * Mat4.from_rotation_y(angle, True)
        )


# pre-loaded house model
house_model = bk.Mesh.load_from(bk.res_path("./assets/house.obj"))


class House:
    def __init__(self, app):
        self.building = app.add_mesh(house_model)
        self.building.set_visible(True)
        angle = random.randint(0, 3) * 90
        self.pre_transform = (
            Mat4.from_scale(Vec3(0.5))
            * Mat4.from_translation(Vec3(0, 6.8, 0))
            * Mat4.from_rotation_y(angle, True)
        )