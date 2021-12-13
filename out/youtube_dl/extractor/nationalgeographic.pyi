from ..utils import smuggle_url as smuggle_url, url_basename as url_basename
from .common import InfoExtractor as InfoExtractor
from .fox import FOXIE as FOXIE

class NationalGeographicVideoIE(InfoExtractor):
    IE_NAME: str

class NationalGeographicTVIE(FOXIE): ...
