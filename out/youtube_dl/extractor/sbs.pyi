from ..utils import ExtractorError as ExtractorError, smuggle_url as smuggle_url
from .common import InfoExtractor as InfoExtractor

class SBSIE(InfoExtractor):
    IE_DESC: str
