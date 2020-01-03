import bpy
import os
import csv

def blend_script(name):
    return(os.path.join(bpy.path.abspath("//"), "scripts", name + ".py"))

def run_script(name):
    filename = blend_script(name)
    exec(compile(open(filename).read(), filename, 'exec'))

# clean the workspace
print("Cleaning the workspace...")
run_script("clean_obj")

# import the base maps
print("Importing the DK pial atlas...")
run_script("import_obj")

# map the colours
print("Creating object materials...")
run_script("map_colours")

# Render!
print("Rendering image...")
run_script("render")