
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
            self.TGAColorMapSpec = None
            self.TGAImageSpec    = None
            
            self.TGAHeader = {
                "IDLength"     : None,                  #1 (1 byte)
                "colorMapType" : None,                  #2 {0 - color map is not included, 1 - is included} (1 byte)
                "imageType"    : None,                  #3 (1 byte)
                "colorMapSpec" : self.TGAColorMapSpec, #4 (5 bytes)
                "imageSpec"    : self.TGAImageSpec     #5 (10 bytes)
                }
            
            self.TGAColorMapSpec = {
                "firstEntryIndex"   : None, #4.1 (2 bytes)
                "colorMapLength"    : None, #4.2 (2 bytes)
                "colorMapEntrySize" : None #4.3 (1 byte)
                }
            
            self.TGAImageSpec = {
                "xOrigin"         : None, #5.1 (2 bytes)
                "yOrigin"         : None, #5.2 (2 bytes)
                "imageWidth"      : None, #5.3 (2 bytes)
                "imageHeight"     : None, #5.4 (2 bytes)
                "pixelDepth"      : None, #5.5 (1 byte)
                "imageDescriptor" : None  #5.6 (1 byte)
                }
            
            self.TGAImageAndColorMapData = {      
                "imageID"      : None, #6 (IDLength bytes)
                "colorMapData" : None, #7 (colorMapLength bytes)
                "imageData"    : None  #8 
                }
            
            self.TGADevArea = None
            self.TGAExtArea = None    #10 - 27 fields

            self.footerLength = 26
            self.TGAFooter = {  #(26 bytes)
                "extOffset"      : None, #28 (4 bytes)
                "devAreaOffset"  : None, #29 (4 bytes)
                "signature"      : None, #30 (16 bytes)
                "reservedChar"   : None, #31 (1 byte)
                "terminator"     : None  #32 (1 byte)
                }  
        
            self.TGAFile = {
                "TGAHeader"               : self.TGAHeader,
                "TGAImageAndColorMapData" : self.TGAImageAndColorMapData,
                "TGADevArea"              : self.TGADevArea,
                "TGAExtArea"              : self.TGAExtArea,
                "TGAFooter"               : self.TGAFooter
                }
            
            self.readTGA()


        
    def validate(TGAfile):
        return True

    def toInt(self, s):
        print type(s)
        print "lololo = " + s
        s = s[2:]
        return int(s, 16)

    def readHeader(self):
        self.TGAfile.seek(0)
        self.TGAHeader["IDLength"] = self.TGAfile.read(1)
        self.TGAHeader["ColorMapType"] = self.TGAfile.read(1)
        self.TGAHeader["imageType"] = self.TGAfile.read(1)
    
        self.TGAColorMapSpec["firstEntryIndex"] = self.TGAfile.read(2)
        self.TGAColorMapSpec["colorMapLength"] = self.TGAfile.read(2)
        self.TGAColorMapSpec["colorMapEntrySize"] = self.TGAfile.read(1)

        self.TGAImageSpec["xOrigin"] = self.TGAfile.read(2)
        self.TGAImageSpec["yOrigin"] = self.TGAfile.read(2)
        self.TGAImageSpec["imageWidth"] = self.TGAfile.read(2)
        self.TGAImageSpec["imageHeight"] = self.TGAfile.read(2)
        self.TGAImageSpec["pixelDepth"] = self.TGAfile.read(1)
        self.TGAImageSpec["imageDescriptor"] = self.TGAfile.read(1)

    def printHeader(self):
        print self.TGAHeader
        #print self.TGAImageAndColorMapData

    def readImageAndColorMapData(self):
        self.TGAImageAndColorMapData["imageID"] = self.TGAfile.read(self.TGAHeader["IDLength"])
        self.TGAImageAndColorMapData["colorMapData"] = self.TGAfile.read(self.TGAColorMapSpec["colorMapData"])

    def readTGA(self):
        #self.readHeader()
        #self.readImageAndColorMapData()
        self.readFooter(self.TGAfile)

    def readFooter(self, TGAfile):
        TGAfile.seek(-self.footerLength, os.SEEK_END)
        self.TGAFooter["extOffset"] = TGAfile.read(4)
        self.TGAFooter["devAreaOffset"] = self.TGAfile.read(4)
        self.TGAFooter["signature"] = self.TGAfile.read(16)
        self.TGAFooter["reservedChar"] = self.TGAfile.read(1)
        self.TGAFooter["terminator"] = self.TGAfile.read(1)
        
    #def printFooter(

