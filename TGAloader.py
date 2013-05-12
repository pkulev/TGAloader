
#!/usr/bin/env python
import os

class CTGA(object):
    def __init__(self, filename):
        """TGA Header ; Field number according to the specefication"""
        try:
            self.TGAfile = open(filename, 'rb')
        except IOError, e:
            print e
        else:
            self.DTGAColorMapSpec = None
            self.DTGAImageSpec    = None
            
            self.DTGAHeader = {
                "IDLength"     : None,                  #1 (1 byte)
                "colorMapType" : None,                  #2 {0 - color map is not included, 1 - is included} (1 byte)
                "imageType"    : None,                  #3 (1 byte)
                "colorMapSpec" : self.DTGAColorMapSpec, #4 (5 bytes)
                "imageSpec"    : self.DTGAImageSpec     #5 (10 bytes)
                }
            
            self.DTGAColorMapSpec = {
                "firstEntryIndex"   : None, #4.1 (2 bytes)
                "colorMapLength"    : None, #4.2 (2 bytes)
                "colorMapEntrySize" : None #4.3 (1 byte)
                }
            
            self.DTGAImageSpec = {
                "xOrigin"         : None, #5.1 (2 bytes)
                "yOrigin"         : None, #5.2 (2 bytes)
                "imageWidth"      : None, #5.3 (2 bytes)
                "imageHeight"     : None, #5.4 (2 bytes)
                "pixelDepth"      : None, #5.5 (1 byte)
                "imageDescriptor" : None  #5.6 (1 byte)
                }
            
            self.DTGAImageAndColorMapData = {      
                "imageID"      : None, #6 (IDLength bytes)
                "colorMapData" : None, #7 (colorMapLength bytes)
                "imageData"    : None  #8 
                }
            
            self.DTGADevArea = None
            self.DTGAExtArea = None    #10 - 27 fields
            
            self.DTGAFooter = {  #(26 bytes)
                "extOffset"      : None, #28 (4 bytes)
                "devAreaOffset"  : None, #29 (4 bytes)
                "signature"      : None, #30 (16 bytes)
                "reservedChar"   : None, #31 (1 byte)
                "terminator"     : None  #32 (1 byte)
                }  
        
            self.DTGAFile = {
                "DTGAHeader"               : self.DTGAHeader,
                "DTGAImageAndColorMapData" : self.DTGAImageAndColorMapData,
                "DTGADevArea"              : self.DTGADevArea,
                "DTGAExtArea"              : self.DTGAExtArea,
                "DTGAFooter"               : self.DTGAFooter
                }
            
            self.readTGA()


        
    def validate(TGAfile):
        return True

    def toInt(self, s): #DANGEROUS
        print type(s)
        print "lololo = " + s
        s = s[2:]
        return 2#int(s, 16)

    def readHeader(self):
        self.TGAfile.seek(0)
        self.DTGAHeader["IDLength"] = self.TGAfile.read(1)
        self.DTGAHeader["ColorMapType"] = self.TGAfile.read(1)
        self.DTGAHeader["imageType"] = self.TGAfile.read(1)
    
        self.DTGAColorMapSpec["firstEntryIndex"] = self.TGAfile.read(2)
        self.DTGAColorMapSpec["colorMapLength"] = self.toInt(self.TGAfile.read(2))
        self.DTGAColorMapSpec["colorMapEntrySize"] = self.TGAfile.read(1)

        self.DTGAImageSpec["xOrigin"] = self.TGAfile.read(2)
        self.DTGAImageSpec["yOrigin"] = self.TGAfile.read(2)
        self.DTGAImageSpec["imageWidth"] = self.TGAfile.read(2)
        self.DTGAImageSpec["imageHeight"] = self.TGAfile.read(2)
        self.DTGAImageSpec["pixelDepth"] = self.TGAfile.read(1)
        self.DTGAImageSpec["imageDescriptor"] = self.TGAfile.read(1)

    def printHeader(self):
        print self.DTGAHeader
        #print self.DTGAImageAndColorMapData

    def readImageAndColorMapData(self):
        self.DTGAImageAndColorMapData["imageID"] = self.TGAfile.read(self.DTGAHeader["IDLength"])
        self.DTGAImageAndColorMapData["colorMapData"] = self.TGAfile.read(self.DTGAColorMapSpec["colorMapData"])

    def readTGA(self):
        #self.readHeader()
        #self.readImageAndColorMapData()
        self.readFooter(self.TGAfile)

    def readFooter(self, TGAfile):
        TGAfile.seek(-18, os.SEEK_END)
        self.DTGAFooter["extOffset"] = TGAfile.read(16)
        print self.DTGAFooter["extOffset"]
        """self.DTGAFooter["devAreaOffset"] = self.TGAfile.read(4)
        self.DTGAFooter["signature"] = self.TGAfile.read(16)
        self.DTGAFooter["reservedChar"] = self.TGAfile.read(1)
        self.DTGAFooter["terminator"] = self.TGAfile.read(1)
        """
