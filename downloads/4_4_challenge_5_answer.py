# 4.4. Geoprocessing in IDLE - Challenge 5

import arcpy

# Replace "your_path" with the path where you save the geodatabase
arcpy.env.workspace = "c:/your_path/schools.gdb"

# Create buffers around schools
arcpy.Clip_analysis("denver_schools","highland","highland_schools","#")

print "Clip processing finished!"
