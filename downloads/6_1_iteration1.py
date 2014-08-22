# 6.1. Iteration in Python 1

import arcpy

# Set the work space, replace "your_path" with your working directory
arcpy.env.workspace = "C:/your_path/schools.gdb"

# Use the ListFeatureClasses function
# to return a list of feature classes under workspace
# whose name start with "schools".
fc_list = arcpy.ListFeatureClasses("schools*")

# Loop through feature class list, execute buffer analysis.
for fc in fc_list:
	arcpy.Buffer_analysis(fc, fc + "_buffer_800", "800 Feet")

print "Buffer analysis finished!"

