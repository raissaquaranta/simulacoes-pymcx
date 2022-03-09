# This code runs mcx and creates the FLUENCE RATE output .nii,of a 1.5x6x6 mm of a human aorta
# irradiated by a disk source 2mm diameter with different wavelengths
# and make the graph's orientation similar to Keijzer's article ones
# It doesn't plots the graph


import pymcx as mcx


# Finding the mcx's exe on the computer
mcx_local = r'C:\Users\User\Documents\Raíssa\Curso Monte Carlo\MCXStudio\MCXSuite\mcx\bin\mcx.exe'


# Creating the simulation session
cfg = mcx.create()


# Setting number os photons, detector's position and name of the file created
cfg["Session"]["Photons"] = 1e8
# cfg["Session"]["ID"] = "FR_660_e8"      # 660 nm
# cfg["Session"]["ID"] = "FR_830_e8"      # 830 nm
cfg["Session"]["ID"] = "FR_904_e8.test"      # 904 nm

# Setting domain
cfg["Domain"]["Dim"] = [150, 600, 600]                  # 1.5x6x6mm media
cfg["Domain"]["LengthUnit"] = 0.01                      # Millimeters per voxel0


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

# # 660 nm CORRECTION
# cfg["Domain"]["Media"].append({
#      "mua": 0.03316,
#      "mus": 8.55509,
#      "g": 0.91,
#      "n": 1.37
#  })


# # 830 nm CORRECTION
# cfg["Domain"]["Media"].append({
#      "mua": 0.01006,
#      "mus": 7.34241,
#      "g": 0.91,
#      "n": 1.37
#  })



# 904 nm CORRECTION
cfg["Domain"]["Media"].append({
     "mua": 0.01038,
     "mus": 6.25059,
     "g": 0.91,
     "n": 1.37
 })

# Running mcx and trying to generate .nii file with FLUENCE RATE information
data_mch, data_mc2 = mcx.run(cfg=cfg, flag='--outputtype F --outputformat nii', mcxbin=mcx_local)


