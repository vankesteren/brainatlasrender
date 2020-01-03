import bpy
import os

filename = "test_render"
scene = bpy.data.scenes['Scene']
scene.render.filepath = os.path.join(bpy.path.abspath("//"), "output", filename)
bpy.ops.render.render( write_still=True ) 