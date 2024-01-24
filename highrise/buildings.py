from bk7084.math import *
from components import *

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