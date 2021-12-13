from ..utils import ExtractorError as ExtractorError
from .common import InfoExtractor as InfoExtractor
from .rutv import RUTVIE as RUTVIE

class VestiIE(InfoExtractor):
    IE_DESC: str
