from bpy import ops, context, data
from . import cleanup, config


def get_readonly_object():
    ops.object.mode_set(mode="OBJECT")
    return context.object


def get_editable_mesh():
    ops.object.mode_set(mode="EDIT")
    ops.mesh.select_all(action="SELECT")
    data = context.edit_object.data
    ops.mesh.select_all(action="DESELECT")
    return data


def import_test_model():
    _clear_scene()
    ops.import_scene.gltf(filepath=config['IMPORT_MODEL'])


def _clear_scene():
    cleanup()
    for obj in data.objects:
        data.objects.remove(obj)
    for coll in data.collections:
        data.collections.remove(coll)
