import os
import bpy
import re

if "MESH" in [ob.type for ob in bpy.data.objects]:
    raise ValueError("Please empty your workspace before running the script")

# put the location to the folder where the objs are located here in this fashion
# this line will only work on windows ie C:\objects
this_folder  = bpy.path.abspath("//")
obj_dir      = 'pial_DK_obj'
obj_dir_path = os.path.join(this_folder, obj_dir)

# get list of all files in directory
file_list = sorted(os.listdir(obj_dir_path))

# get a list of files ending in 'obj'
obj_list = [item for item in file_list if item.endswith('.obj')]

# loop through the strings in obj_list and add the files to the scene
for item in obj_list:
    path_to_file = os.path.join(obj_dir_path, item)
    bpy.ops.import_scene.obj(filepath = path_to_file)
    
# rotate the objects because they are loaded in with a 90 degree angle
for obj in bpy.data.objects:
    if (obj.type == "CAMERA"):
        continue 
    if (obj.type == "LIGHT"):
        continue
    obj.rotation_euler[0] = 0

# set smooth shading
bpy.ops.object.select_all(action='DESELECT')
bpy.ops.object.select_by_type(type='MESH')
bpy.ops.object.shade_smooth()
bpy.ops.object.select_all(action='DESELECT')

# set the names to be more legible
trailingdigits = re.compile(r"\.\d+")
replacetext    = re.compile(r"\.pial\.DK\.")

for obj in bpy.data.objects:
    n = obj.name
    n = trailingdigits.sub("", n)
    n = replacetext.sub("-", n)
    obj.name = n
    

# remove all materials
for material in bpy.data.materials:
    # material.user_clear()
    bpy.data.materials.remove(material)