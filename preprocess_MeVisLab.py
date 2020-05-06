import numpy as np
import os
import matplotlib.pyplot as plt
import pydicom
import cv2

PathDicom = "C:/Users/Aritra Mazumdar/Downloads/ISIC/3000566-03192"

#lstFilesDCM = []  # create an empty list
for dirName, subdirList, fileList in os.walk(PathDicom):
    for filename in fileList:
        if ".dcm" in filename.lower():  # check whether the file's DICOM

            ds = pydicom.read_file(os.path.join(dirName, filename))
            j = ds.pixel_array
            #Ribs
            #j[162:513].fill(0)
            #Spine
            #j[0:327].fill(0)
            #Vascular
            j[0:162].fill(0)
            j[327:513].fill(0)
            ds.PixelData = j.tostring()
            ds.save_as(os.path.join(dirName, filename))

