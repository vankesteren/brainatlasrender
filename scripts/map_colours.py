import bpy
import os
import csv

this_folder = bpy.path.abspath("//")
file_name   = "factors.csv"

file_path = os.path.join(this_folder, file_name)

print(file_path)

# generate a dataset
dataset = []
with open(file_path, "r") as csvfile:
    rowreader = csv.reader(csvfile, delimiter = ",", quotechar = "\"")
    header = True
    names  = []
    for row in rowreader:
        if (header):
            # extract the header
            names    = row
            names[0] = "name"
            header   = False
            continue
        rowdict = {}
        for i in range(len(names)):
            rowdict[names[i]] = row[i]
        # create dictionary for each row with name and attributes
        dataset.append(rowdict)
        

print("removing materials")
# remove all materials
for material in bpy.data.materials:
    # material.user_clear()
    bpy.data.materials.remove(material)

print("creating materials")
bpy.ops.object.select_all(action='DESELECT')
# create new materials
for row in dataset:
    name          = row.get("name")
    obj           = bpy.data.objects[name]
    # if (int(row.get("hide", 0)) == 1):
    #     bpy.ops.object.select_pattern(pattern = name)
    #     bpy.ops.object.hide_view_set(unselected=False)
    #     bpy.ops.object.select_all(action='DESELECT')
    #     continue
    mat           = bpy.data.materials.new(name)
    mat.use_nodes = True
    bsdf          = mat.node_tree.nodes["Principled BSDF"]
    # input rgba values with suitable defaults
    bsdf.inputs[0].default_value = (float(row.get("red", 0.5)), 
                                    float(row.get("green", 0.5)), 
                                    float(row.get("blue", 0.5)), 
                                    float(row.get("alpha", 1.0)))
    obj.data.materials[0] = mat