from bpy import ops
from . import cleanup


def smooth_mesh():
    ops.object.mode_set(mode="EDIT")
    ops.mesh.select_all(action="SELECT")
    ops.mesh.remove_doubles(
        threshold=0.0001, use_sharp_edge_from_normals=True)
    ops.mesh.vertices_smooth(factor=0.5, repeat=3)
    cleanup()

    ops.mesh.select_all(action='DESELECT')


def smooth_object():
    ops.object.mode_set(mode="OBJECT")
    ops.object.select_all(action='SELECT')
    ops.object.shade_smooth()
    ops.object.select_all(action='DESELECT')


def _lossless_smooth():
    ops.object.mode_set(mode="OBJECT")
    ops.mesh.select_all(action="SELECT")
    ops.mesh.remove_doubles(
        threshold=0.0001, use_sharp_edge_from_normals=True)
    ops.mesh.select_all(action="DESELECT")
