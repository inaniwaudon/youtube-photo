from ..utils import ExtractorError as ExtractorError
from .common import InfoExtractor as InfoExtractor

class CommonMistakesIE(InfoExtractor):
    IE_DESC: bool

class UnicodeBOMIE(InfoExtractor):
    IE_DESC: bool
