# 6.1. Iteration in Python 2

import arcpy

# Set the work space, replace "youu_path" with your working directory
arcpy.env.workspace = "C:/youu_path/schools.gdb"

# Create a list to store buffer distances
buffer_list = [1500,2500,3500]

# Loop through buffer distance list, execute buffer analysis.
for buffer in buffer_list:
    arcpy.Buffer_analysis("sunnyside_schools", "sunnyside_schools_buffer_" + str(buffer), str(buffer) + " Feet")

print "Buffer analysis finished!"

