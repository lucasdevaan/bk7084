import bk7084 as bk
import numpy as np
from numpy.random import randint, rand

material_green_tiles = bk.Material()
material_green_tiles.specular = bk.Color(0.1, 0.1, 0.1)
material_green_tiles.textures = {
    "diffuse_texture": bk.res_path("./assets/tegeltjes.jpg"),
}

material_basic_floor = bk.Material()
material_basic_floor.diffuse = bk.Color(0.8, 0.5, 0.5)

material_basic_window = bk.Material()
material_basic_window.textures = {
    "diffuse_texture": bk.res_path("./assets/raam_hout.png"),
}

material_concrete_wall = bk.Material()
material_concrete_wall.textures = {
    "diffuse_texture": bk.res_path("./assets/concrete_wall_diffuse.jpg"),
    "normal_texture": bk.res_path("./assets/concrete_wall_normal.jpg"),
    "specular_texture": bk.res_path("./assets/stone_bricks_refl.jpg"),
    "shininess_texture": bk.res_path("./assets/stone_bricks_gloss.jpg"),
}

material_concrete_roof = bk.Material()
material_concrete_roof.textures = {
    "diffuse_texture": bk.res_path("./assets/concrete_roof_diffuse.jpg"),
    "normal_texture": bk.res_path("./assets/concrete_roof_normal.jpg"),
    "specular_texture": bk.res_path("./assets/stone_bricks_refl.jpg"),
    "shininess_texture": bk.res_path("./assets/stone_bricks_gloss.jpg"),
}

material_glass_wall = bk.Material()
material_glass_wall.textures = {
    "diffuse_texture": bk.res_path("./assets/glass_wall_diffuse.jpg"),
    "normal_texture": bk.res_path("./assets/glass_wall_normal.jpg"),
}

material_round_window = bk.Material()
material_round_window.textures = {
    "diffuse_texture": bk.res_path("./assets/round_window_diffuse.png"),
    "normal_texture": bk.res_path("./assets/round_window_normal.png"),
    "specular_texture": bk.res_path("./assets/stone_bricks_refl.jpg"),
    "shininess_texture": bk.res_path("./assets/stone_bricks_gloss.jpg"),
}

material_basic_ground = bk.Material()
material_basic_ground.textures = {
    "diffuse_texture": bk.res_path("./assets/grass.jpg"),
    "specular_texture": bk.res_path("./assets/stone_bricks_refl.jpg"),
    "shininess_texture": bk.res_path("./assets/stone_bricks_gloss.jpg"),
}

material_yellow_wall = bk.Material()
material_yellow_wall.textures = {
    "diffuse_texture": bk.res_path("./assets/gele_latten.jpg"),
}

material_concrete_blue = bk.Material()
material_concrete_blue.textures = {
    "diffuse_texture": bk.res_path("./assets/blue_wall.jpg"),
}

material_rood_raam = bk.Material()
material_rood_raam.textures = {
    "diffuse_texture": bk.res_path("./assets/rood_raam.jpg"),
}

material_dakpannen = bk.Material()
material_dakpannen.textures = {
    "diffuse_texture": bk.res_path("./assets/dakpannen.jpg"),
}


class ConcreteWall(bk.Mesh):

    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, width=1, height=1, m=material_concrete_wall):
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

class ConcreteFloor(bk.Mesh):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, width=1, height=1, m=material_concrete_wall):
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

class ConcreteRoof(bk.Mesh):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, width=1, height=1, m=material_concrete_roof):
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

class GlassWall(bk.Mesh):

    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, w=1, h=1, m=material_glass_wall):
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

class GlassRoof(bk.Mesh):
    
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, width=1, height=1, m=material_glass_wall):
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
            material_concrete_wall,
            material_round_window,
        ]
        self.sub_meshes = [
            bk.SubMesh(0, 8, 0),
            bk.SubMesh(8, 10, 1),
        ]

class TileWall(bk.Mesh):

    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, w=1, h=1, m=material_green_tiles):
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


class BasicFloor(bk.Mesh):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, w=1, h=1, m=material_basic_floor):
        super().__init__()
        self.w = w
        self.h = h
        self.name = "BasicFloorMesh"
        # self.materials = materials
        self.positions = [
            [-w / 2, 0, -h / 2],
            [w / 2, 0, -h / 2],
            [w / 2, 0, h / 2],
            [-w / 2, 0, h / 2],
        ]
        self.texcoords = [[0, 0], [1, 0], [1, 1], [0, 1]]
        self.triangles = [[0, 2, 1], [0, 3, 2]]
        self.materials = [m]


class TileWindowWall(bk.Mesh):
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
            material_green_tiles,
            material_basic_window,
        ]
        self.sub_meshes = [
            bk.SubMesh(0, 8, 0),
            bk.SubMesh(8, 10, 1),
        ]

class YellowWall(bk.Mesh):

    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, w=0.5, h=0.5, m=material_yellow_wall):
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

class YellowWindowWall(bk.Mesh):
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
            material_yellow_wall,
            material_rood_raam,
        ]
        self.sub_meshes = [
            bk.SubMesh(0, 8, 0),
            bk.SubMesh(8, 10, 1),
        ]

class BlueWall(bk.Mesh):

    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, w=0.5, h=0.5, m=material_concrete_blue):
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

class BlueWindowWall(bk.Mesh):
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
            material_concrete_blue,
            material_rood_raam,
        ]
        self.sub_meshes = [
            bk.SubMesh(0, 8, 0),
            bk.SubMesh(8, 10, 1),
        ]

class GreenRoof(bk.Mesh):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, w=1, h=1, m=material_basic_ground):
        super().__init__()
        self.w = w
        self.h = h
        self.name = "BasicFloorMesh"
        # self.materials = materials
        self.positions = [
            [-w / 2, 0, -h / 2],
            [w / 2, 0, -h / 2],
            [w / 2, 0, h / 2],
            [-w / 2, 0, h / 2],
        ]
        self.texcoords = [[0, 0], [1, 0], [1, 1], [0, 1]]
        self.triangles = [[0, 2, 1], [0, 3, 2]]
        self.materials = [m]

class Dakpannen(bk.Mesh):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, w=1, h=1, m=material_dakpannen):
        super().__init__()
        self.w = w
        self.h = h
        self.name = "BasicFloorMesh"
        # self.materials = materials
        self.positions = [
            [-w / 2, 0, -h / 2],
            [w / 2, 0, -h / 2],
            [w / 2, 0, h / 2],
            [-w / 2, 0, h / 2],
        ]
        self.texcoords = [[0, 0], [1, 0], [1, 1], [0, 1]]
        self.triangles = [[0, 2, 1], [0, 3, 2]]
        self.materials = [m]