import sys
import importlib
sys.path.append('src')

if __name__ == "__main__":
    import smooth
    importlib.reload(smooth)
    smooth.import_test_model()  # debug
    vertices_before = len(smooth.get_readonly_object().data.vertices)
    smooth.register()
    smooth.debug_run()          # debug
    vertices_after = len(smooth.get_readonly_object().data.vertices)
    smooth.log(f"Vertices before: {vertices_before}")
    smooth.log(f"Vertices after: {vertices_after}")
    smooth.render_stills()
