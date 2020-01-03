import bpy

# remove all objects
objs = bpy.data.objects
for ob in objs:
    if (ob.type == "CAMERA"):
        continue 
    if (ob.type == "LIGHT"):
        continue
    objs.remove(ob, do_unlink = True)

# remove all materials
for material in bpy.data.materials:
    # material.user_clear()
    bpy.data.materials.remove(material)