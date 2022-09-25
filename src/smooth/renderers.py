import bpy
from random import random
from math import pi

from . import get_readonly_object, config


def render_stills():
    camera_collection = bpy.data.collections.new("Cameras")
    camera_collection.hide_viewport = True
    bpy.context.scene.collection.children.link(camera_collection)
    cam_data = bpy.data.cameras.new("Camera")
    cam_data.lens = 38
    cam_data.dof.focus_object = get_readonly_object()

    def render_from(name, location, rotation):
        cam = bpy.data.objects.new(f"{name}_Camera", cam_data)
        cam.location = location
        cam.rotation_euler = rotation
        camera_collection.objects.link(cam)
        bpy.context.scene.camera = cam
        bpy.context.scene.render.filepath = f"{config['RENDER_DIR']}{name}.png"
        bpy.ops.render.render(write_still=True)

    offset = random() * .01
    render_from("TOPLEFT", (-.5-offset, -.5, .5), (pi/4, 0, -pi/4))
    render_from("TOPRIGHT", (.5+offset, -.5, .5), (pi/4, 0, pi/4))

    render_from("TOP",    (0, 0, .5+offset), (0, 0, pi/2))
    render_from("BOTTOM", (0, 0, -.5-offset), (pi, 0, pi/2))

    render_from("FRONT", (0, -.75-offset, 0), (pi/2, 0, 0))
    render_from("BACK", (0, .75+offset, 0), (pi/2, 0, pi))
