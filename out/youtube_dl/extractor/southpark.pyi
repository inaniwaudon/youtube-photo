from .mtv import MTVServicesInfoExtractor as MTVServicesInfoExtractor

class SouthParkIE(MTVServicesInfoExtractor):
    IE_NAME: str

class SouthParkEsIE(SouthParkIE):
    IE_NAME: str

class SouthParkDeIE(SouthParkIE):
    IE_NAME: str

class SouthParkNlIE(SouthParkIE):
    IE_NAME: str

class SouthParkDkIE(SouthParkIE):
    IE_NAME: str
