from osgeo import gdal
from gdalconst import *
from pyproj import Proj
from gdal import GetDriverByName
import numpy
from numpy import nan_to_num
from numpy import add, subtract, divide, multiply
import math
import os
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import scipy.misc as sm

class NDVI:
    TAG = "NDVI.class"
    open_B4 = None
    open_B5 = None
    isOpenB4 = False
    isOpenB5 = False

    crop_B4 = None
    crop_B5 = None

    correctionB4Reflectance = None
    correctionB5Reflectance = None
    correctionB4Radiance = None
    correctionB4Radiance
    isCorrection = False

    ndviResult = None
    listener = None
    isCropped = False
    metadataPath = None
    cols = 0
    rows = 0
    output_cols = 0
    output_rows = 0

    lonStartCrop = 0
    latStartCrop = 0
    lonEndCrop = 0
    latEndCrop = 0

    lonStartDefault = 0
    latStartDefault = 0
    lonEndDefault = 0
    latEndDefault = 0

    isMtl = False

    b4MultiReflectance = 0
    b4AddReflectance = 0
    b5MultiReflectance = 0
    b5AddReflectance = 0

    b4MultiRadiance = 0
    b4AddRadiance = 0
    b5MultiRadiance = 0
    b5AddRadiance = 0

    sunElevation = 0

    data_B4 = 0
    data_B5 = 0

    dataB4Reflectance = None
    dataB5Reflectance = None

    isNdvi = False

    def __init__(self):
        print("NDVI instance created")

    def OpenB4File(self, path):
        if "B4" in path:
            print(self.TAG, "Band 4 path:", path)
            self.open_B4 = gdal.Open(path, GA_ReadOnly)
            self.isCropped = False
            self.isOpenB4 = True
        else:
            self.isOpenB4 = False

    def OpenB5File(self, path):
        if "B5" in path:
            print(self.TAG, "Band 5 path:", path)
            self.open_B5 = gdal.Open(path, GA_ReadOnly)
            self.isCropped = False
            self.isOpenB5 = True
        else:
            self.isOpenB5 = False

    def SetCropCoordinate(self, lonStart, lonEnd, latStart, latEnd):
        self.lonStartCrop = lonStart
        self.lonEndCrop = lonEnd
        self.latStartCrop = latStart
        self.latEndCrop = latEnd

        issue = []

        if self.lonStartCrop < self.lonStartDefault or self.lonStartCrop > self.lonEndDefault:
            issue.append("Longitude start crop less the limit")
        if self.latStartCrop < self.latStartDefault or self.latStartCrop > self.latEndDefault:
            issue.append("Latitude start crop less the limit")
        if self.lonEndCrop > self.lonEndDefault or self.lonEndCrop < self.lonStartDefault:
            issue.append("Longitude end crop exceeds the limit")
        if self.latEndCrop > self.latEndDefault or self.latEndCrop < self.latStartDefault:
            issue.append("Latitude end crop exceeds the limit")

        if issue:
            issueBuf = ""
            for item in issue:
                issueBuf += item + "\n"
                print(issueBuf)
            self.listener.showMessageError("Crop failed\n\n" + issueBuf)


        print("lonStart: ", self.lonStartCrop)
        print("lonEnd: ", self.lonEndCrop)
        print("latStart: ", self.latStartCrop)
        print("latEnd: ", self.latEndCrop)

    def OpenMtlFile(self, path):
        issue = []
        issue.clear()
        if "mtl" in path.lower():
            file = open(path, 'r')
            line = file.readlines()

            for x in line:
                if x.startswith("    CORNER_UL_LON_PRODUCT"):
                    data = x.split()
                    lonStart = data[2]
                    print("Lon start: " + lonStart)
                    self.lonStartDefault = lonStart

                if x.startswith("    CORNER_UR_LAT_PRODUCT"):
                    data = x.split()
                    latStart = data[2]
                    print("Lat Start: " + latStart)
                    self.latStartDefault = latStart

                if x.startswith("    CORNER_UR_LON_PRODUCT"):
                    data = x.split()
                    lonEnd = data[2]
                    print("Lon end: " + lonEnd)
                    self.lonEndDefault = lonEnd

                if x.startswith("    CORNER_LL_LAT_PRODUCT"):
                    data = x.split()
                    latEnd = data[2]
                    print("lat end: " + latEnd)
                    self.latEndDefault = latEnd

                if x.startswith("    REFLECTANCE_MULT_BAND_4"):
                    data = x.split()
                    result = data[2]
                    print("b4MultiReflectance: " + result)
                    self.b4MultiReflectance = result

                if x.startswith("    REFLECTANCE_ADD_BAND_4"):
                    data = x.split()
                    result = data[2]
                    print("b4AddReflectance: " + result)
                    self.b4AddReflectance = result

                if x.startswith("    REFLECTANCE_MULT_BAND_5"):
                    data = x.split()
                    result = data[2]
                    print("b5MultiReflectance: " + result)
                    self.b5MultiReflectance = result

                if x.startswith("    REFLECTANCE_ADD_BAND_5"):
                    data = x.split()
                    result = data[2]
                    print("b5AddReflectance: " + result)
                    self.b5AddReflectance = result

                if x.startswith("    RADIANCE_MULT_BAND_4"):
                    data = x.split()
                    result = data[2]
                    print("b4MultiRadiance: " + result)
                    self.b4MultiRadiance = result

                if x.startswith("    RADIANCE_ADD_BAND_4"):
                    data = x.split()
                    result = data[2]
                    print("b4AddRadiance: " + result)
                    self.b4AddRadiance = result

                if x.startswith("    RADIANCE_MULT_BAND_5"):
                    data = x.split()
                    result = data[2]
                    print("b5MultiRadiance: " + result)
                    self.b5MultiRadiance = result

                if x.startswith("    RADIANCE_ADD_BAND_5"):
                    data = x.split()
                    result = data[2]
                    print("b5AddRadiance: " + result)
                    self.b5AddRadiance = result

                if x.startswith("    SUN_ELEVATION"):
                    data = x.split()
                    result = data[2]
                    print("sun elevation: " + result)
                    self.sunElevation = result

            # check imprt value from mtl file

            if self.lonStartDefault == 0:
                issue.append("CORNER_UL_LON_PRODUCT not found")
            if self.latStartDefault == 0:
                issue.append("CORNER_UR_LAT_PRODUCT not found")
            if self.lonEndDefault == 0:
                issue.append("CORNER_UR_LON_PRODUCT not found")
            if self.latEndDefault == 0:
                issue.append("CORNER_LL_LAT_PRODUCT not found")
            if self.b4MultiReflectance == 0:
                issue.append("REFLECTANCE_MULT_BAND_4 not found")
            if self.b4AddReflectance == 0:
                issue.append("REFLECTANCE_ADD_BAND_4 not found")
            if self.b5MultiReflectance == 0:
                issue.append("REFLECTANCE_MULT_BAND_5 not found")
            if self.b5AddReflectance == 0:
                issue.append("REFLECTANCE_ADD_BAND_5 not found")
            if self.b4MultiRadiance == 0:
                issue.append("RADIANCE_MULT_BAND_4 not found")
            if self.b4AddRadiance == 0:
                issue.append("RADIANCE_ADD_BAND_4 not found")
            if self.b5MultiRadiance == 0:
                issue.append("RADIANCE_MULT_BAND_5 not found")
            if self.b5AddRadiance == 0:
                issue.append("RADIANCE_ADD_BAND_5 not found")
            if self.sunElevation == 0:
                issue.append("SUN_ELEVATION not found")

            if issue:
                issueBuf = ""
                for item in issue:
                    issueBuf += item + "\n"
                self.listener.showMessageError("Import mtl file failed\n\n" + issueBuf + "\n" + "Its caused by wrong mtl file imported")
                self.isMtl = False
            else:
                self.listener.showMessage("Successfully import mtl file")
                self.isMtl = True
        else:
            self.listener.showMessageError("Wrong mtl file imported")

    def CropImage(self):
        self.cols = self.open_B4.RasterXSize
        self.rows = self.open_B4.RasterYSize
        bands = self.open_B4.RasterCount
        print("cols: ", self.cols, "\nrows: ", self.rows, "\nbands: ", bands)

        gt = self.open_B4.GetGeoTransform()
        print("GeoTransform: ", gt)
        x0 = gt[0]
        y0 = gt[3]
        pwidth = gt[1]
        pheight = gt[5]
        x_end = self.cols * pwidth + x0
        y_end = self.cols * pheight + y0

        myProj = Proj("+proj=utm +zone=50, +north +ellps=WGS84 +datum=WGS84 +units=m +no_defs")
        lon, lat = myProj(x0, y0, inverse=True)
        x_utm, y_utm = myProj(lon, lat)
        print("lon: ", lon, "\nlat: ", lat)
        print("x_utm", x_utm, "\ny_utm", y_utm)

        x_mulai_crop_utm, y_mulai_crop_utm = myProj(self.lonStartCrop, self.latStartCrop)
        x_akhir_crop_utm, y_akhir_crop_utm = myProj(self.lonEndCrop, self.latEndCrop)
        print("x_mulai_crop_utm: ", x_mulai_crop_utm, "\ny_mulai_crop_utm: ", y_mulai_crop_utm, "\nx_akhir_crop_utm: ",
              x_akhir_crop_utm, "\nx_akhir_crop_utm: ", y_akhir_crop_utm)

        xoff = int((x_mulai_crop_utm - x0) / pwidth)
        yoff = int((y_mulai_crop_utm - y0) / pheight)
        print("xoff: ", xoff, "\nyoff: ", yoff)

        self.output_cols = int((x_akhir_crop_utm - x_mulai_crop_utm) / pwidth)
        self.output_rows = int((y_akhir_crop_utm - y_mulai_crop_utm) / pheight)

        print("output_cols: ", self.output_cols)
        print("output_rows: ", self.output_rows)

        band_B4 = self.open_B4.GetRasterBand(1)
        band_B5 = self.open_B5.GetRasterBand(1)

        self.crop_B4 = band_B4.ReadAsArray(xoff, yoff, self.output_cols, self.output_rows)
        self.crop_B5 = band_B5.ReadAsArray(xoff, yoff, self.output_cols, self.output_rows)

        print("\nData Band 4: \n", self.crop_B4, "\n")
        print("Data Band 5: \n", self.crop_B5, "\n")

        self.isCropped = True

        if self.listener is not None:
            self.listener.onCropFinish(self.crop_B4, self.crop_B5)

    def setupFullImage(self):
        self.cols = self.open_B4.RasterXSize
        self.rows = self.open_B4.RasterYSize
        bands = self.open_B4.RasterCount
        print("cols: ", self.cols, "\nrows: ", self.rows, "\nbands: ", bands)

        self.output_cols = self.cols
        self.output_rows = self.rows

        band_B4 = self.open_B4.GetRasterBand(1)
        band_B5 = self.open_B5.GetRasterBand(1)

        self.data_B4 = band_B4.ReadAsArray(0, 0, self.output_cols, self.output_rows)
        self.data_B5 = band_B5.ReadAsArray(0, 0, self.output_cols, self.output_rows)

    def StartCorrection(self):
        if self.isCropped:
            b4MultiReflectance = float(self.b4MultiReflectance)
            b4AddReflectance = float(self.b4AddReflectance)
            b5MultiReflectance = float(self.b5MultiReflectance)
            b5AddReflectance = float(self.b5AddReflectance)

            b4MultiRadiance = float(self.b4MultiRadiance)
            b4AddRadiance = float(self.b4AddRadiance)
            b5MultiRadiance = float(self.b5MultiRadiance)
            b5AddRadiance = float(self.b5AddRadiance)

            sun_elevation = float(self.sunElevation)

            dataB4Reflectance = (self.crop_B4 * b4MultiReflectance) + b4AddReflectance
            dataB5Reflectance = (self.crop_B5 * b5MultiReflectance) + b5AddReflectance

            dataB4Radiance = (self.crop_B4 * b4MultiRadiance) + b4AddRadiance
            dataB5Radiance = (self.crop_B5 * b5MultiRadiance) + b5AddRadiance

            print("dataB4Reflectance: " + str(dataB4Reflectance))
            print("dataB5Reflectance: " + str(dataB5Reflectance))
            print("dataB4Radiance: " + str(dataB4Radiance))
            print("dataB5Radiance: " + str(dataB5Radiance))

            self.correctionB4Reflectance = dataB4Reflectance / math.sin(sun_elevation) * 65536
            self.correctionB5Reflectance = dataB5Reflectance / math.sin(sun_elevation) * 65536

            self.correctionB4Radiance = dataB4Radiance / math.sin(sun_elevation) * 65536
            self.correctionB5Radiance = dataB5Radiance / math.sin(sun_elevation) * 65536

            print("correctionB4Reflectance: " + str(self.correctionB4Reflectance))
            print("correctionB5Reflectance: " + str(self.correctionB5Reflectance))
            print("correctionB4Radiance: " + str(self.correctionB4Radiance))
            print("correctionB5Radiance: " + str(self.correctionB5Radiance))

            self.isCorrection = True

            if self.listener is not None:
                self.listener.onCorrectionFinish(
                    self.correctionB4Reflectance, 
                    self.correctionB5Reflectance, 
                    self.correctionB4Radiance, 
                    self.correctionB5Radiance
                )

    def StartNDVI(self):
        data_B4_32 = self.correctionB4Reflectance.astype(numpy.float32)
        data_B5_32 = self.correctionB5Reflectance.astype(numpy.float32)

        numerator = subtract(data_B5_32, data_B4_32)
        denominator = add(data_B5_32, data_B4_32)
        self.ndviResult = divide(numerator, denominator)

        print("NDVI: \n", self.ndviResult, "\n")

        self.isNdvi = True

        if self.listener is not None:
            self.listener.onNDVIFinish(self.ndviResult)

    def SetOnProcessFinishListener(self, listener):
        self.listener = listener

    def SaveResult(self, path):
        geotiff = GetDriverByName('Gtiff')
        output = geotiff.Create(path, self.output_cols, self.output_rows, 1, gdal.GDT_Float32)
        output_band = output.GetRasterBand(1)
        output_band.WriteArray(self.ndviResult)
        output.SetGeoTransform(self.open_B4.GetGeoTransform())
        print("File created successfully.")

    def SaveRed(self, path):
        plt.imshow(self.crop_B4)
        plt.savefig(path)
        print("File created successfully.")

    def SaveNir(self, path):
        plt.imshow(self.crop_B5)
        plt.savefig(path)
        print("File created successfully.")

    def SaveReflectanceNir(self, path):
        plt.imshow(self.correctionB5Reflectance)
        plt.savefig(path)
        print("File created successfully.")

    def SaveReflectanceRed(self, path):
        plt.imshow(self.correctionB4Reflectance)
        plt.savefig(path)
        print("File created successfully.")

    def SaveRadianceNir(self, path):
        plt.imshow(self.correctionB5Radiance)
        plt.savefig(path)
        print("File created successfully.")

    def SaveRadianceRed(self, path):
        plt.imshow(self.correctionB4Radiance)
        plt.savefig(path)
        print("File created successfully.")


class OnProcessFinishListener:
    def onNDVIFinish(self, result):
        print("ndvi finished")

    def onCropFinish(self, red, nir):
        print("crop finished")

    def onCorrectionFinish(self, red, nir):
        print("Correction`finished")

    def showMessage(self, message):
        print("show message info")

    def showMessageError(self, message):
        print("show message error")