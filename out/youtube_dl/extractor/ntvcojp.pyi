from ..utils import js_to_json as js_to_json, smuggle_url as smuggle_url
from .common import InfoExtractor as InfoExtractor

class NTVCoJpCUIE(InfoExtractor):
    IE_NAME: str
    IE_DESC: str
    BRIGHTCOVE_URL_TEMPLATE: str
