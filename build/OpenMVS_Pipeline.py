#!/usr/bin/python
#! -*- encoding: utf-8 -*-

# This file is part of OpenMVG (Open Multiple View Geometry) C++ library.

# Python implementation of the bash script written by Romuald Perrot
# Created by @vins31
# Modified by Pierre Moulon
#
# this script is for easy use of OpenMVG
#
# usage : python openmvg.py image_dir output_dir
#
# image_dir is the input directory where images are located
# output_dir is where the project must be saved
#
# if output_dir is not present script will create it
#

# Indicate the openMVG binary directory
OPENMVS_BIN = "/home/ubuntu/anna/forks/openMVS/build/bin"

# Indicate the openMVG camera sensor width directory
#CAMERA_SENSOR_WIDTH_DIRECTORY = "/home/ubuntu/anna/forks/openMVS" + "/../../openMVG/exif/sensor_width_database"

import os
import subprocess
import sys

if __name__ == "__main__":
	if len(sys.argv) < 3:
	    print ("Usage %s input_scene output_scene" % sys.argv[0])
	    sys.exit(1)

	input_scene = sys.argv[1]
	output_scene = sys.argv[2]

	print ("Using input scene  : ", input_scene)
	print ("      output_dir : ", output_scene)

	print ("1. Densify pointcloud")
	pDensify = subprocess.Popen( [os.path.join(OPENMVS_BIN, "DensifyPointCloud"),  "-i", input_scene, "-o", output_scene,
	 "--optimize", "0", "--resolution-level", "2", "-v", "4", "--number-views", "0", "--number-views-fuse", "2"] )
	pDensify.wait()


