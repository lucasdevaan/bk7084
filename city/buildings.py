import random

from bk7084.math import *
from components import *


"""
This file contains the Skyscraper, Highrise, and Office classes.
These classes are used to generate buildings with different shapes and sizes.
The Skyscraper class is already implemented for you as an example.
You will need to implement the Highrise and Office classes yourself.

A building is made up of multiple components. Each component is a mesh. For
example, a skyscraper is made up of multiple floors, walls, and windows. Each
floor, wall, and window is a component. To generate a building, we need to
generate each component and place them in the correct position. 
 
But how do we place each component in the correct position? Of course, we can
place each component manually. But what if we want to translate the whole
building? We will need to translate each component individually. This is
tedious and error-prone.

Recall what we have learned in the hierarchy lecture, how do we construct the 
solar system? We parent each planet to the sun, and moon to each planet by 
multiplying the transformation of the parent right before the transformation
of the child. This way, all the children will be transformed correctly when
the parent is transformed.
 
We can do the same thing here. We can parent each component to a base 
component and only transform the base component. This way, all the children 
will be transformed correctly when the base component is transformed. This
time, we will use the app.spawn_building() function to spawn a base component
for us. The app.spawn_building() function will spawn a base component with
nothing in it. You can then parent other components to this base component.

Check out the `self.building` variable in the Skyscraper class. It is the base
component that we will use to parent other components. Go back to the main.py
file and you will see that we apply a transformation to the self.building
component. This transformation will be applied to all the children of the
self.building component. This is how we can translate the whole building.
"""


class Skyscraper:
    """A basic skyscraper class that procedurally generates
    a skyscraper given a number of floors and width.

    Args:
        app (bk.App):
            The app instance.
        num_floors (int):
            Number of floors to generate.
        max_width (float):
            The maximum width for each component.
    """

    def __init__(self, app, num_floors, max_width):
        self.num_floors = num_floors
        # Spawn the building and save the reference to the building
        self.building = app.spawn_building()
        self.building.set_visible(True)
        for i in range(self.num_floors):
            floor1 = app.add_mesh(
                BasicFloor(max_width, max_width), parent=self.building
            )
            floor1.set_transform(Mat4.from_translation(Vec3(0, max_width * i, 0)))
            floor1.set_visible(True)
            floor2 = app.add_mesh(BasicFloor(max_width, max_width), parent=floor1)
            floor2.set_transform(Mat4.from_translation(Vec3(0, max_width, 0)))
            floor2.set_visible(True)
            wall1 = app.add_mesh(TileWindowWall(max_width, max_width), parent=floor1)
            wall1.set_transform(
                Mat4.from_translation(Vec3(0, max_width / 2, max_width / 2))
            )
            wall1.set_visible(True)
            wall2 = app.add_mesh(TileWall(max_width, max_width), parent=floor1)
            wall2.set_transform(
                Mat4.from_translation(Vec3(max_width / 2, max_width / 2, 0))
                * Mat4.from_rotation_y(90, True)
            )
            wall2.set_visible(True)
            wall3 = app.add_mesh(TileWall(max_width, max_width), parent=floor1)
            wall3.set_transform(
                Mat4.from_translation(Vec3(0, max_width / 2, -max_width / 2))
                * Mat4.from_rotation_y(180, True)
            )
            wall3.set_visible(True)
            wall4 = app.add_mesh(TileWall(max_width, max_width), parent=floor1)
            wall4.set_transform(
                Mat4.from_translation(Vec3(-max_width / 2, max_width / 2, 0))
                * Mat4.from_rotation_y(-90, True)
            )
            wall4.set_visible(True)


class Highrise:

    def __init__(self, app, num_floors, max_width):
        self.num_floors = num_floors
        # Spawn the building and save the reference to the building
        self.building = app.spawn_building()
        self.building.set_visible(True)
        for i in range(self.num_floors):
            # To place each floor higher than the previous one, we parent all
            # components to one 'base' component (floor1, see below). Then we
            # only have to move the base component up higher and the framework
            # takes care of the rest.
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
                roof = app.add_mesh(BasicFloor(max_width, max_width), parent=floor)
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
