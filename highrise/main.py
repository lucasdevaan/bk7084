import bk7084 as bk
from buildings import *
from components import material_basic_ground

win = bk.Window()
win.set_title("kantoorgebouw")
win.set_size(800, 800)
win.set_resizable(False)

app = bk.App()
camera = app.create_camera(
    pos=Vec3(18, 18, 26), look_at=Vec3(0, 0, 0), fov_v=60.0, background=bk.Color.BLUE
)
camera.set_as_main_camera()

app.add_directional_light(Vec3(-1, -1, -1), bk.Color(0.8, 0.8, 0.8))


highrise = Highrise(app, 10, 3)
highrise.building.set_transform(Mat4.from_translation(Vec3(0, 0, 0)))

ground_mesh = bk.Mesh.create_quad(33, bk.Alignment.XY)
ground_mesh.set_material(material_basic_ground)
ground = app.add_mesh(ground_mesh)
ground.set_transform(Mat4.from_rotation_x(-90, True))
ground.set_visible(True)

is_key_1_pressed = False
is_key_2_pressed = False

enable_backface_culling = True
enable_wireframe = False

app.enable_backface_culling(enable_backface_culling)
app.enable_wireframe(enable_wireframe)

@app.event
def on_update(input, dt, t):
    global enable_backface_culling
    global enable_wireframe
    global is_key_1_pressed
    global is_key_2_pressed

    if input.is_key_pressed(bk.KeyCode.Key1):
        if not is_key_1_pressed:
            is_key_1_pressed = True
            enable_backface_culling = not enable_backface_culling
            app.enable_backface_culling(enable_backface_culling)
    if input.is_key_released(bk.KeyCode.Key1):
        is_key_1_pressed = False
    if input.is_key_pressed(bk.KeyCode.Key2):
        if not is_key_2_pressed:
            is_key_2_pressed = True
            enable_wireframe = not enable_wireframe
            app.enable_wireframe(enable_wireframe)
    if input.is_key_released(bk.KeyCode.Key2):
        is_key_2_pressed = False

app.run(win)
