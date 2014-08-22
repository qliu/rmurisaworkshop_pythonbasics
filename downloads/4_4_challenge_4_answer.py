# 4.4. Geoprocessing in IDLE - Challenge 4

import arcpy

# Replace "your_path" with the path where you save the geodatabase
arcpy.env.workspace = "c:/your_path/schools.gdb"

# Create buffers around schools
arcpy.Buffer_analysis("denver_schools","school_buffer_2000","2000 feet")

print "Buffer processing finished!"
