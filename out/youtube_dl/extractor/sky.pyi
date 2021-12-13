from ..utils import extract_attributes as extract_attributes, smuggle_url as smuggle_url, strip_or_none as strip_or_none, urljoin as urljoin
from .common import InfoExtractor as InfoExtractor

class SkyBaseIE(InfoExtractor):
    BRIGHTCOVE_URL_TEMPLATE: str

class SkySportsIE(SkyBaseIE):
    IE_NAME: str

class SkyNewsIE(SkyBaseIE):
    IE_NAME: str

class SkySportsNewsIE(SkyBaseIE):
    IE_NAME: str
