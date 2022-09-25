from bpy import ops, types, utils, ops
from . import cleanup, remove_xy_plane, smooth_mesh, smooth_object, remove_artifacts, fill_holes


def menu_func(self, context):
    self.layout.operator(SmoothOperator.bl_idname,
                         text=SmoothOperator.bl_label)


def register():
    utils.register_class(SmoothOperator)
    types.VIEW3D_MT_edit_mesh_context_menu.append(menu_func)


def unregister():
    utils.unregister_class(SmoothOperator)
    types.VIEW3D_MT_edit_mesh_context_menu.remove(menu_func)


debug_run = ops.object.smooth_model


class SmoothOperator(types.Operator):
    """Smooths the selected mesh"""
    bl_idname = "object.smooth_model"
    bl_label = "Smooth AR Model"

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        cleanup()
        remove_xy_plane()
        smooth_mesh()
        remove_artifacts()
        fill_holes()
        smooth_object()
        cleanup()
        unregister()  # debug
        return {"FINISHED"}
