
#!/usr/bin/env python

class CTGA(object):
    def __init__(self):
        """TGA Header ; Field number according to the specefication"""
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
            "Signature"      : None, #30 (16 bytes)
            "reservedChar"   : None, #31 (1 byte)
            "terminator"     : None  #32 (1 byte)
            }  
        
        self.DTGAFile = {
            "DTGAHeader"               : DTGAHeader,
            "DTGAImageAndColorMapData" : DTGAImageAndColorMapData,
            "DTGADevArea"              : DTGADevArea,
            "DTGAExtArea"              : DTGAExtArea,
            "DTGAFooter"               : DTGAFooter
            }
   
        def readHeader(self):
            pass
