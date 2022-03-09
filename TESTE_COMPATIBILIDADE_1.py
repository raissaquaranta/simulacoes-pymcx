# VARIANDO COEF. ESPALHAMENTO
#
# This code runs mcx and creates the FLUENCE RATE output .nii,of a 1.5x6x6 mm
# 3 medias are irradiated by a disk source 2mm diameter with different scattering coefficients
# It doesn't plots the graph


import pymcx as mcx


# Finding the mcx's exe on the computer
mcx_local = r'C:\Users\User\Documents\Raíssa\Curso Monte Carlo\MCXStudio\MCXSuite\mcx\bin\mcx.exe'


# Creating the simulation session
cfg = mcx.create()


# Setting number os photons, detector's position and name of the file created
cfg["Session"]["Photons"] = 1e7
# cfg["Session"]["ID"] = "FR_MUS_0.1"
# cfg["Session"]["ID"] = "FR_MUS_1"
# cfg["Session"]["ID"] = "FR_MUS_10"
cfg["Session"]["ID"] = "FR_MUS_50"

# Setting domain
cfg["Domain"]["Dim"] = [150, 600, 600]                  # 1.5x6x6mm media
cfg["Domain"]["LengthUnit"] = 0.01                      # Millimeters per voxel


# Setting Source
cfg["Optode"]["Source"]["Type"] = "Disk"                # source type
cfg["Optode"]["Source"]["Param1"] = [100, 0, 0, 0]      # RADIUS in voxels (100 voxels = 1 mm)
cfg["Optode"]["Source"]["Pos"] = [150, 300, 300]        # source position in voxels
cfg["Optode"]["Source"]["Dir"] = [-1, 0, 0]             # source direction


# Layers and elements
cfg["Shapes"].pop()                                     # Deletes the tag 1 that is there by default
cfg["Shapes"] = [{"Grid": {"Tag": 1, "Size": [150, 600, 600]}}]


# Media properties
cfg["Domain"]["Media"].pop()                            # Deletes the last list's element

# # Media 0.1
# cfg["Domain"]["Media"].append({
#      "mua": 1,
#      "mus": 0.1,
#      "g": 0.91,
#      "n": 1.37
#  })


# # Media 1
# cfg["Domain"]["Media"].append({
#      "mua": 1,
#      "mus": 1,
#      "g": 0.91,
#      "n": 1.37
#  })


# # Media 10
# cfg["Domain"]["Media"].append({
#      "mua": 1,
#      "mus": 10,
#      "g": 0.91,
#      "n": 1.37
#  })


# Media 50
cfg["Domain"]["Media"].append({
     "mua": 1,
     "mus": 50,
     "g": 0.91,
     "n": 1.37
 })


# Running mcx and trying to generate .nii file with FLUENCE RATE information
data_mch, data_mc2 = mcx.run(cfg=cfg, flag='--outputtype F --outputformat nii', mcxbin=mcx_local)
