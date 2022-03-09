# This code runs mcx and creates the FLUENCE RATE output .nii,of a 3x6x6 mm of a human SKIN
# irradiated by a disk source 2mm diameter with different wavelengths
# and make the graph's orientation similar to Keijzer's article ones
# It doesn't plots the graph


import pymcx as mcx
import matplotlib.pyplot as plt
import numpy as np
import nibabel as nii
import seaborn as sns


# Finding the mcx's exe on the computer
mcx_local = r'C:\Users\User\Documents\Raíssa\Curso Monte Carlo\MCXStudio\MCXSuite\mcx\bin\mcx.exe'


# Creating the simulation session
cfg = mcx.create()


# Setting number os photons, detector's position and name of the file created
cfg["Session"]["Photons"] = 1e8
# cfg["Session"]["ID"] = "FR_660_PEN_OP"      # 660 nm
# cfg["Session"]["ID"] = "FR_830_PEN_OP"      # 830 nm
cfg["Session"]["ID"] = "FR_904_PEN_OP"      # 904 nm

# Setting domain
cfg["Domain"]["Dim"] = [300, 600, 600]                  # 1.5x6x6mm media
cfg["Domain"]["LengthUnit"] = 0.01                      # Millimeters per voxel


# Setting Source
cfg["Optode"]["Source"]["Type"] = "Disk"                # source type
cfg["Optode"]["Source"]["Param1"] = [100, 0, 0, 0]      # RADIUS in voxels (100 voxels = 1 mm)
cfg["Optode"]["Source"]["Pos"] = [300, 300, 300]        # source position in voxels
cfg["Optode"]["Source"]["Dir"] = [-1, 0, 0]             # source direction


# Layers and elements
cfg["Shapes"].pop()                                     # Deletes the tag 1 that is there by default
cfg["Shapes"] = [{"Grid": {"Tag": 1, "Size": [300, 600, 600]}}]


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


# # Loading the image with 1e8 photons
# image1 = nii.load(r'C:\Users\User\Documents\Raíssa\Curso Monte Carlo\pymcx-master\pymcx\FR_660_PEN_OP.nii')
#
#
# # Getting the 3D data array
# data1 = image1.get_fdata()
# data1 = np.squeeze(data1)  # Removing the time dimension
#
#
# # Scale Vectors
# Y = np.linspace(-3, 0,300)
# X = np.linspace(-3, 3, 600)
#
#
# # # Plot to get the optical penetration length 600X600X300
# plt.rcParams.update({'font.size': 10})  # Font size
# sns.set_theme()
#
# fig,axs = plt.subplots(1, figsize=(14, 7))
#
# plt.suptitle('Fluence Rate $W/cm^2$', y=1, x=0.43)
#
# plt.subplots_adjust(hspace=0.5)   # Pushing up the title
#
# axs.set_title('660 nm - Lateral View - $10^8$ photons')
#
# # Actual Lateral View Plot
# axs.contour(X, Y, 100*data1[:, 300, :], cmap="jet", levels=['8', '17.6', '24', '32', '40', '48', '56'])
# #  *100 to convert to J/cm^2
# img2 = axs.contour(X, Y, 100*data1[:, 300, :], cmap="jet", levels=['8', '17.6', '24', '32', '40', '48', '56'])
# #  Creates an object with the plot
# fig.colorbar(img2, ax=axs)  # Generates the particular colorbar
#
# # Legend for the axis
# fig.text(0.43, 0.02, 'Side [mm]', ha='center')
# fig.text(0.04, 0.5, 'Depth [mm]', va='center', rotation='vertical')
#
# # Saving and Showing
# # plt.savefig("FluenceRate660LateralView_3x6x6.jpg")
# plt.show()

# # Plot optical penetration length
#
# # Loading the images with 1e8 photons
# # 660nm
# kjzimg4 = nii.load(r'C:\Users\User\Documents\Raíssa\Curso Monte Carlo\pymcx-master\pymcx\FR_660_e8.nii')
# # 1 mm
# kjzimg5 = nii.load(r'C:\Users\User\Documents\Raíssa\Curso Monte Carlo\pymcx-master\pymcx\FR_830_e8.nii')
# # 4 mm
# kjzimg6 = nii.load(r'C:\Users\User\Documents\Raíssa\Curso Monte Carlo\pymcx-master\pymcx\FR_904_e8.nii')
#
# # Getting the 3D data array
# kjzdata4 = kjzimg4.get_fdata()
# kjzdata4 = np.squeeze(kjzdata4)
# kjzdata5 = kjzimg5.get_fdata()
# kjzdata5 = np.squeeze(kjzdata5)
# kjzdata6 = kjzimg6.get_fdata()
# kjzdata6 = np.squeeze(kjzdata6)
#
# # Vector to Scale Correction
# Y = np.linspace(1.5, 0, 150)
#
# # Plot commands
# sns.set_theme()
# fig, axs = plt.subplots(1, figsize = (10, 7))
# plt.suptitle('Diferentes Comprimentos de Onda', y=0.975, x=0.51, fontsize=20)
# plt.subplots_adjust(hspace=0.5)   # Pushing up the title
# axs.set_title('$10^8$ photons', fontsize=15)
#
# # Actual Lateral View Plot
# axs.plot(Y, 100*kjzdata4[:, 300, 300], color='blue', label='660 nm')
# axs.plot(Y, 100*kjzdata5[:, 300, 300], color='green', label='830 nm')
# axs.plot(Y, 100*kjzdata6[:, 300, 300], color='red', label='904 nm')
# plt.legend(loc=1, prop={'size': 15})
#
#
# # # Legend for the axis
# axs.set_xlabel('Depth [mm]', fontsize=18)
# plt.xticks(fontsize=15)
# plt.yticks(fontsize=15)
# axs.set_ylabel('Fluence Rate [W/$cm^2$]', fontsize=18)
# # plt.rc('xtick', labelsize=25)
# # plt.rc('ytick', labelsize=15)
#
#
# # # Saving and Showing
# # plt.savefig("FluenceRateDecay_e8.jpg")
# plt.show()



