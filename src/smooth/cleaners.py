from bpy import ops, data


def cleanup():
    """Only idempotent actions should be performed here"""
    if (len(data.scenes[0].objects) == 0):
        return

    # The context override is needed so it's possible to set edit-mode.
    ops.object.mode_set(mode='EDIT')

    _remove_orphans()
    ops.object.mode_set(mode="EDIT")
    ops.mesh.select_all(action="SELECT")
    ops.mesh.delete_loose(use_faces=True)
    _remove_orphans()


def _remove_orphans():
    ops.outliner.orphans_purge(
        do_local_ids=True, do_linked_ids=True, do_recursive=True)
    ops.outliner.orphans_purge(
        do_local_ids=True, do_linked_ids=False, do_recursive=True)
    ops.outliner.orphans_purge(
        do_local_ids=False, do_linked_ids=True, do_recursive=True)
