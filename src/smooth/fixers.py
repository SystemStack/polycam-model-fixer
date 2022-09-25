from math import pi
from bpy import ops, context
from bmesh import from_edit_mesh
from . import log

def fill_holes():
    ops.object.mode_set(mode="EDIT")
    ops.mesh.select_all(action='SELECT')
    ops.mesh.beautify_fill(angle_limit=pi)


def remove_artifacts():
    ops.object.mode_set(mode="EDIT")
    ops.mesh.select_all(action="SELECT")
    data = context.edit_object.data
    ops.mesh.select_all(action="DESELECT")
    mesh = from_edit_mesh(data)
    mesh.verts.ensure_lookup_table()
    z_vert = max(mesh.verts, key=lambda v: v.co.z)
    mesh.verts[z_vert.index].select = True
    prev, next = 0, 1
    while prev != next:
        prev = next
        ops.mesh.select_more()
        next = len([v for v in mesh.verts if v.select])
    # select inverse
    for v in mesh.verts:
        v.select = not v.select
    ops.mesh.delete(type="VERT")
    # count selected verts


def remove_xy_plane():
    ops.object.mode_set(mode="EDIT")
    ops.mesh.select_all(action="SELECT")
    data = context.edit_object.data
    ops.mesh.select_all(action="DESELECT")
    mesh = from_edit_mesh(data)
    mesh.verts.ensure_lookup_table()
    max_z = max([min(mesh.verts, key=lambda v: v.co.x),
                 max(mesh.verts, key=lambda v: v.co.x),
                 min(mesh.verts, key=lambda v: v.co.y),
                 max(mesh.verts, key=lambda v: v.co.y)], key=lambda v: v.co.z).co.z
    for v in [vert for vert in mesh.verts if vert.co.z < max_z]:
        v.select = True
    ops.mesh.delete(type="VERT")
