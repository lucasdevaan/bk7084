import bk7084 as bk
import numpy as np
from numpy.random import randint, rand


material_stone_bricks = bk.Material()
material_stone_bricks.textures = {
    "diffuse_texture": bk.res_path("../03_textures/assets/stone_bricks_col.jpg"),
    "normal_texture": bk.res_path("../03_textures/assets/stone_bricks_nrm.png"),
    "specular_texture": bk.res_path("../03_textures/assets/stone_bricks_refl.jpg"),
    "shininess_texture": bk.res_path("../03_textures/assets/stone_bricks_gloss.jpg"),
}

material_basic_bricks = bk.Material()
material_basic_bricks.specular = bk.Color(0.1, 0.1, 0.1)
material_basic_bricks.textures = {
    "diffuse_texture": bk.res_path("../assets/brick.jpg"),
}

material_basic_concrete = bk.Material()
material_basic_concrete.specular = bk.Color(0.1, 0.1, 0.1)
material_basic_concrete.textures = {
    "diffuse_texture": bk.res_path("../assets/concrete.jpg"),
}

material_basic_floor = bk.Material()
material_basic_floor.specular = bk.Color(0.1, 0.1, 0.1)
material_basic_floor.textures = {
    "diffuse_texture": bk.res_path("../assets/brick.jpg"),
}

material_basic_window = bk.Material()
material_basic_window.textures = {
    "diffuse_texture": bk.res_path("../assets/coolwindow.png"),
}

material_basic_ground = bk.Material()
material_basic_ground.textures = {
    "diffuse_texture": bk.res_path("../assets/grass.jpg"),
}

from bk7084 import Mesh as bkMesh
import numpy as np

class BasicWall(bk.Mesh):

    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, w=1, h=1, m=material_basic_concrete):
        super().__init__()
        self.w = w
        self.h = h
        self.name = "BasicWallMesh"
        self.positions = [
            [-w / 2, -h / 2, 0],
            [w / 2, -h / 2, 0],
            [w / 2, h / 2, 0],
            [-w / 2, h / 2, 0],
        ]
        self.texcoords = [[0, 0], [1, 0], [1, 1], [0, 1]]
        self.triangles = [[0, 1, 2], [0, 2, 3]]
        self.materials = [m]

class BasicFloor(bkMesh):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, width=1, height=1, m=material_basic_concrete):
        super().__init__()

        self.w = width
        self.h = height
        self.name = "BasicFloorMesh"
        self.materials = [m]

        scale_matrix = np.diag([self.w, 1, self.h, 1])
        self.positions = [
            np.dot(scale_matrix, [-0.5, 0, -0.5, 1])[:-1],
            np.dot(scale_matrix, [0.5, 0, -0.5, 1])[:-1],
            np.dot(scale_matrix, [0.5, 0, 0.5, 1])[:-1],
            np.dot(scale_matrix, [-0.5, 0, 0.5, 1])[:-1],
        ]
        self.texcoords = [[0, 0], [1, 0], [1, 1], [0, 1]]
        self.triangles = [[0, 2, 1], [0, 3, 2]]

class BasicRoof(bkMesh):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, width=1, height=1, m=material_basic_concrete):
        super().__init__()

        self.w = width
        self.h = height
        self.name = "BasicFloorMesh"
        self.materials = [m]

        scale_matrix = np.diag([self.w, 1, self.h, 1])
        self.positions = [
            np.dot(scale_matrix, [-0.5, 0, -0.5, 1])[:-1],
            np.dot(scale_matrix, [0.5, 0, -0.5, 1])[:-1],
            np.dot(scale_matrix, [0.5, 0, 0.5, 1])[:-1],
            np.dot(scale_matrix, [-0.5, 0, 0.5, 1])[:-1],
        ]
        self.texcoords = [[0, 0], [1, 0], [1, 1], [0, 1]]
        self.triangles = [[0, 2, 1], [0, 3, 2]]

class WindowWall(bk.Mesh):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, w=1, h=1):
        super().__init__()
        self.w = w
        self.h = h
        self.name = "BasicWindowWallMesh"
        # self.materials = materials
        self.positions = [
            [-w/2, -h/2, 0.0], [w/2, -h/2, 0.0], [w/2, h/2, 0.0], [-w/2, h/2, 0.0],
            [-w*0.2, -h*0.2, 0.0], [w*0.2, -h*0.2, 0.0], [w*0.2, h*0.2, 0.0], [-w*0.2, h*0.2, 0.0],
            [-w*0.2, -h*0.2, 0.0], [w*0.2, -h*0.2, 0.0], [w*0.2, h*0.2, 0.0], [-w*0.2, h*0.2, 0.0],
        ]
        self.texcoords = [
            [0.0, 0.0], [1.0, 0.0], [1.0, 1.0], [0, 1.0],
            [0.3, 0.3], [0.7, 0.3], [0.7, 0.7], [0.3, 0.7],
            [0.0, 0.0], [1.0, 0.0], [1.0, 1.0], [0, 1.0]
        ]
        self.triangles = [
            [0, 1, 5], [0, 5, 4], [1, 2, 6], [1, 6, 5], [2, 3, 7], [2, 7, 6], [3, 0, 4], [3, 4, 7],
            [8, 9, 10], [8, 10, 11],
        ]
        self.materials = [
            material_basic_concrete,
            material_basic_window,
        ]
        self.sub_meshes = [
            bk.SubMesh(0, 8, 0),
            bk.SubMesh(8, 10, 1),
        ]
