from ..utils import update_url_query as update_url_query
from .mtv import MTVServicesInfoExtractor as MTVServicesInfoExtractor

class NickIE(MTVServicesInfoExtractor):
    IE_NAME: str

class NickBrIE(MTVServicesInfoExtractor):
    IE_NAME: str

class NickDeIE(MTVServicesInfoExtractor):
    IE_NAME: str

class NickNightIE(NickDeIE):
    IE_NAME: str

class NickRuIE(MTVServicesInfoExtractor):
    IE_NAME: str
